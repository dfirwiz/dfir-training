"""Describe routes in fictional SSH forwarding metadata; create no connection or listener."""
import argparse,json,ipaddress
from pathlib import Path
def address(v):
    if not isinstance(v,str):raise ValueError('IPv4 string required')
    return str(ipaddress.IPv4Address(v))
def port(v):
    if type(v) is not int or not 1<=v<=65535:raise ValueError('port1-65535 required')
    return v
def compare(c):
    if not isinstance(c,dict) or not isinstance(c.get('id'),str):raise ValueError('case ID required')
    client=address(c['ssh_client']);server=address(c['ssh_server']);server_port=port(c['ssh_port'])
    mode=c['mode']
    if mode not in ('local','remote','unknown'):raise ValueError('local/remote/unknown teaching mode required')
    for k in ('approved_in_fixture','forwarding_permitted_in_fixture','target_reachable_in_fixture'):
        if type(c.get(k)) is not bool:raise ValueError('explicit boolean assumptions required')
    out=dict(id=c['id'],physical_ssh_connection_claim=f'{client} -> {server}:{server_port}',mode_claim=mode,entry_host_role=None,target_connecting_role=None,listener_scope=None,loopback_target_host=None,modeled_path_available=None,approved_assumption=c['approved_in_fixture'],actual_ssh_verified=False,actual_forwarding_verified=False,public_exposure='unverified',incident_verdict='unresolved',external_actions=0)
    if mode=='unknown':return out
    bind=ipaddress.IPv4Address(address(c['bind']));listen_port=port(c['listen_port']);target=ipaddress.IPv4Address(address(c['target']));target_port=port(c['target_port'])
    entry='ssh_client' if mode=='local' else 'ssh_server';connector='ssh_server' if mode=='local' else 'ssh_client'
    out.update(entry_host_role=entry,target_connecting_role=connector,listener_scope='loopback' if bind.is_loopback else ('all_ipv4_interfaces' if bind.is_unspecified else 'specified_ipv4_interface'),listener_claim=f'{bind}:{listen_port}',target_claim=f'{target}:{target_port}',loopback_target_host=connector if target.is_loopback else None,modeled_path_available=c['forwarding_permitted_in_fixture'] and c['target_reachable_in_fixture'])
    return out
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);a=p.parse_args()
    try:
        d=json.loads(a.input.read_text(encoding='utf-8'))
        if not isinstance(d,dict) or d.get('schema')!='training-ssh-route-v1' or d.get('external_actions_allowed') is not False or not isinstance(d.get('cases'),list) or not d['cases']:raise ValueError('teaching contract required')
        print(json.dumps([compare(c) for c in d['cases']],indent=2));return 0
    except (OSError,ValueError,KeyError,TypeError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
