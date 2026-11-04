#!/usr/bin/env python3
"""Read synthetic workflow JSON; no C2, endpoint actions, download, or file writes.
This teaching state model is not a parser for actual Cobalt Strike logs.
Python 3.10+, standard library. Existing UTF-8 JSON input <=64 KiB.
"""
import argparse
import copy
import hashlib
import json
import re
import sys
from pathlib import Path
LIMIT=65536


def reduce_events(events):
    if not isinstance(events,list) or len(events)>200:
        raise ValueError('Expected a list of at most 200 synthetic events')
    sessions={};tasks={};transfers={};jobs={}
    def ident(e,key):
        v=e.get(key)
        if not isinstance(v,str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,48}',v):
            raise ValueError('Invalid identifier: '+key)
        return v
    def count(e,key):
        v=e.get(key)
        if type(v) is not int or not 0<=v<=1_048_576:
            raise ValueError('Invalid byte count: '+key)
        return v
    def digest(e,key):
        v=e.get(key)
        if not isinstance(v,str) or not re.fullmatch('[0-9a-f]{64}',v):
            raise ValueError('Invalid SHA256: '+key)
        return v
    for i,e in enumerate(events):
        try:
            if not isinstance(e,dict):raise ValueError('Event must be an object')
            kind=e.get('event');sid=ident(e,'session')
            if kind=='session_seen':
                if sid in sessions:raise ValueError('Duplicate session id')
                sessions[sid]={'connected':True};continue
            if sid not in sessions:raise ValueError('Unknown session')
            if kind=='session_disconnected':sessions[sid]['connected']=False;continue
            if kind.startswith('task_'):
                tid=ident(e,'task');key=(sid,tid)
                if kind=='task_queued':
                    if key in tasks:raise ValueError('Duplicate task id in session')
                    tasks[key]={'state':'queued','output_chunks':0}
                else:
                    if key not in tasks:raise ValueError('Unknown task')
                    t=tasks[key]
                    if kind=='task_delivered' and t['state']=='queued':t['state']='delivered'
                    elif kind=='task_output' and t['state'] in ('delivered','output_received'):
                        t['state']='output_received';t['output_chunks']+=1
                    elif kind=='task_completed' and t['state'] in ('delivered','output_received'):
                        status=e.get('result')
                        if status not in ('success','failed'):raise ValueError('Invalid task result')
                        t['state']='completed_'+status
                    else:raise ValueError('Invalid task transition')
            elif kind.startswith('transfer_'):
                fid=ident(e,'transfer');key=(sid,fid)
                if kind=='transfer_started':
                    if key in transfers:raise ValueError('Duplicate transfer id')
                    transfers[key]={'state':'receiving','total':count(e,'total'),'received':0,'expected_sha256':digest(e,'sha256')}
                else:
                    if key not in transfers:raise ValueError('Unknown transfer')
                    f=transfers[key]
                    if kind=='transfer_progress' and f['state']=='receiving':
                        n=count(e,'received')
                        if not f['received']<=n<=f['total']:raise ValueError('Nonmonotonic or oversized progress')
                        f['received']=n
                    elif kind=='transfer_server_complete' and f['state']=='receiving' and f['received']==f['total']:
                        f['state']='server_complete'
                    elif kind=='transfer_client_synced' and f['state']=='server_complete':
                        if count(e,'bytes')!=f['total'] or digest(e,'sha256')!=f['expected_sha256']:
                            raise ValueError('Client size or SHA256 mismatch')
                        f['state']='client_synced'
                    else:raise ValueError('Invalid transfer transition')
            elif kind.startswith('job_'):
                jid=ident(e,'job');key=(sid,jid)
                if kind=='job_started':
                    if key in jobs:raise ValueError('Duplicate job id')
                    jobs[key]={'state':'running'}
                else:
                    if key not in jobs:raise ValueError('Unknown job')
                    j=jobs[key]
                    if kind=='job_stop_requested' and j['state']=='running':j['state']='stop_requested'
                    elif kind=='job_stopped' and j['state']=='stop_requested':j['state']='stopped'
                    else:raise ValueError('Invalid job transition')
            else:raise ValueError('Unknown event type')
        except (ValueError,AttributeError) as exc:
            raise ValueError(f'Event {i}: {exc}') from exc
    def flatten(items):return [{'session':s,'id':n,**v} for (s,n),v in items.items()]
    return {'sessions':sessions,'tasks':flatten(tasks),'transfers':flatten(transfers),'jobs':flatten(jobs),
            'limits':'Synthetic model only. No actual Cobalt Strike log parsing, connection, execution, or byte transfer verification.'}


def inspect_bytes(raw):
    if len(raw)>LIMIT:raise ValueError('Input exceeds 65536 bytes')
    data=json.loads(raw.decode('utf-8-sig'))
    return {'input_sha256':hashlib.sha256(raw).hexdigest(),**reduce_events(data)}


def demo_cases():
    h=hashlib.sha256(b'TRAINING_ONLY\n').hexdigest();n=len(b'TRAINING_ONLY\n')
    start=[{'event':'session_seen','session':'S-A'}]
    task=start+[{'event':'task_queued','session':'S-A','task':'T-1'}, {'event':'task_delivered','session':'S-A','task':'T-1'}, {'event':'task_output','session':'S-A','task':'T-1'}]
    server=start+[{'event':'transfer_started','session':'S-A','transfer':'F-1','total':n,'sha256':h},{'event':'transfer_progress','session':'S-A','transfer':'F-1','received':n},{'event':'transfer_server_complete','session':'S-A','transfer':'F-1'}]
    synced=server+[{'event':'transfer_client_synced','session':'S-A','transfer':'F-1','bytes':n,'sha256':h}]
    wrong=copy.deepcopy(synced);wrong[-1]['sha256']='0'*64
    disconnect=start+[{'event':'job_started','session':'S-A','job':'J-1'},{'event':'session_disconnected','session':'S-A'}]
    premature=start+[{'event':'task_queued','session':'S-A','task':'T-1'},{'event':'task_completed','session':'S-A','task':'T-1','result':'success'}]
    return [('output-without-completion',task),('server-only',server),('client-synced',synced),('wrong-client-hash',wrong),('disconnect-with-running-job',disconnect),('completion-before-delivery',premature)]


def main():
    ap=argparse.ArgumentParser(description=__doc__);g=ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--demo',action='store_true');g.add_argument('--json',type=Path,help='Existing synthetic-event JSON file')
    args=ap.parse_args()
    if args.demo:
        for name,events in demo_cases():
            try:out=reduce_events(events)
            except ValueError as exc:out={'error':str(exc)}
            print(json.dumps({'case':name,**out},ensure_ascii=False))
        return 0
    try:
        with args.json.open('rb') as f:raw=f.read(LIMIT+1)
        print(json.dumps(inspect_bytes(raw),ensure_ascii=False,indent=2))
    except (OSError,ValueError,UnicodeError) as exc:
        print(json.dumps({'error':str(exc)},ensure_ascii=False),file=sys.stderr);return 2
    return 0


if __name__=='__main__':raise SystemExit(main())
