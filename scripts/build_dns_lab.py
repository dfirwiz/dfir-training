"""Generate original, deterministic offline training data. No network I/O."""
from pathlib import Path
from datetime import datetime, timezone
import csv, ipaddress, struct

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/network-security/lab05'
OUT.mkdir(parents=True,exist_ok=True)
BASE=int(datetime(2026,11,2,tzinfo=timezone.utc).timestamp())
TYPES={'A':1,'CNAME':5,'SOA':6,'PTR':12,'TXT':16,'AAAA':28}

def name(s):
    return b''.join(bytes([len(x)])+x.encode('ascii') for x in s.rstrip('.').split('.'))+b'\0'

def rr(owner,kind,value,ttl=300):
    if kind in ('A','AAAA'):data=ipaddress.ip_address(value).packed
    elif kind in ('CNAME','PTR'):data=name(value)
    elif kind=='TXT':data=bytes([len(value)])+value.encode('ascii')
    elif kind=='SOA':data=name('ns.example.com')+name('hostmaster.example.com')+struct.pack('!5I',2026110201,3600,600,86400,300)
    else:raise ValueError(kind)
    return name(owner)+struct.pack('!HHIH',TYPES[kind],1,ttl,len(data))+data

def dns(ident,qname,kind,answers=(),response=False,rcode=0,tc=False,negative=False):
    flags=(0x8180 if response else 0x0100)|rcode|(0x0200 if tc else 0)
    question=name(qname)+struct.pack('!HH',TYPES[kind],1)
    auth=rr('example.com','SOA',None) if negative else b''
    return struct.pack('!6H',ident,flags,1,len(answers),int(negative),0)+question+b''.join(rr(*a) for a in answers)+auth

