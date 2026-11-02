"""Independently decode the original training PCAP with dpkt 1.9.8.

This deliberately handles only the unfragmented, complete messages in this lab.
It does not implement general TCP reassembly or arbitrary capture analysis.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict,deque
import csv,hashlib,ipaddress,json,struct,zipfile
import dpkt

OUT=Path(__file__).resolve().parents[1]/'assets/network-security/lab05'
TYPES={1:'A',5:'CNAME',6:'SOA',12:'PTR',16:'TXT',28:'AAAA'}
def csvwrite(path,rows):
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
def utc(ts):return datetime.fromtimestamp(ts,tz=timezone.utc).isoformat(timespec='microseconds').replace('+00:00','Z')
def decode(path):
    rows=[];pending=defaultdict(deque);transactions=[];dns_count=0
    with path.open('rb') as f:
        reader=dpkt.pcap.Reader(f);assert reader.datalink()==1
        for frame_no,(ts,raw) in enumerate(reader,1):
            eth=dpkt.ethernet.Ethernet(raw);ip=eth.data
            assert isinstance(ip,dpkt.ip.IP) and not ip.offset
            assert len(raw)==14+ip.len
            assert dpkt.in_cksum(raw[14:34])==0
            transport=ip.data;proto='UDP' if isinstance(transport,dpkt.udp.UDP) else 'TCP'
            pseudo=ip.src+ip.dst+struct.pack('!BBH',0,ip.p,len(bytes(transport)))
            assert dpkt.in_cksum(pseudo+bytes(transport))==0
            row=dict(frame=frame_no,time_utc=utc(ts),relative_seconds=f'{ts-1793577600:.6f}',transport=proto,src=str(ipaddress.ip_address(ip.src)),sport=transport.sport,dst=str(ipaddress.ip_address(ip.dst)),dport=transport.dport,is_response='',dns_id='',qname='',qtype='',rcode='',tc='',answers='',ttls='',authority_types='')
            payload=bytes(transport.data)
            if payload:
                if proto=='TCP':
                    declared=struct.unpack('!H',payload[:2])[0];payload=payload[2:];assert declared==len(payload)
                msg=dpkt.dns.DNS(payload);dns_count+=1;assert len(msg.qd)==1
                q=msg.qd[0];answers=[]
                for rr in msg.an:
                    if rr.type in (1,28):v=str(ipaddress.ip_address(rr.ip if rr.type==1 else rr.ip6))
                    elif rr.type==5:v=rr.cname
                    elif rr.type==12:v=rr.ptrname
                    elif rr.type==16:v=' '.join(x.decode() if isinstance(x,bytes) else x for x in rr.text)
                    else:v='[not decoded]'
                    answers.append(f'{rr.name} {TYPES.get(rr.type,rr.type)} {v}')
                row.update(is_response=msg.qr,dns_id=f'0x{msg.id:04x}',qname=q.name,qtype=TYPES.get(q.type,str(q.type)),rcode=msg.rcode,tc=msg.tc,answers='; '.join(answers),ttls=';'.join(str(rr.ttl) for rr in msg.an),authority_types=';'.join(TYPES.get(rr.type,str(rr.type)) for rr in msg.ns))
                forward=(proto,row['src'],row['sport'],row['dst'],row['dport'],msg.id,q.name,q.type)
                reverse=(proto,row['dst'],row['dport'],row['src'],row['sport'],msg.id,q.name,q.type)
                if not msg.qr:pending[forward].append(row)
                else:
                    assert pending[reverse],('orphan response',frame_no)
                    query=pending[reverse].popleft()
                    transactions.append(dict(query_frame=query['frame'],response_frame=frame_no,client=query['src'],resolver=query['dst'],transport=proto,dns_id=row['dns_id'],qname=q.name,qtype=row['qtype'],rcode=msg.rcode,tc=msg.tc,answers=row['answers']))
            rows.append(row)
    for queue in pending.values():
        for q in queue:transactions.append(dict(query_frame=q['frame'],response_frame='',client=q['src'],resolver=q['dst'],transport=q['transport'],dns_id=q['dns_id'],qname=q['qname'],qtype=q['qtype'],rcode='',tc='',answers=''))
    transactions.sort(key=lambda t:t['query_frame'])
    return rows,transactions,dns_count

rows,transactions,dns_count=decode(OUT/'dns-client.pcap')
upstream,upstream_tx,upstream_dns=decode(OUT/'dns-upstream.pcap')
queries=[r for r in rows if r['is_response']==0];responses=[r for r in rows if r['is_response']==1]
collect=[r for r in queries if r['qname'].endswith('.collect.example.net')]
external=[r['frame'] for r in queries if r['dst']!='192.0.2.53']
stats=dict(decoder=f'dpkt {dpkt.__version__}',frames=len(rows),dns_messages=dns_count,query_rows=len(queries),response_rows=len(responses),paired_queries=sum(bool(t['response_frame']) for t in transactions),unanswered_query_frames=[t['query_frame'] for t in transactions if not t['response_frame']],external_query_frames=external,collect_query_frames=[r['frame'] for r in collect],collect_query_rows=len(collect),collect_unique_names=len(set(r['qname'] for r in collect)),collect_unique_ratio=len(set(r['qname'] for r in collect))/len(collect),nxdomain_responses=sum(r['rcode']==3 for r in responses),nxdomain_response_ratio=sum(r['rcode']==3 for r in responses)/len(responses),truncated_response_frames=[r['frame'] for r in responses if r['tc']],tcp_dns_frames=[r['frame'] for r in rows if r['transport']=='TCP' and r['qname']],upstream_frames=len(upstream),upstream_query_sources=sorted(set(t['client'] for t in upstream_tx)),ipv4_and_transport_checksums='all valid')
assert len(rows)==46 and dns_count==42 and len(queries)==22 and len(responses)==20
assert stats['unanswered_query_frames']==[15,16] and external==[13]
assert stats['collect_query_rows']==8 and stats['collect_unique_names']==6
assert stats['truncated_response_frames']==[40] and stats['tcp_dns_frames']==[44,45]
assert transactions[0]['response_frame']==4 and transactions[1]['response_frame']==3
assert rows[7]['rcode']==0 and not rows[7]['answers'] and rows[7]['authority_types']=='SOA'
assert rows[9]['rcode']==3 and rows[11]['ttls']=='180;180;180'
csvwrite(OUT/'packets.csv',rows);csvwrite(OUT/'transactions.csv',transactions)
(OUT/'analysis-results.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
files=sorted(p for p in OUT.iterdir() if p.is_file() and p.name not in ('SHA256SUMS.txt','dns-investigation-lab.zip'))
(OUT/'SHA256SUMS.txt').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in files),encoding='ascii',newline='\n')
with zipfile.ZipFile(OUT/'dns-investigation-lab.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in files+[OUT/'SHA256SUMS.txt']:
        info=zipfile.ZipInfo(p.name,date_time=(2026,11,2,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED
        z.writestr(info,p.read_bytes())
print(json.dumps(stats,ensure_ascii=False,indent=2))
