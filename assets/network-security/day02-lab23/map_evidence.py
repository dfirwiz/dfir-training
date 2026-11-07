"""Compare supplied fictional evidence records with stage questions, offline."""
from pathlib import Path
import argparse,json,datetime
def time(s):
 t=datetime.datetime.fromisoformat(s)
 if t.utcoffset() is None:raise ValueError('timezone required')
 return t
def evaluate(d):
 if d.get('schema')!='training-visibility-v1' or d.get('external_actions_allowed') is not False:raise ValueError('teaching contract required')
 sensors=d['sensors'];stages=d['stages'];records=d['records']
 if not stages or len({s['id'] for s in stages})!=len(stages):raise ValueError('unique nonempty stages required')
 for s in sensors.values():
  if time(s['start'])>=time(s['end']):raise ValueError('sensor window ordered')
 accepted=[];ignored=[]
 for row in records:
  s=sensors[row['sensor']];t=time(row['time'])
  if time(s['start'])<=t<time(s['end']) and row['path']==s['path'] and row['kind'] in s['kinds']:accepted.append(row)
  else:ignored.append(row['id'])
 results=[]
 for stage in stages:
  if not stage['required'] or time(stage['start'])>=time(stage['end']):raise ValueError('stage requirements/window required')
  rows=[x for x in accepted if x['path']==stage['path'] and time(stage['start'])<=time(x['time'])<time(stage['end'])]
  found=sorted({x['kind'] for x in rows}&set(stage['required']));missing=sorted(set(stage['required'])-set(found))
  results.append(dict(id=stage['id'],record_ids=[x['id'] for x in rows],required_found=found,required_missing=missing,supplied_evidence_complete=not missing,actual_stage_verified=False,incident_verdict='unresolved'))
 return dict(stages=results,ignored_record_ids=ignored,actual_sensor_or_records_verified=False,external_actions=0)
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);a=p.parse_args()
 try:print(json.dumps(evaluate(json.loads(a.input.read_text(encoding='utf-8'))),indent=2));return 0
 except (OSError,ValueError,KeyError,TypeError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
