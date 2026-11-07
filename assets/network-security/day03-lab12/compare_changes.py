"""Compare own fictional snapshots and candidate record links, not live FIM."""
import json,hashlib,sys
from pathlib import Path
from datetime import datetime

def time(value):
    if not isinstance(value,str):raise ValueError('timestamp must be text')
    t=datetime.fromisoformat(value)
    if t.tzinfo is None or t.utcoffset() is None:raise ValueError('timezone required')
    return t

def compare(data,refs):
    if not isinstance(data,dict) or set(data)!={'collection_complete','before','after','configs','triggers','processes'}:raise ValueError('invalid fields')
    if type(data['collection_complete']) is not bool:raise ValueError('collection_complete must be bool')
    def snapshot(rows):
        if not isinstance(rows,list):raise ValueError('snapshot must be list')
        out={}
        for row in rows:
            if not isinstance(row,dict) or set(row)!={'path','content','owner','mode'}:raise ValueError('invalid snapshot fields')
            if any(not isinstance(v,str) or not v for v in row.values()):raise ValueError('snapshot values must be nonempty text')
            if row['content'] not in refs or row['path'] in out:raise ValueError('unknown reference or duplicate path')
            out[row['path']]=dict(sha256=refs[row['content']],owner=row['owner'],mode=row['mode'])
        return out
    before=snapshot(data['before']);after=snapshot(data['after'])
    changed=[dict(path=p,fields=[f for f in ('sha256','owner','mode') if before[p][f]!=after[p][f]]) for p in sorted(before.keys()&after.keys()) if before[p]!=after[p]]
    absent=sorted(before.keys()-after.keys());complete=data['collection_complete']
    def records(rows):
        if not isinstance(rows,list):raise ValueError('records must be list')
        seen=set()
        for row in rows:
            if not isinstance(row,dict) or set(row)!={'id','host','entry','path','time'}:raise ValueError('invalid record fields')
            if any(not isinstance(v,str) or not v for v in row.values()) or row['id'] in seen:raise ValueError('invalid or duplicate record id')
            seen.add(row['id']);time(row['time'])
        return rows
    configs=records(data['configs']);triggers=records(data['triggers']);processes=records(data['processes'])
    def identity(row):return row['host'],row['entry'],row['path']
    candidates=[]
    for cfg in configs:
        for trigger in triggers:
            if identity(cfg)!=identity(trigger) or time(cfg['time'])>time(trigger['time']):continue
            for proc in processes:
                if identity(trigger)==identity(proc) and time(trigger['time'])<=time(proc['time']):candidates.append(dict(config=cfg['id'],trigger=trigger['id'],process=proc['id']))
    return dict(changed=changed,added=sorted(after.keys()-before.keys()),missing_if_complete=absent if complete else [],unresolved_absence=[] if complete else absent,candidates=candidates,actual_fim=False,actual_autoruns=False,external_actions=0)

if __name__=='__main__':
    try:
        if len(sys.argv)!=4:raise ValueError('usage: python compare_changes.py cases.json reference-A.txt reference-B.txt')
        refs={k:hashlib.sha256(Path(p).read_bytes()).hexdigest() for k,p in zip(('A','B'),sys.argv[2:])}
        print(json.dumps(dict(reference_sha256=refs,results=compare(json.loads(Path(sys.argv[1]).read_text('utf-8')),refs)),ensure_ascii=False,indent=2))
    except (ValueError,OSError,TypeError) as exc:print(str(exc),file=sys.stderr);sys.exit(2)
