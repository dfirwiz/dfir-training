"""Compare fictional allowed-action claims. Never check or change OS permissions."""
from pathlib import Path
import argparse,json
ACTIONS={'read-user-data','write-user-data','read-service-data','change-machine-config','connect-internal','operate-other-host'}
def compare(d):
 if not isinstance(d,dict) or d.get('schema')!='training-endpoint-context-v1' or d.get('external_actions_allowed') is not False or not d.get('cases'):raise ValueError('teaching contract required')
 out=[]
 for c in d['cases']:
  if not isinstance(c['id'],str) or not isinstance(c['context_label'],str):raise ValueError('explicit labels required')
  if type(c['admin_group_claim']) is not bool:raise ValueError('group claim must be bool')
  allowed=c['allowed_actions_claim'];wanted=c['requested_actions']
  if allowed is not None and (not isinstance(allowed,list) or any(x not in ACTIONS for x in allowed) or len(set(allowed))!=len(allowed)):raise ValueError('supported unique action list or null required')
  if not isinstance(wanted,list) or not wanted or any(x not in ACTIONS for x in wanted):raise ValueError('explicit supported requested actions required')
  out.append(dict(id=c['id'],context_label=c['context_label'],admin_group_claim=c['admin_group_claim'],action_comparison={x:None if allowed is None else x in allowed for x in wanted},permissions_inferred_from_group_or_label=False,actual_os_permissions_verified=False,actual_token_verified=False,actual_access_or_exploitation_verified=False,actual_remote_authorization_verified=False,incident_verdict='unresolved',external_actions=0))
 return out
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);a=p.parse_args()
 try:print(json.dumps(compare(json.loads(a.input.read_text(encoding='utf-8'))),indent=2));return 0
 except (OSError,ValueError,TypeError,KeyError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