def checksum(data):
    if len(data)%2:data+=b'\0'
    total=sum(struct.unpack('!%dH'%(len(data)//2),data))
    while total>>16:total=(total&65535)+(total>>16)
    return (~total)&65535

def frame(src,dst,sport,dport,payload,proto=17,seq=0,ack=0,flags=0x18):
    a=ipaddress.IPv4Address(src).packed;b=ipaddress.IPv4Address(dst).packed
    if proto==17:header=struct.pack('!4H',sport,dport,8+len(payload),0)
    else:header=struct.pack('!HHIIBBHHH',sport,dport,seq,ack,0x50,flags,65535,0,0)
    pseudo=a+b+struct.pack('!BBH',0,proto,len(header)+len(payload))
    csum=checksum(pseudo+header+payload) or 65535
    offset=6 if proto==17 else 16
    header=header[:offset]+struct.pack('!H',csum)+header[offset+2:]
    ip=struct.pack('!BBHHHBBH4s4s',0x45,0,20+len(header)+len(payload),0,0,64,proto,0,a,b)
    ip=ip[:10]+struct.pack('!H',checksum(ip))+ip[12:]
    ethernet=bytes.fromhex('0200000000020200000000010800')
    return ethernet+ip+header+payload

def write_pcap(path,events):
    with path.open('wb') as f:
        f.write(struct.pack('<IHHIIII',0xa1b2c3d4,2,4,0,0,65535,1))
        for elapsed,packet in events:
            sec=int(elapsed);usec=round((elapsed-sec)*1000000)
            f.write(struct.pack('<IIII',BASE+sec,usec,len(packet),len(packet))+packet)

def write_csv(path,rows,fields=None):
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields or list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)

def build():
    events=[];r='192.0.2.53';c='192.0.2.25';d='192.0.2.26'
    def udp(t,src,dst,sp,dp,p):events.append((t,frame(src,dst,sp,dp,p)))
    def pair(t,client,port,ident,q,kind,answers=(),resolver=r,rcode=0,negative=False,tc=False):
        udp(t,client,resolver,port,53,dns(ident,q,kind))
        udp(t+.02,resolver,client,53,port,dns(ident,q,kind,answers,True,rcode,tc,negative))
    addr=[('portal.example.com','CNAME','edge.example.com',300),('edge.example.com','A','203.0.113.80',300),('edge.example.com','A','203.0.113.81',300)]
    udp(0,c,r,53001,53,dns(0x1001,'portal.example.com','A'))
    udp(.01,d,r,53002,53,dns(0x1001,'files.example.net','AAAA'))
    udp(.04,r,d,53,53002,dns(0x1001,'files.example.net','AAAA',[('files.example.net','AAAA','2001:db8::20',300)],True))
    udp(.05,r,c,53,53001,dns(0x1001,'portal.example.com','A',addr,True))
    pair(1,c,53003,0x1002,'80.113.0.203.in-addr.arpa','PTR',[('80.113.0.203.in-addr.arpa','PTR','edge.example.com',300)])
    pair(2,c,53004,0x1003,'empty.example.com','AAAA',negative=True)
    pair(3,c,53005,0x1004,'missing.example.com','A',rcode=3,negative=True)
    pair(120,c,53006,0x1005,'portal.example.com','A',[(o,k,v,180) for o,k,v,_ in addr])
    pair(121,c,53007,0x1006,'portal.example.com','A',[('portal.example.com','A','203.0.113.80',300)],resolver='198.51.100.53')
    for t in [122,123]:udp(t,d,r,53008,53,dns(0x1007,'unanswered.example.org','A'))
    for i,n in enumerate([1,2,3,4,5,6,1,2]):
        q=f'part{n:02d}.'+'4142434445464748495041424344454647484950'+'.collect.example.net'
        pair(130+i,c,53100+i,0x1100+i,q,'TXT',[(q,'TXT',f'LAB-ACK-{n:02d}',30)])
    for i in [1,2]:
        q=f'check{i:02d}.'+'4142434445464748495041424344454647484950'+'.check.security.example.com'
        pair(140+i,d,53200+i,0x1200+i,q,'TXT',[(q,'TXT','TRAINING-VERDICT-UNKNOWN',60)])
    pair(145,c,53300,0x1300,'www.xn--exmple-4nf.example','A',[('www.xn--exmple-4nf.example','A','203.0.113.90',300)])
    pair(150,c,53400,0x1400,'large.example.org','TXT',tc=True)
    q=dns(0x1401,'large.example.org','TXT');a=dns(0x1401,'large.example.org','TXT',[('large.example.org','TXT','Training response over TCP.',300)],True)
    q=struct.pack('!H',len(q))+q;a=struct.pack('!H',len(a))+a
    def tcp(t,src,dst,sp,dp,p,seq,ack,flags):events.append((t,frame(src,dst,sp,dp,p,6,seq,ack,flags)))
    tcp(150.10,c,r,54000,53,b'',1000,0,2)
    tcp(150.12,r,c,53,54000,b'',5000,1001,0x12)
    tcp(150.13,c,r,54000,53,b'',1001,5001,0x10)
    tcp(150.14,c,r,54000,53,q,1001,5001,0x18)
    tcp(150.16,r,c,53,54000,a,5001,1001+len(q),0x18)
    tcp(150.17,c,r,54000,53,b'',1001+len(q),5001+len(a),0x10)
    events.sort(key=lambda e:e[0]);assert len(events)==46
    write_pcap(OUT/'dns-client.pcap',events)
    upstream=[]
    tunnel_name='part01.'+'4142434445464748495041424344454647484950'+'.collect.example.net'
    for t,ident,q,kind,answers in [(.02,0x9001,'portal.example.com','A',addr),(130.005,0x9002,tunnel_name,'TXT',[(tunnel_name,'TXT','LAB-ACK-01',30)])]:
        upstream.append((t,frame(r,'198.51.100.53',55000+(ident&255),53,dns(ident,q,kind))))
        upstream.append((t+.010,frame('198.51.100.53',r,53,55000+(ident&255),dns(ident,q,kind,answers,True))))
    write_pcap(OUT/'dns-upstream.pcap',upstream)
    write_csv(OUT/'endpoint-events.csv',[
      dict(time_utc='2026-11-02T00:00:00Z',host='WS25',process_guid='PROC-BROWSER-25',image='browser.exe',event='dns_query',detail='portal.example.com'),
      dict(time_utc='2026-11-02T00:02:01Z',host='WS25',process_guid='PROC-DIAG-25',image='diagnostic-helper.exe',event='dns_query',detail='portal.example.com; resolver=198.51.100.53; approval unknown'),
      dict(time_utc='2026-11-02T00:02:09Z',host='WS25',process_guid='PROC-HELPER-25',image='lab-helper.exe',event='process_start',detail='installation approval unknown'),
      dict(time_utc='2026-11-02T00:02:09.500000Z',host='WS25',process_guid='PROC-HELPER-25',image='lab-helper.exe',event='file_read',detail='training-notes.txt; content not recorded'),
      dict(time_utc='2026-11-02T00:02:10Z',host='WS25',process_guid='PROC-HELPER-25',image='lab-helper.exe',event='dns_query',detail='collect.example.net subtree; DNS payload not recorded here'),
      dict(time_utc='2026-11-02T00:02:21Z',host='WS26',process_guid='PROC-SECURITY-26',image='security-agent.exe',event='dns_query',detail='check.security.example.com subtree; approved training inventory entry')])
    write_csv(OUT/'asset-inventory.csv',[
      dict(ip=c,host='WS25',role='employee endpoint',valid_from_utc='2026-11-02T00:00:00Z',valid_to_utc='2026-11-02T01:00:00Z'),
      dict(ip=d,host='WS26',role='employee endpoint',valid_from_utc='2026-11-02T00:00:00Z',valid_to_utc='2026-11-02T01:00:00Z'),
      dict(ip=r,host='DNS-FWD',role='approved forwarding resolver',valid_from_utc='2026-11-02T00:00:00Z',valid_to_utc='2026-11-02T01:00:00Z')])
    write_csv(OUT/'connection-events.csv',[
      dict(time_utc='2026-11-02T00:00:00.200000Z',src=c,dst='203.0.113.80',dst_port=443,transport='tcp',observation='connection allowed; application success not recorded'),
      dict(time_utc='2026-11-02T00:02:01Z',src=c,dst='198.51.100.53',dst_port=53,transport='udp',observation='allow; endpoint resolver use outside approved policy')])
    (OUT/'README.txt').write_text('DNS investigation lab 05 / version 1\n\nAll data is original synthetic training data, generated offline. No real traffic was captured or sent. Documentation IPs and example domains only.\n\nPolicy: employee endpoints use 192.0.2.53 only. The forwarding resolver may use 198.51.100.53 as upstream.\n\ndns-client.pcap: client-side synthetic Ethernet/IPv4 traffic, 46 frames; UDP and TCP DNS.\ndns-upstream.pcap: separate upstream observation, 4 frames, not the same sensor.\npackets.csv: independently decoded packet fields from dns-client.pcap; not TShark output.\ntransactions.csv: query-row pairing by transport/address/port/ID/question; repeated unanswered rows retained.\nanalysis-results.json: measured counts from file decoding.\nendpoint-events.csv, asset-inventory.csv, connection-events.csv: independent fictional context, not measured host telemetry.\n\nTimes are UTC. The interval is 2026-11-02T00:00:00Z through 00:02:30.170000Z. Two unanswered query rows are intentional. TC=1 followed by TCP is intentional. The IPv6 address is an AAAA answer transported over IPv4; no IPv6 packet exists in this lab. No DoH/DoT/DoQ or malicious code exists. TXT values are inert training markers.\n\nOpen PCAPs locally in Wireshark; do not replay them or resolve the names. All generated files are educational examples, not original vendor workbook materials.\n',encoding='utf-8',newline='\n')
    (OUT/'README-ko.txt').write_text('''DNS 분석 실습 05 / 자료 버전 1

이 자료는 오프라인에서 만든 독립적인 교육용 합성 자료입니다.
실제 회사·단말·사용자·침해 사건의 기록이 아닙니다. 네트워크 수집·전송·조회는 하지 않았습니다.
원래 교재 워크북의 자료가 아닙니다. 자세한 순서와 해설은 5강 웹페이지를 참고하세요.

제시된 정책: 직원 단말은 192.0.2.53만 사용합니다.
전달 서버 192.0.2.53은 상위 198.51.100.53에 질문할 수 있습니다.

dns-client.pcap: 단말 쪽을 가정한 46개 패킷입니다. IPv4 안에 UDP/TCP DNS가 있습니다.
dns-upstream.pcap: 두 대화만 넣은 별도 상위 관측 사례 4개 패킷입니다. 전체 상위 수집본이 아닙니다.
packets.csv: 독립 해석기 dpkt로 첫 PCAP을 읽은 표입니다. TShark 출력이 아닙니다.
transactions.csv: 질문 행과 응답을 연결합니다. 응답 미관측 재시도 두 행을 그대로 남겼습니다.
endpoint-events.csv, asset-inventory.csv, connection-events.csv: 가상 보조 맥락이며 실제 수집 결과가 아닙니다.
analysis-results.json: PCAP 해석에서 확인한 수치입니다.
SHA256SUMS.txt: ZIP을 제외한 파일의 SHA-256 비교값입니다.

시간은 UTC이며 2026-11-02 00:00:00부터 00:02:30.170000까지입니다.
AAAA 응답의 IPv6 주소는 IPv4 패킷에 들어 있습니다. IPv6 패킷은 없습니다.
응답 없는 질문 두 행과 TC=1 이후 TCP 조회는 의도한 조건입니다.
TXT 값은 무해한 학습 표식이며 실제 파일이나 공격 명령이 아닙니다.
DoH/DoT/DoQ·실제 악성 실행·실제 정보 유출은 포함하지 않았습니다.

PCAP은 로컬 도구로 읽기만 하세요. 패킷 재전송·도메인 실제 조회가 필요한 실습이 아닙니다.
''',encoding='utf-8',newline='\n')
    print('Generated synthetic PCAPs and context; run independent decoder next.')

if __name__=='__main__':build()
