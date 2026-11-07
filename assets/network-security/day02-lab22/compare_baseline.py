"""Compare fictional remote-access claims with a supplied rule; no real authorization."""
from pathlib import Path
import json,datetime,argparse,ipaddress
def evaluate(d):
 if d.get('schema')!='training-remote-baseline-v1' or d.get('external_actions_allowed') is not False or not isinstance(d.get('cases'),list) or not d['cases']:raise ValueError('teaching contract required')
 r=d['rule'];start=datetime.datetime.fromisoformat(r['start']);end=datetime.datetime.fromisoformat(r['end'])
 if start.utcoffset() is None or end.utcoffset() is None or start>=end:raise ValueError('timezone-aware ordered rule required')
 network=ipaddress.ip_network(r['source_network']);dest=ipaddress.ip_address(r['destination']);out=[]
 for c in d['cases']:
  src=ipaddress.ip_address(c['source']);dst=ipaddress.ip_address(c['destination']);t=datetime.datetime.fromisoformat(c['time'])
  if t.utcoffset() is None:raise ValueError('timezone-aware time required')
  if type(c['port']) is not int or not 1<=c['port']<=65535:raise ValueError('port1-65535 required')
  for key in ('tool','tenant','user'):
   if c[key] is not None and (not isinstance(c[key],str) or not c[key]):raise ValueError('explicit nonempty claim or null required')
  if c['ticket_linked_claim'] is not None and type(c['ticket_linked_claim']) is not bool:raise ValueError('explicit bool or null ticket claim required')
  reasons=[];unknown=[]
  if src not in network:reasons.append('source_outside_rule')
  if dst!=dest:reasons.append('destination_outside_rule')
  if not start<=t<end:reasons.append('time_outside_rule')
  for key in ('tool','tenant','user'):
   if c[key] is None:unknown.append(key)
   elif c[key]!=r[key]:reasons.append(key+'_outside_rule')
  if c['ticket_linked_claim'] is None:unknown.append('ticket')
  elif not c['ticket_linked_claim']:reasons.append('ticket_not_linked')
  state='deviation' if reasons else 'insufficient_evidence' if unknown else 'matches_supplied_rule'
  out.append(dict(id=c['id'],rule_comparison=state,reasons=reasons,unknown=unknown,port_used_to_identify_tool=False,actual_product_verified=False,actual_tenant_verified=False,actual_user_verified=False,actual_approval_verified=False,actual_remote_execution_verified=False,incident_verdict='unresolved',external_actions=0))
 return out
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);a=p.parse_args()
 try:print(json.dumps(evaluate(json.loads(a.input.read_text(encoding='utf-8'))),indent=2));return 0
 except (OSError,ValueError,TypeError,KeyError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
