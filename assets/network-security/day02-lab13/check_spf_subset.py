"""Evaluate only fictional ip4/ip6/all policy conditions; no DNS or real SPF verification."""
import argparse,json,ipaddress
from pathlib import Path

def evaluate(case):
    if not isinstance(case,dict) or not isinstance(case.get('id'),str):raise ValueError('case object and ID required')
    ip=ipaddress.ip_address(case['client_ip']);record=case['record']
    if case.get('identity_scope') not in ('mailfrom','helo'):raise ValueError('explicit identity scope required')
    if not isinstance(case.get('checked_domain'),str) or not case['checked_domain']:raise ValueError('checked domain claim required')
    trace=[];result='none';matched=None
    if record is not None:
        if not isinstance(record,str):raise ValueError('record string/null required')
        parts=record.split()
        if not parts or parts[0]!='v=spf1':raise ValueError('fixture version required')
        parsed=[]
        for token in parts[1:]:
            qualifier=token[0] if token and token[0] in '+-~?' else '+'
            mechanism=token[1:] if token and token[0] in '+-~?' else token
            if mechanism=='all':network=None
            elif mechanism.startswith(('ip4:','ip6:')):
                kind,value=mechanism.split(':',1);network=ipaddress.ip_network(value,strict=True)
                if network.version!=(4 if kind=='ip4' else 6):raise ValueError('address family mismatch')
            else:raise ValueError('unsupported teaching subset; not an SPF permerror verdict')
            parsed.append((token,qualifier,network))
        result='neutral'
        for token,qualifier,network in parsed:
            match=network is None or (ip.version==network.version and ip in network)
            trace.append(dict(term=token,matched=match))
            if match:result={'+':'pass','-':'fail','~':'softfail','?':'neutral'}[qualifier];matched=token;break
    return dict(id=case['id'],identity_scope=case['identity_scope'],checked_domain_claim=case['checked_domain'],subset_result=result,matched_term=matched,trace=trace,dns_queries=0,real_spf_verified=False,displayed_author_verified=False,incident_verdict='unresolved',external_actions=0)

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);a=p.parse_args()
    try:
        d=json.loads(a.input.read_text(encoding='utf-8'))
        if not isinstance(d,dict) or d.get('schema')!='training-spf-subset-v1' or d.get('external_actions_allowed') is not False or not isinstance(d.get('cases'),list) or not d['cases']:raise ValueError('training contract required')
        print(json.dumps([evaluate(c) for c in d['cases']],indent=2));return 0
    except (OSError,ValueError,TypeError,KeyError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
