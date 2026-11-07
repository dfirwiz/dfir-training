"""Compare fictional authentication/read/copy claims to an owned reference file."""
from pathlib import Path
import argparse,json,hashlib,re

def tri_all(values):
 if any(x is False for x in values):return False
 if any(x is None for x in values):return None
 return True

def flag(x):
 if x is not None and type(x) is not bool:raise ValueError('bool or null required')
 return x

def equal(a,b):return None if a is None or b is None else a==b

def labels(row,keys):
 for k in keys:
  if row[k] is not None and (not isinstance(row[k],str) or not row[k]):raise ValueError('label or null required')

def compare(d,reference):
 if not isinstance(d,dict) or d.get('schema')!='training-movement-claims-v1' or d.get('external_actions_allowed') is not False or not d.get('cases'):raise ValueError('teaching contract required')
 digest=hashlib.sha256(reference).hexdigest();out=[]
 for c in d['cases']:
  labels(c,('origin_host',));connection=flag(c['connection_claim']);auth=c['authentication_claim'];read=c['read_claim'];cp=c['local_copy_claim'];missing=[k for k in ('authentication_claim','read_claim','local_copy_claim') if c[k] is None]
  if auth is not None:labels(auth,('account','target'));flag(auth['accepted'])
  if read is not None:labels(read,('account','target','object_id'));flag(read['success'])
  if cp is not None:
   labels(cp,('host','source_account','source_target','source_object_id'))
   if cp['sha256_claim'] is not None and (not isinstance(cp['sha256_claim'],str) or not re.fullmatch('[0-9a-f]{64}',cp['sha256_claim'])):raise ValueError('lowercase SHA256 claim or null required')
   if cp['bytes_claim'] is not None and (type(cp['bytes_claim']) is not int or cp['bytes_claim']<0):raise ValueError('nonnegative byte count or null required')
  ar=False if auth is None or read is None else tri_all([auth['accepted'],read['success'],equal(auth['account'],read['account']),equal(auth['target'],read['target'])])
  rc=False if read is None or cp is None else tri_all([read['success'],equal(c['origin_host'],cp['host']),equal(read['account'],cp['source_account']),equal(read['target'],cp['source_target']),equal(read['object_id'],cp['source_object_id'])])
  bytecmp=False if cp is None else tri_all([equal(cp['sha256_claim'],digest),equal(cp['bytes_claim'],len(reference))])
  out.append(dict(id=c['id'],missing_claim_records=missing,authentication_read_link_under_claims=ar,read_copy_link_under_claims=rc,copy_claim_matches_owned_reference=bytecmp,candidate_chain_under_claims=tri_all([connection,ar,rc,bytecmp]),actual_network_or_remote_authentication_verified=False,actual_remote_read_or_copy_verified=False,actual_remote_execution_verified=False,actual_causality_or_authorization_verified=False,incident_verdict='unresolved',external_actions=0))
 return dict(owned_reference_bytes=len(reference),owned_reference_sha256=digest,cases=out)

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);p.add_argument('reference',type=Path);a=p.parse_args()
 try:print(json.dumps(compare(json.loads(a.input.read_text(encoding='utf-8')),a.reference.read_bytes()),indent=2));return 0
 except (OSError,ValueError,TypeError,KeyError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
