"""Compare fictional RDP session claims, not EVTX, network traffic or user activity."""
import argparse,json,datetime,ipaddress
from pathlib import Path
def time(v):
    if not isinstance(v,str):raise ValueError('timestamp string required')
    t=datetime.datetime.fromisoformat(v.replace('Z','+00:00'))
    if t.tzinfo is None:raise ValueError('timezone required')
    return t
def text(v):
    if not isinstance(v,str) or not v:raise ValueError('nonempty identifier required')
    return v
def address(v):
    if not isinstance(v,str):raise ValueError('IP address string required')
    return ipaddress.ip_address(v)
def compare(c):
    if not isinstance(c,dict) or not isinstance(c.get('id'),str) or type(c.get('approved_in_fixture')) is not bool:raise ValueError('case/approval assumption required')
    flow=c['flow'];address(flow['source']);address(flow['destination'])
    if type(flow.get('destination_port')) is not int or not 1<=flow['destination_port']<=65535:raise ValueError('valid port required')
    auth=c.get('auth');events=c['transitions']
    if not isinstance(events,list):raise ValueError('transition list required')
    if auth is not None:
        if not isinstance(auth,dict):raise ValueError('optional auth object required')
        for k in ('target','logon_id','user','session_name'):text(auth[k])
        start=time(auth['time']);source=address(auth['source'])
    else:start=None;source=None
    eligible=bool(auth and auth.get('event')==4624 and auth.get('logon_type')==10 and auth.get('session_kind')=='rdp')
    linked=[];ignored=0;prior=start;last_disconnect=None;gaps=[]
    for e in events:
        if not isinstance(e,dict) or e.get('event') not in (4778,4779):raise ValueError('4778/4779 teaching transitions required')
        t=time(e['time'])
        for k in ('target','logon_id','user','session_name'):text(e[k])
        matches=eligible and e.get('session_kind')=='rdp' and all(e[k]==auth[k] for k in ('target','logon_id','user','session_name'))
        if not matches:ignored+=1;continue
        if t<prior:raise ValueError('matched transitions must be chronological and after supplied logon')
        if linked and linked[-1]['event']==e['event']:raise ValueError('repeated identical transitions outside teaching subset')
        prior=t;state='disconnected_claim' if e['event']==4779 else 'reconnected_claim'
        linked.append(dict(event=e['event'],state=state,offset_seconds=(t-start).total_seconds()))
        if e['event']==4779:last_disconnect=t
        elif last_disconnect is not None:gaps.append((t-last_disconnect).total_seconds());last_disconnect=None
    return dict(id=c['id'],remote_interactive_logon_claim=eligible,linked_transition_claims=linked,unmatched_transitions=ignored,disconnect_to_reconnect_seconds=gaps,last_transition_claim=linked[-1]['state'] if linked else None,loopback_source_claim=source.is_loopback if source is not None else None,approved_assumption=c['approved_in_fixture'],actual_rdp_verified=False,actual_windows_event_verified=False,operator_identity='unverified',hands_on_activity='unverified',current_session_status='unverified',incident_verdict='unresolved',external_actions=0)
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);a=p.parse_args()
    try:
        d=json.loads(a.input.read_text(encoding='utf-8'))
        if not isinstance(d,dict) or d.get('schema')!='training-rdp-session-v1' or d.get('external_actions_allowed') is not False or not isinstance(d.get('cases'),list) or not d['cases']:raise ValueError('teaching contract required')
        print(json.dumps([compare(c) for c in d['cases']],indent=2));return 0
    except (OSError,ValueError,KeyError,TypeError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
