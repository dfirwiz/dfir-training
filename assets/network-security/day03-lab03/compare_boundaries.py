"""Compare fictional privilege-path claims and integer intervals, never OS state."""
from pathlib import Path
import argparse,json

def tri_all(values):
 if any(x is False for x in values):return False
 if any(x is None for x in values):return None
 return True

def tri(x):
 if x is not None and type(x) is not bool:raise ValueError('bool or null required')
 return x

def number(x,positive=False):
 if type(x) is not int or x<(1 if positive else 0):raise ValueError('nonnegative integer / positive size required')
 return x

def compare(d):
 if not isinstance(d,dict) or d.get('schema')!='training-boundary-claims-v1' or d.get('external_actions_allowed') is not False:raise ValueError('teaching contract required')
 paths=[];ranges=[]
 for c in d['paths']:
  gates={k:tri(c[k]) for k in ('writable_input_claim','privileged_consumer_claim','activation_link_claim')}
  paths.append(dict(id=c['id'],gate_claims=gates,candidate_path_under_claims=tri_all(list(gates.values())),actual_privilege_escalation_verified=False,actual_os_permissions_verified=False,incident_verdict='unresolved',external_actions=0))
 for c in d['ranges']:
  page=number(c['page_bytes'],True);offset=number(c['offset_bytes']);length=number(c['length_bytes'],True);size=number(c['file_bytes']);read=tri(c['read_permission_claim'])
  end=offset+length;next_page=(offset//page+1)*page
  gates=dict(read_permission_claim=read,start_not_on_boundary=offset%page!=0,within_same_page=end<=next_page,within_declared_file=end<=size)
  ranges.append(dict(id=c['id'],end_exclusive_bytes=end,next_boundary_bytes=next_page,condition_comparison=gates,range_conditions_match=tri_all(list(gates.values())),actual_kernel_or_vulnerability_verified=False,actual_file_access_or_write_verified=False,incident_verdict='unresolved',external_actions=0))
 return dict(paths=paths,ranges=ranges,model='claim-and-integer-comparison-only')

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);a=p.parse_args()
 try:print(json.dumps(compare(json.loads(a.input.read_text(encoding='utf-8'))),indent=2));return 0
 except (OSError,ValueError,TypeError,KeyError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
