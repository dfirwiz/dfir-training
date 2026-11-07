"""Compare fictional connection and bounded scanner-schedule claims; no firewall engine."""
import json,sys
from pathlib import Path
from datetime import datetime

def stamp(s):
    if s is None:return None
    if not isinstance(s,str):raise ValueError('timestamp string or null required')
    t=datetime.fromisoformat(s.replace('Z','+00:00'))
    if t.utcoffset() is None:raise ValueError('timezone required')
    return t

def eq(a,b):return None if a is None or b is None else a==b

def all_claims(v):
    if False in v:return False
    return None if None in v else True

FIELDS=('source','destination','transport','destination_port','direction','profile')

def checked(row):
    for k in FIELDS:
        v=row[k]
        if k=='destination_port':
            if v is not None and (type(v) is not int or not 1<=v<=65535):raise ValueError('port int1..65535 or null required')
        elif v is not None and (not isinstance(v,str) or not v):raise ValueError('nonempty string or null required')
    if row['direction'] not in ('inbound','outbound',None):raise ValueError('invalid direction')
    if row['profile'] not in ('Domain','Private','Public',None):raise ValueError('invalid profile')

def compare(d):
    if d.get('schema')!='training-connection-schedule-v1' or d.get('external_actions') is not False:raise ValueError('fictional contract required')
    schedule=d['schedule'];checked(schedule);start=stamp(schedule['start']);end=stamp(schedule['end'])
    if start is None or end is None or start>=end:raise ValueError('ordered window required')
    out=[];ids=set()
    for x in d['connections']:
        if not isinstance(x['id'],str) or not x['id'] or x['id'] in ids:raise ValueError('unique nonempty id required')
        ids.add(x['id']);checked(x);t=stamp(x['time'])
        in_time=None if t is None else start<=t<end
        match=all_claims([eq(x[k],schedule[k]) for k in FIELDS]+[in_time])
        action=x['action_claim']
        if action not in ('allow','block','unknown'):raise ValueError('invalid action')
        out.append(dict(id=x['id'],in_window=in_time,schedule_match=match,block_claim=True if action=='block' else False if action=='allow' else None))
    return dict(results=out,external_actions=0,actual_firewall_policy_read=False,actual_connection_test=False,actual_block_verified=False,actual_scanner_authorization='unverified',incident_conclusion='unresolved')

if __name__=='__main__':
    print(json.dumps(compare(json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))),ensure_ascii=False,indent=2))
