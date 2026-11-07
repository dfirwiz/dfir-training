"""Compare fictional egress allow-rule claims and captured-byte rates, no networking."""
from pathlib import Path
from fractions import Fraction
import argparse,json
FIELDS=('source_role','destination','transport','destination_port','application_claim')

def tri_all(v):
 if any(x is False for x in v):return False
 if any(x is None for x in v):return None
 return True

def valid(row,unknown):
 for k in FIELDS:
  x=row[k]
  if x is None and unknown:continue
  if k=='destination_port':
   if type(x) is not int or not 1<=x<=65535:raise ValueError('port integer1..65535 required')
  elif not isinstance(x,str) or not x:raise ValueError('nonempty labels or declared unknown required')

def compare(d):
 if not isinstance(d,dict) or d.get('schema')!='training-egress-claims-v1' or d.get('external_actions_allowed') is not False or d.get('default_action_claim')!='deny' or d.get('accounting_scope')!='fictional-captured-layer-count':raise ValueError('teaching contract required')
 for rule in d['allow_rules']:valid(rule,False)
 out=[]
 for c in d['cases']:
  valid(c,True);b=c['observed_bytes'];t=c['interval_seconds']
  if b is not None and (type(b) is not int or b<0):raise ValueError('nonnegative byte count or null required')
  if type(t) is not int or t<=0:raise ValueError('positive integer seconds required')
  matches=[tri_all([None if c[k] is None else c[k]==rule[k] for k in FIELDS]) for rule in d['allow_rules']]
  decision='allow_rule_match' if True in matches else 'unverified' if None in matches else 'no_rule_match'
  out.append(dict(id=c['id'],rule_comparisons=matches,policy_match_under_claims=decision,observed_bytes_per_second=None if b is None else str(Fraction(b,t)),observed_bits_per_second=None if b is None else str(Fraction(8*b,t)),actual_firewall_action_verified=False,actual_protocol_or_content_verified=False,actual_file_or_exfiltration_verified=False,incident_verdict='unresolved',external_actions=0))
 return out

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);a=p.parse_args()
 try:print(json.dumps(compare(json.loads(a.input.read_text(encoding='utf-8'))),indent=2));return 0
 except (OSError,ValueError,TypeError,KeyError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
