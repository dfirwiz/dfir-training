"""Compare fictional transport/protection claims; never contact a remoting endpoint."""
import argparse,json,ipaddress
from pathlib import Path
LAYERS={'wsman-http':['PSRP','WSMan/SOAP','HTTP','TCP'],'wsman-https':['PSRP','WSMan/SOAP','HTTPS/TLS','TCP'],'ssh':['PSRP','SSH','TCP']}
def compare(c):
    if not isinstance(c,dict) or not isinstance(c.get('id'),str):raise ValueError('case ID required')
    for name in ('source','destination'):
        if not isinstance(c.get(name),str):raise ValueError('address string required')
        ipaddress.ip_address(c[name])
    if type(c.get('port')) is not int or not 1<=c['port']<=65535:raise ValueError('port1-65535 required')
    transport=c['transport'];message=c['message_protection_claim'];auth=c['authentication_claim']
    if transport not in (*LAYERS,'unknown') or message not in ('encrypted','none','unknown') or not isinstance(auth,str) or not auth:raise ValueError('supported teaching claims required')
    for key in ('peer_identity_checked_in_fixture','trustedhosts_in_fixture','approved_in_fixture'):
        if type(c.get(key)) is not bool:raise ValueError('explicit boolean assumptions required')
    if auth=='basic' and message=='encrypted':raise ValueError('Basic alone does not provide message encryption')
    basis=[]
    if transport=='wsman-https':basis.append('TLS_transport_claim')
    elif transport=='ssh':basis.append('SSH_transport_claim')
    elif transport=='unknown':basis.append('unknown_transport')
    if message=='encrypted':basis.append('message_encryption_claim')
    elif message=='unknown':basis.append('message_protection_unknown')
    return dict(id=c['id'],layers_claim=LAYERS.get(transport),protection_basis_claim=basis,peer_identity_assumption=c['peer_identity_checked_in_fixture'],trustedhosts_assumption=c['trustedhosts_in_fixture'],approved_assumption=c['approved_in_fixture'],protocol_identified_from_port=False,actual_transport_verified=False,actual_encryption_verified=False,actual_peer_identity_verified=False,remote_execution_verified=False,second_hop_verified=False,incident_verdict='unresolved',external_actions=0)
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);a=p.parse_args()
    try:
        d=json.loads(a.input.read_text(encoding='utf-8'))
        if not isinstance(d,dict) or d.get('schema')!='training-remoting-claims-v1' or d.get('external_actions_allowed') is not False or not isinstance(d.get('cases'),list) or not d['cases']:raise ValueError('teaching contract required')
        print(json.dumps([compare(c) for c in d['cases']],indent=2));return 0
    except (OSError,ValueError,TypeError,KeyError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
