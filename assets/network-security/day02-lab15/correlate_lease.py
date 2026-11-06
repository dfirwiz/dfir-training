"""Compare supplied fictional lease intervals; do not identify a real owner."""
import argparse,json,datetime,ipaddress
from pathlib import Path
def time(value):
    if not isinstance(value,str):raise ValueError('timestamp string required')
    t=datetime.datetime.fromisoformat(value.replace('Z','+00:00'))
    if t.tzinfo is None:raise ValueError('timezone required')
    return t
def compare(d):
    if not isinstance(d,dict) or d.get('schema')!='training-lease-interval-v1' or d.get('external_actions_allowed') is not False:raise ValueError('teaching contract required')
    if not isinstance(d.get('leases'),list) or not isinstance(d.get('queries'),list):raise ValueError('lists required')
    leases=[]
    for row in d['leases']:
        start,end=time(row['start']),time(row['end'])
        if end<=start:raise ValueError('positive lease interval required')
        if not isinstance(row.get('scope'),str) or not row['scope'] or not isinstance(row.get('client'),str):raise ValueError('scope/client required')
        leases.append((row,ipaddress.ip_address(row['ip']),start,end))
    result=[]
    for q in d['queries']:
        target=ipaddress.ip_address(q['ip']);t=time(q['time']);scope=q['scope']
        if not isinstance(scope,str) or not scope:raise ValueError('scope required')
        matches=[row['client'] for row,addr,start,end in leases if addr==target and row['scope']==scope and start<=t<end]
        result.append(dict(id=q['id'],candidates=matches,state='none_in_supplied_records' if not matches else ('one_candidate' if len(matches)==1 else 'ambiguous'),owner_verified=False,actual_lease_log_verified=False,incident_verdict='unresolved',external_actions=0))
    return result
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);a=p.parse_args()
    try:print(json.dumps(compare(json.loads(a.input.read_text(encoding='utf-8'))),indent=2));return 0
    except (OSError,ValueError,TypeError,KeyError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
