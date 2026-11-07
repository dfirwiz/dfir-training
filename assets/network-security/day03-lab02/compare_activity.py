"""Compare fictional execution/startup/discovery claims without executing commands."""
from pathlib import Path
import argparse,json,datetime
def stamp(s):
 t=datetime.datetime.fromisoformat(s)
 if t.utcoffset() is None:raise ValueError('timezone-aware record time required')
 return t
def compare(d):
 if not isinstance(d,dict) or d.get('schema')!='training-endpoint-activity-v1' or d.get('external_actions_allowed') is not False or not d.get('cases'):raise ValueError('teaching contract required')
 out=[]
 for c in d['cases']:
  rows=c['records'];times=[stamp(x['time']) for x in rows]
  if times!=sorted(times):raise ValueError('chronological teaching records required')
  if len({x['id'] for x in rows})!=len(rows):raise ValueError('unique record IDs required')
  for x in rows:
   if x['kind'] not in ('process_start','startup_config','trigger_event','discovery_command'):raise ValueError('supported teaching record kinds required')
   if not all(isinstance(x[k],str) and x[k] for k in ('host','subject')):raise ValueError('host/subject labels required')
  configs=[x for x in rows if x['kind']=='startup_config'];triggers=[x for x in rows if x['kind']=='trigger_event'];processes=[x for x in rows if x['kind']=='process_start'];linked=[]
  for cfg in configs:
   for trigger in triggers:
    if cfg['host']!=trigger['host'] or cfg['subject']!=trigger['subject'] or stamp(trigger['time'])<stamp(cfg['time']):continue
    for proc in processes:
     if proc['host']==cfg['host'] and proc['subject']==cfg['subject'] and stamp(proc['time'])>=stamp(trigger['time']):linked.append([cfg['id'],trigger['id'],proc['id']])
  out.append(dict(id=c['id'],process_start_record_ids=[x['id'] for x in processes],startup_config_record_ids=[x['id'] for x in configs],trigger_record_ids=[x['id'] for x in triggers],candidate_config_trigger_process_links=linked,discovery_record_ids=[x['id'] for x in rows if x['kind']=='discovery_command'],actual_process_or_command_verified=False,actual_persistence_verified=False,actual_causality_verified=False,actual_attacker_intent_verified=False,incident_verdict='unresolved',external_actions=0))
 return out
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);a=p.parse_args()
 try:print(json.dumps(compare(json.loads(a.input.read_text(encoding='utf-8'))),indent=2));return 0
 except (OSError,ValueError,TypeError,KeyError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
