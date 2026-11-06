"""Read fictional logs and query an in-memory SQLite database. Not a SIEM or incident verdict."""
import argparse
from datetime import datetime,timezone
import json
from pathlib import Path
import sqlite3

QUERY="""SELECT source, realm, user, src_ip, COUNT(*) AS failures
FROM observations
WHERE kind = 'auth' AND outcome = 'failure'
  AND realm <> '' AND user <> '' AND src_ip <> ''
  AND selected_time >= ? AND selected_time < ?
GROUP BY source, realm, user, src_ip
HAVING COUNT(*) >= ?
ORDER BY source, realm, user, src_ip"""

def instant(s):
 if not isinstance(s,str):raise ValueError('time string required')
 t=datetime.fromisoformat(s.replace('Z','+00:00'))
 if t.tzinfo is None or t.utcoffset() is None:raise ValueError('timezone required')
 return t.astimezone(timezone.utc).timestamp()

def review(rows,policy,as_of=None,time_field='event_time',threshold=None):
 if not isinstance(policy,dict) or policy.get('schema')!='training-investigation-v1' or policy.get('external_actions_allowed') is not False:raise ValueError('training policy with external actions false required')
 start,end=instant(policy['start']),instant(policy['end']);cutoff=instant(as_of or policy['as_of'])
 if start>=end:raise ValueError('start must precede end')
 if time_field not in ('event_time','received'):raise ValueError('unknown time field')
 limit=policy['threshold'] if threshold is None else threshold
 if type(limit) is not int or limit<1:raise ValueError('positive integer threshold required')
 if not isinstance(rows,list) or not rows:raise ValueError('non-empty records required')
 unique={};duplicates=0;raw_available=0
 for row in rows:
  if not isinstance(row,dict):raise ValueError('object record required')
  for k in ('source','id','kind','event_time','received','user','realm','src_ip','outcome','detail'):
   if not isinstance(row.get(k),str):raise ValueError('required string fields')
  if any(not row[k] for k in ('source','id','kind')):raise ValueError('non-empty source/id/kind required')
  event,received=instant(row['event_time']),instant(row['received'])
  if row['kind']=='auth' and row['outcome'] not in ('failure','success'):raise ValueError('auth outcome required')
  key=(row['source'],row['id'])
  raw_available+=received<=cutoff
  if key in unique:
   if row!=unique[key][0]:raise ValueError('conflicting duplicate')
   duplicates+=1;continue
  unique[key]=(row,event,received)
 available=[x for x in unique.values() if x[2]<=cutoff]
 selected=[x for x in available if start<=(x[1] if time_field=='event_time' else x[2])<end]
 missing=sum(x[0]['kind']=='auth' and any(not x[0][k] for k in ('realm','user','src_ip')) for x in selected)
 with sqlite3.connect(':memory:') as con:
  con.row_factory=sqlite3.Row
  con.execute('CREATE TABLE observations(source TEXT,id TEXT,kind TEXT,realm TEXT,user TEXT,src_ip TEXT,outcome TEXT,selected_time REAL)')
  con.executemany('INSERT INTO observations VALUES(?,?,?,?,?,?,?,?)',[(x[0]['source'],x[0]['id'],x[0]['kind'],x[0]['realm'],x[0]['user'],x[0]['src_ip'],x[0]['outcome'],x[1] if time_field=='event_time' else x[2]) for x in available])
  candidates=[]
  for group in con.execute(QUERY,(start,end,limit)).fetchall():
   item=dict(group);identity=tuple(item[k] for k in ('source','realm','user','src_ip'))
   matched=[x[0]['id'] for x in selected if tuple(x[0][k] for k in ('source','realm','user','src_ip'))==identity and x[0]['kind']=='auth' and x[0]['outcome']=='failure']
   item['matched_event_ids']=sorted(matched)
   item['success_records_same_group']=sum(x[0]['kind']=='auth' and x[0]['outcome']=='success' and tuple(x[0][k] for k in ('source','realm','user','src_ip'))==identity for x in selected)
   candidates.append(item)
 return dict(status='training_review_only',python_sqlite_version=sqlite3.sqlite_version,raw_rows=len(rows),raw_available=raw_available,duplicate_rows=duplicates,unique_available=len(available),selected_rows=len(selected),missing_identity_auth_rows=missing,time_field=time_field,threshold=limit,candidates=candidates,incident_verdict='unresolved',cross_source_session_links='not_established',external_actions=0)

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('events',type=Path);p.add_argument('policy',type=Path);p.add_argument('--as-of');p.add_argument('--time-field',choices=['event_time','received'],default='event_time');p.add_argument('--threshold',type=int);a=p.parse_args()
 try:
  rows=[json.loads(s) for s in a.events.read_text(encoding='utf-8').splitlines() if s.strip()]
  print(json.dumps(review(rows,json.loads(a.policy.read_text(encoding='utf-8')),a.as_of,a.time_field,a.threshold),indent=2));return 0
 except (OSError,ValueError,TypeError,KeyError,OverflowError,sqlite3.Error) as exc:
  print('ERROR '+str(exc));return 2

if __name__=='__main__':raise SystemExit(main())
