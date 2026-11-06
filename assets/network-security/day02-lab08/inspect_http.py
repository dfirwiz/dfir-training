"""Inspect this course's single-flow IPv4 HTTP/1.1 fixture, never execute extracted data."""
import argparse,hashlib,json,struct,gzip,socket
from pathlib import Path
import dpkt

def inspect(path):
    segments={};frames=0;requests=0
    with Path(path).open('rb') as f:
        capture=dpkt.pcap.Reader(f)
        if capture.datalink()!=1:raise ValueError('Ethernet fixture required')
        for ts,buf in capture:
            frames+=1;eth=dpkt.ethernet.Ethernet(buf);ip=eth.data
            if not isinstance(ip,dpkt.ip.IP) or not isinstance(ip.data,dpkt.tcp.TCP):raise ValueError('fixture requires IPv4 TCP')
            if ip.offset or ip.mf:raise ValueError('fragmented IP not supported')
            raw=buf[14:];hlen=ip.hl*4
            if len(raw)!=ip.len or dpkt.in_cksum(raw[:hlen])!=0:raise ValueError('IP length/checksum')
            tcpraw=raw[hlen:];pseudo=ip.src+ip.dst+struct.pack('!BBH',0,6,len(tcpraw))
            if dpkt.in_cksum(pseudo+tcpraw)!=0:raise ValueError('TCP checksum')
            tcp=ip.data
            if tcp.sport==50000 and tcp.dport==80:
                if socket.inet_ntoa(ip.src)!='192.0.2.25' or socket.inet_ntoa(ip.dst)!='198.51.100.20':raise ValueError('unexpected fixture addresses')
                req=dpkt.http.Request(tcp.data)
                if req.method!='GET' or req.uri!='/note.txt' or req.headers.get('host')!='files.example':raise ValueError('unexpected fixture request')
                requests+=1;continue
            if tcp.sport!=80 or tcp.dport!=50000:raise ValueError('unexpected direction')
            if socket.inet_ntoa(ip.src)!='198.51.100.20' or socket.inet_ntoa(ip.dst)!='192.0.2.25':raise ValueError('unexpected fixture addresses')
            if tcp.seq in segments and segments[tcp.seq]!=tcp.data:raise ValueError('conflicting retransmission')
            segments[tcp.seq]=tcp.data
    if requests!=1 or not segments:raise ValueError('one complete fixture request and response required')
    end=None;chunks=[]
    for seq,data in sorted(segments.items()):
        if end is not None and seq!=end:raise ValueError('gap or overlap; general TCP reassembly not supported')
        chunks.append(data);end=seq+len(data)
    payload=b''.join(chunks);header,sep,body=payload.partition(b'\r\n\r\n')
    if not sep:raise ValueError('incomplete header')
    lines=header.decode('ascii').split('\r\n')
    if lines[0]!='HTTP/1.1 200 OK':raise ValueError('fixture response required')
    fields=dict(x.split(': ',1) for x in lines[1:])
    if fields.get('Content-Encoding')!='gzip' or 'Transfer-Encoding' in fields:raise ValueError('only gzip with fixed Content-Length supported')
    declared=int(fields['Content-Length']);complete=len(body)==declared
    if len(body)>declared:raise ValueError('body exceeds declared fixture length')
    result=dict(frames=frames,checksum_validated=True,declared_body_bytes=declared,observed_body_bytes=len(body),missing_body_bytes=declared-len(body),complete=complete,external_actions=0,incident_verdict='unresolved')
    if complete:
        plain=gzip.decompress(body)
        if len(plain)>1024:raise ValueError('fixture text too large')
        result.update(decoded_bytes=len(plain),decoded_text=plain.decode('ascii'),decoded_sha256=hashlib.sha256(plain).hexdigest())
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('capture');a=p.parse_args()
    try:print(json.dumps(inspect(a.capture),indent=2))
    except (OSError,ValueError,EOFError,dpkt.Error) as e:print('ERROR '+str(e));raise SystemExit(2)
