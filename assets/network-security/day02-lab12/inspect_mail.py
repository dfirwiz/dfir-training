"""Read a simplified fictional email trace and an explicit analyst assumption."""
import argparse,json,re,hashlib,ipaddress
from pathlib import Path
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
from datetime import timezone

def inspect(raw,assumption):
    if not isinstance(assumption,dict) or assumption.get('schema')!='training-mail-trace-v1' or assumption.get('external_actions_allowed') is not False:raise ValueError('training contract required')
    msg=BytesParser(policy=policy.default).parsebytes(raw)
    for name in ('From','To','Date','Message-ID','Subject'):
        if len(msg.get_all(name,[]))!=1:raise ValueError('one fixture '+name+' field required')
    values=msg.get_all('Received',[])
    if not values:raise ValueError('Received fields required')
    rows=[]
    for i,value in enumerate(values):
        text=str(value);prefix,sep,date=text.rpartition(';')
        if not sep:raise ValueError('fixture Received date separator required')
        t=parsedate_to_datetime(date.strip())
        if t is None or t.tzinfo is None:raise ValueError('Received timezone required')
        by=re.search(r'\bby\s+([A-Za-z0-9.-]+)\b',prefix,re.I)
        peer=re.search(r'\[([0-9.]+)\]',prefix)
        if not by or not peer:raise ValueError('simplified IPv4 fixture Received form required')
        ipaddress.IPv4Address(peer[1])
        rows.append(dict(top_index=i,by_claim=by[1].lower(),peer_ip_text=peer[1],time_utc=t.astimezone(timezone.utc).isoformat()))
    index=assumption.get('boundary_received_index')
    if type(index) is not int or not 0<=index<len(rows):raise ValueError('explicit in-range boundary index required')
    expected=assumption.get('expected_by')
    if not isinstance(expected,str) or rows[index]['by_claim']!=expected.lower():raise ValueError('selected boundary disagrees with expected fixture receiver')
    ipaddress.IPv4Address(assumption['expected_peer_ip'])
    from datetime import datetime
    gaps=[dict(earlier_top_index=i,later_top_index=i-1,claimed_seconds=(datetime.fromisoformat(rows[i-1]['time_utc'])-datetime.fromisoformat(rows[i]['time_utc'])).total_seconds()) for i in range(len(rows)-1,0,-1)]
    return dict(message_sha256=hashlib.sha256(raw).hexdigest(),from_claim=str(msg['From']),return_path_claim=str(msg.get('Return-Path','')),message_id_claim=str(msg['Message-ID']),received_rows_top_first=rows,claimed_adjacent_intervals=gaps,selected_boundary_index=index,selected_peer_matches_supplied_expectation=rows[index]['peer_ip_text']==assumption['expected_peer_ip'],boundary_authority_verified=False,earlier_trace_authority_verified=False,originating_person_verified=False,mime_leaf_types=[p.get_content_type() for p in msg.walk() if not p.is_multipart()],body_rendered=False,authentication_checked=False,incident_verdict='unresolved',external_actions=0)

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('message',type=Path);p.add_argument('assumption',type=Path);a=p.parse_args()
    try:
        print(json.dumps(inspect(a.message.read_bytes(),json.loads(a.assumption.read_text(encoding='utf-8'))),indent=2));return 0
    except (OSError,ValueError,TypeError,KeyError,AttributeError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
