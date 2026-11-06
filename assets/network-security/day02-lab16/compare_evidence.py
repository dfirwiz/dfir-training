"""Compare supplied fictional evidence claims; neither parse Windows logs nor contact SMB."""
import argparse,json,datetime,ipaddress
from pathlib import Path
def time(v):
    if not isinstance(v,str):raise ValueError('timestamp string required')
    t=datetime.datetime.fromisoformat(v.replace('Z','+00:00'))
    if t.tzinfo is None:raise ValueError('timezone required')
    return t
def compare(case):
    if not isinstance(case,dict) or not isinstance(case.get('id'),str) or type(case.get('approved_in_fixture')) is not bool:raise ValueError('case/approval assumption required')
    flow=case['flow'];ipaddress.ip_address(flow['source']);ipaddress.ip_address(flow['destination'])
    if type(flow['destination_port']) is not int or not 1<=flow['destination_port']<=65535:raise ValueError('port range required')
    auth=case.get('auth');share=case.get('share');service=case.get('service');process=case.get('process');window=120
    for row in (auth,share,service,process):
        if row is not None and (not isinstance(row,dict) or not isinstance(row.get('target'),str) or not row['target']):raise ValueError('optional event claim object required')
        if row is not None:time(row['time'])
    for row in (auth,share,service):
        if row is not None and (not isinstance(row.get('logon_id'),str) or not row['logon_id']):raise ValueError('explicit target-scoped logon ID required')
    auth_ok=bool(auth and auth.get('event')==4624 and auth.get('logon_type')==3)
    def linked(row,event):
        return bool(auth_ok and row and row.get('event')==event and row['target']==auth['target'] and row.get('logon_id')==auth.get('logon_id') and 0<=(time(row['time'])-time(auth['time'])).total_seconds()<=window)
    share_ok=linked(share,5140);service_ok=linked(service,4697)
    process_candidate=bool(service_ok and process and process.get('event')==4688 and process['target']==service['target'] and isinstance(service.get('image'),str) and isinstance(process.get('image'),str) and service['image'].casefold()==process['image'].casefold() and 0<=(time(process['time'])-time(service['time'])).total_seconds()<=window)
    return dict(id=case['id'],destination_port_claim=flow['destination_port'],network_logon_claim=auth_ok,share_link_condition=share_ok,service_link_condition=service_ok,process_time_image_candidate=process_candidate,approved_assumption=case['approved_in_fixture'],actual_smb_protocol_verified=False,actual_windows_event_verified=False,causal_remote_execution_verified=False,credential_theft_verified=False,incident_verdict='unresolved',external_actions=0)
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);a=p.parse_args()
    try:
        d=json.loads(a.input.read_text(encoding='utf-8'))
        if not isinstance(d,dict) or d.get('schema')!='training-smb-evidence-claims-v1' or d.get('external_actions_allowed') is not False or not isinstance(d.get('cases'),list) or not d['cases']:raise ValueError('teaching contract required')
        print(json.dumps([compare(c) for c in d['cases']],indent=2));return 0
    except (OSError,ValueError,TypeError,KeyError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
