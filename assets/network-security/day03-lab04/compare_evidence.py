"""Compare fictional credential investigation record kinds, never collect secrets."""
from pathlib import Path
import argparse,json
KINDS=('process_access','material_report','authentication_accept','session_record','action_result')
MATERIALS=('none','unknown','plaintext','nt_hash','tgt','service_ticket','cached_logon_verifier')

def tri_all(values):
 if any(x is False for x in values):return False
 if any(x is None for x in values):return None
 return True

def compare(d):
 if not isinstance(d,dict) or d.get('schema')!='training-credential-evidence-v1' or d.get('external_actions_allowed') is not False or not d.get('cases'):raise ValueError('teaching contract required')
 out=[]
 for c in d['cases']:
  kinds=c['evidence_kinds'];m=c['material_type_claim']
  if not isinstance(kinds,list) or any(k not in KINDS for k in kinds) or len(set(kinds))!=len(kinds) or m not in MATERIALS:raise ValueError('supported unique kinds and material label required')
  gates={k:c[k] for k in ('same_account_link_claim','same_target_link_claim','time_order_link_claim')}
  if any(x is not None and type(x) is not bool for x in gates.values()):raise ValueError('links must be bool or null')
  missing=[k for k in KINDS if k not in kinds];complete=not missing
  out.append(dict(id=c['id'],material_type_claim=m,present_record_kinds=kinds,missing_record_kinds=missing,evidence_complete_for_teaching_chain=complete,link_claims=gates,candidate_link_under_claims=tri_all([complete,*gates.values()]),remote_reusability_inferred_from_material_label=False,actual_credential_extraction_verified=False,actual_material_reuse_verified=False,actual_authentication_or_action_verified=False,actual_causality_or_attacker_intent_verified=False,incident_verdict='unresolved',external_actions=0))
 return out

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);a=p.parse_args()
 try:print(json.dumps(compare(json.loads(a.input.read_text(encoding='utf-8'))),indent=2));return 0
 except (OSError,ValueError,TypeError,KeyError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
