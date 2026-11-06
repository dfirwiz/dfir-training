"""Summarize fictional request times, not a C2 classifier or RITA implementation."""
from pathlib import Path
import csv,json,math,statistics,argparse

def inspect(path):
    rows=list(csv.DictReader(Path(path).open(encoding='utf-8',newline='')))
    unique={};duplicates=0
    for r in rows:
        if any(not r.get(k) for k in ['source','id','group','seconds']):raise ValueError('required fields')
        t=float(r['seconds'])
        if not math.isfinite(t) or t<0:raise ValueError('finite nonnegative time required')
        key=(r['source'],r['id'])
        if key in unique:
            if unique[key]!=r:raise ValueError('conflicting duplicate')
            duplicates+=1
        unique[key]=r
    groups=[]
    for group in sorted({r['group'] for r in unique.values()}):
        times=sorted(float(r['seconds']) for r in unique.values() if r['group']==group)
        gaps=[b-a for a,b in zip(times,times[1:])]
        groups.append(dict(group=group,events=len(times),gaps=gaps,mean_seconds=statistics.mean(gaps) if gaps else None,range_seconds=max(gaps)-min(gaps) if gaps else None,incident_verdict='unresolved'))
    return dict(raw_rows=len(rows),duplicate_rows=duplicates,unique_rows=len(unique),groups=groups,external_actions=0)
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('csv');a=p.parse_args()
    try:print(json.dumps(inspect(a.csv),indent=2))
    except (OSError,ValueError) as e:print('ERROR '+str(e));raise SystemExit(2)
