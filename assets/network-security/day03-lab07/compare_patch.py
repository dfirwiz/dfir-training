"""Compare fictional patch-completion claims only; no system queries or changes."""
import json,sys
from pathlib import Path

def tri_and(values):
    if False in values:return False
    return None if None in values else True

def flag(v):
    if v is not None and type(v) is not bool:raise ValueError('flag must be bool or null')
    return v

from datetime import datetime
from fractions import Fraction

def stamp(s):
    if s is None:return None
    if not isinstance(s,str):raise ValueError('timestamp string or null required')
    t=datetime.fromisoformat(s.replace('Z','+00:00'))
    if t.utcoffset() is None:raise ValueError('timezone required')
    return t

def compare(d):
    if d.get('schema')!='training-patch-claims-v1' or d.get('external_actions') is not False:raise ValueError('fictional contract required')
    now=stamp(d['as_of']);window=d['max_age_seconds']
    if now is None or type(window) is not int or window<=0:raise ValueError('time/window required')
    rows=[];ids=set()
    for x in d['assets']:
        if not isinstance(x['id'],str) or not x['id'] or x['id'] in ids:raise ValueError('unique nonempty id required')
        ids.add(x['id']);t=stamp(x['observed_at'])
        age=None if t is None else (now-t).total_seconds()
        fresh=None if age is None or age<0 else age<window
        facts=[flag(x[k]) for k in ('install_succeeded_claim','activation_verified_claim','post_check_passed_claim')]
        rows.append(dict(id=x['id'],age_seconds=age,fresh_claim=fresh,completion_gate=tri_and(facts+[fresh])))
    n=len(rows);passed=sum(x['completion_gate'] is True for x in rows)
    return dict(results=rows,declared_assets=n,gate_true=passed,gate_false=sum(x['completion_gate'] is False for x in rows),gate_unknown=sum(x['completion_gate'] is None for x in rows),confirmed_fraction=None if not n else str(Fraction(passed,n)),external_actions=0,actual_patch_installed=False,actual_device_verification=False,actual_vulnerability_status='unverified')

if __name__=='__main__':
    print(json.dumps(compare(json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))),ensure_ascii=False,indent=2))
