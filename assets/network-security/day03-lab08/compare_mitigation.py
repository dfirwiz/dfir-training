"""Resolve a fictional inherited setting and compare separate runtime/action claims."""
import json,sys
from pathlib import Path

def tri_and(values):
    if False in values:return False
    return None if None in values else True

def flag(v):
    if v is not None and type(v) is not bool:raise ValueError('flag must be bool or null')
    return v

def compare(d):
    if d.get('schema')!='training-mitigation-claims-v1' or d.get('external_actions') is not False:raise ValueError('fictional contract required')
    rows=[];ids=set()
    for x in d['cases']:
        if not isinstance(x['id'],str) or not x['id'] or x['id'] in ids:raise ValueError('unique nonempty id required')
        ids.add(x['id'])
        if x['default_state'] not in ('on','off'):raise ValueError('known default required')
        for k in ('system_state','app_state'):
            if x[k] not in ('on','off','notset','unknown'):raise ValueError('invalid state')
        state=x['app_state'];origin='app'
        if state=='notset':state=x['system_state'];origin='system'
        if state=='notset':state=x['default_state'];origin='default'
        selected=None if state=='unknown' else state=='on'
        action=x['observed_action_claim']
        if action not in ('blocked','audited','none','unknown'):raise ValueError('invalid action')
        action_block=True if action=='blocked' else False if action=='audited' else None
        candidate=tri_and([selected,flag(x['supported_claim']),flag(x['running_claim'])])
        rows.append(dict(id=x['id'],resolved_state=state,selected_from=origin,coverage_candidate=candidate,record_claims_block=action_block))
    return dict(results=rows,external_actions=0,actual_policy_read=False,actual_control_running=False,actual_exploit_blocked=False,incident_conclusion='unresolved')

if __name__=='__main__':
    print(json.dumps(compare(json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))),ensure_ascii=False,indent=2))
