"""Inspect the course's fixed cleartext FTP/EPSV/STOR fixture; never contact a server."""
from pathlib import Path
import argparse,struct,ipaddress,json,hashlib,re
def checksum(data):
    if len(data)%2:data+=b'\0'
    n=sum(struct.unpack('!%dH'%(len(data)//2),data))
    while n>>16:n=(n&65535)+(n>>16)
    return (~n)&65535
def join(rows):
    if not rows:return b'',False,0
    segments={};duplicates=0
    for seq,data in rows:
        if seq in segments:
            if segments[seq]!=data:raise ValueError('conflicting exact-sequence data')
            duplicates+=1
        segments[seq]=data
    seqs=sorted(segments);data=b'';expected=seqs[0];gap=False
    for seq in seqs:
        value=segments[seq]
        if seq<expected:raise ValueError('partial overlap outside teaching subset')
        if seq>expected:gap=True;break
        data+=value;expected=seq+len(value)
    return data,gap,duplicates
def inspect(path,reference):
    raw=Path(path).read_bytes();streams={};frames=0;offset=24
    if len(raw)<24 or struct.unpack('<IHHIIII',raw[:24])!=(0xa1b2c3d4,2,4,0,0,65535,1):raise ValueError('fixed classic PCAP contract required')
    while offset<len(raw):
        if offset+16>len(raw):raise ValueError('truncated record header')
        sec,usec,size,original=struct.unpack_from('<IIII',raw,offset);offset+=16
        if size!=original or offset+size>len(raw) or usec>=1000000:raise ValueError('truncated/invalid record')
        buf=raw[offset:offset+size];offset+=size;frames+=1
        if len(buf)<54 or buf[12:14]!=b'\x08\x00':raise ValueError('non-VLAN Ethernet IPv4 required')
        ip=buf[14:]
        if ip[0]!=0x45 or ip[9]!=6 or int.from_bytes(ip[6:8],'big')&0x3fff:raise ValueError('fixed nonfragmented IPv4 TCP required')
        if len(ip)!=int.from_bytes(ip[2:4],'big') or checksum(ip[:20]):raise ValueError('IPv4 length/checksum')
        tcp=ip[20:]
        if tcp[12]>>4!=5 or checksum(ip[12:20]+struct.pack('!BBH',0,6,len(tcp))+tcp):raise ValueError('TCP header/checksum')
        sport,dport,seq=struct.unpack('!HHI',tcp[:8]);payload=tcp[20:]
        if not payload:raise ValueError('only supplied payload segments supported')
        key=(str(ipaddress.IPv4Address(ip[12:16])),str(ipaddress.IPv4Address(ip[16:20])),sport,dport)
        streams.setdefault(key,[]).append((seq,payload))
    ckey=('192.0.2.25','198.51.100.20',50001,21);skey=('198.51.100.20','192.0.2.25',21,50001)
    client,cgap,cd=join(streams.get(ckey,[]));server,sgap,sd=join(streams.get(skey,[]))
    if cgap or sgap or not client.endswith(b'\r\n') or not server.endswith(b'\r\n'):raise ValueError('complete control directions required by teaching subset')
    lines=client.decode('ascii').splitlines();replies=server.decode('ascii').splitlines()
    if lines!=['USER user-a','PASS training-only','EPSV','TYPE I','STOR note.txt']:raise ValueError('one fixed fictional EPSV/TYPE-I/STOR exchange required')
    m=re.search(r'^229 .*\(\|\|\|(\d+)\|\)',server.decode('ascii'),re.M)
    if not m or not 1<=int(m[1])<=65535:raise ValueError('one teaching EPSV port required')
    data_key=('192.0.2.25','198.51.100.20',50002,int(m[1]))
    if set(streams)-{ckey,skey,data_key}:raise ValueError('unexpected flow outside teaching subset')
    data,gap,dd=join(streams.get(data_key,[]));ref=Path(reference).read_bytes()
    match=(data==ref) if not gap and len(data)==len(ref) else None
    return dict(frames=frames,client_control_lines=['PASS <redacted fictional value>' if x.startswith('PASS ') else x for x in lines],server_reply_codes=[int(x[:3]) for x in replies if re.match(r'^\d{3} ',x)],epsv_port=int(m[1]),server_reported_complete=any(x.startswith('226 ') for x in replies),observed_data_bytes=len(data),reference_bytes=len(ref),data_gap=gap,short_bytes_against_reference=max(0,len(ref)-len(data)),captured_prefix_sha256=hashlib.sha256(data).hexdigest() if data else None,reference_match=match,exact_retransmissions=cd+sd+dd,actual_server_authentication_verified=False,actual_server_file_stored=False,incident_verdict='unresolved',external_actions=0)
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('pcap',type=Path);p.add_argument('reference',type=Path);a=p.parse_args()
    try:print(json.dumps(inspect(a.pcap,a.reference),indent=2));return 0
    except (OSError,ValueError,struct.error,UnicodeError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
