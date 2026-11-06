"""Inspect fictional DKIM tag claims and strict domain alignment from supplied outcomes."""
import argparse,json,re
from pathlib import Path
RESULTS={'pass','fail','none','neutral','softfail','temperror','permerror'}

def domain(value):
    if not isinstance(value,str) or len(value)>253:raise ValueError('ASCII domain required')
    value=value.lower().removesuffix('.')
    if '.' not in value or any(not re.fullmatch(r'[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?',label) for label in value.split('.')):raise ValueError('simplified ASCII domain required')
    return value

def compare(case):
    if not isinstance(case,dict) or type(case.get('results_trusted_in_fixture')) is not bool:raise ValueError('explicit fixture trust assumption required')
    author=domain(case['author_domain']);spf=case['spf'];signatures=case['dkim']
    if not isinstance(spf,dict) or spf.get('result') not in RESULTS or not isinstance(signatures,list):raise ValueError('supplied outcome structure required')
    spf_domain=domain(spf['domain']) if spf.get('domain') is not None else None
    if spf['result']=='pass' and spf_domain is None:raise ValueError('passing SPF needs its supplied domain')
    spf_ok=spf['result']=='pass' and spf_domain==author
    rows=[]
    for sig in signatures:
        if not isinstance(sig,dict) or sig.get('result') not in RESULTS:raise ValueError('supplied signature outcome required')
        signing=domain(sig['domain']);rows.append(dict(signing_domain=signing,supplied_result=sig['result'],strictly_aligned=signing==author,contributes=sig['result']=='pass' and signing==author))
    trusted=case['results_trusted_in_fixture'];ok=spf_ok or any(x['contributes'] for x in rows)
    return dict(id=case['id'],author_domain=author,spf_contributes=spf_ok,dkim_conditions=rows,strict_condition_result=('pass' if ok else 'fail') if trusted else 'unverified',fixture_trust_assumption=trusted,real_authentication_verified=False,policy_discovery_performed=False,receiver_action='not_computed',content_safety='unresolved',incident_verdict='unresolved',external_actions=0)

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);a=p.parse_args()
    try:
        d=json.loads(a.input.read_text(encoding='utf-8'))
        if not isinstance(d,dict) or d.get('schema')!='training-auth-alignment-v1' or d.get('external_actions_allowed') is not False or d.get('alignment_mode')!='strict' or not isinstance(d.get('cases'),list) or not d['cases']:raise ValueError('strict teaching contract required')
        tags=d['signature_field_claims'];signing=domain(tags['d']);selector=domain(tags['s']+'.selector.example').removesuffix('.selector.example')
        if not isinstance(tags.get('h'),list) or any(not isinstance(v,str) for v in tags['h']):raise ValueError('claimed header names required')
        metadata=dict(public_key_name_claim=selector+'._domainkey.'+signing,header_names_claim=tags['h'],cryptographic_signature_verified=False,dns_queries=0)
        print(json.dumps(dict(signature_metadata=metadata,cases=[compare(c) for c in d['cases']]),indent=2));return 0
    except (OSError,ValueError,TypeError,KeyError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
