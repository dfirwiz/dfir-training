"""Create harmless fictional HTTP packets and timing records; no network I/O."""
from pathlib import Path
import csv,struct,socket,gzip,hashlib,json
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'assets/network-security/day02-lab08'

def checksum(b):
    if len(b)%2:b+=b'\x00'
    s=sum(struct.unpack('!%dH'%(len(b)//2),b));s=(s&65535)+(s>>16);s=(s&65535)+(s>>16)
    return (~s)&65535

def packet(src,dst,sport,dport,seq,ack,data,ident):
    a,b=socket.inet_aton(src),socket.inet_aton(dst)
    tcp=struct.pack('!HHIIBBHHH',sport,dport,seq,ack,80,24,65535,0,0)+data
    tc=checksum(a+b+struct.pack('!BBH',0,6,len(tcp))+tcp)
    tcp=tcp[:16]+struct.pack('!H',tc)+tcp[18:]
    ip=struct.pack('!BBHHHBBH4s4s',69,0,20+len(tcp),ident,16384,64,6,0,a,b)
    ip=ip[:10]+struct.pack('!H',checksum(ip))+ip[12:]
    return bytes.fromhex('0200000000020200000000010800')+ip+tcp

def build():
    OUT.mkdir(parents=True,exist_ok=True)
    plain=b'Training only.\n';encoded=gzip.compress(plain,mtime=0)
    request=b'GET /note.txt HTTP/1.1\r\nHost: files.example\r\nUser-Agent: TrainingClient/1.0\r\nConnection: close\r\n\r\n'
    header=b'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Encoding: gzip\r\nContent-Length: '+str(len(encoded)).encode()+b'\r\nConnection: close\r\n\r\n'
    response=header+encoded;cut=len(header)+10
    frames=[packet('192.0.2.25','198.51.100.20',50000,80,1001,9001,request,1),packet('198.51.100.20','192.0.2.25',80,50000,9001,1001+len(request),response[:cut],2),packet('198.51.100.20','192.0.2.25',80,50000,9001+cut,1001+len(request),response[cut:],3)]
    for name,selected in [('complete.pcap',frames),('missing-tail.pcap',frames[:2])]:
        data=struct.pack('<IHHIIII',0xa1b2c3d4,2,4,0,0,65535,1)
        for i,f in enumerate(selected):data+=struct.pack('<IIII',1793523600,i*100000,len(f),len(f))+f
        (OUT/name).write_bytes(data)
    (OUT/'expected-note.txt').write_bytes(plain)
    with (OUT/'intervals.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f,lineterminator='\n');w.writerow(['source','id','group','seconds','context'])
        for group,times,context in [('A',[0,60,120,180,240],'unknown process'),('B',[0,60,120,180,240],'claimed scheduled job; verify approval'),('C',[0,55,120,181,240],'variable interval'),('D',[0,60,180,240],'one event omitted by fixture')]:
            for i,t in enumerate(times):w.writerow(['sensor-1',group+str(i),group,t,context])
        w.writerow(['sensor-1','A1','A',60,'unknown process'])
    manifest=dict(notice='Independent fictional packets, not live capture or original workbook',plain_bytes=len(plain),encoded_bytes=len(encoded),header_bytes=len(header),response_bytes=len(response),response_first_payload=cut,response_second_payload=len(response)-cut,plain_sha256=hashlib.sha256(plain).hexdigest(),frames_full=3,frames_missing=2)
    print(json.dumps(manifest,indent=2))
if __name__=='__main__':build()
