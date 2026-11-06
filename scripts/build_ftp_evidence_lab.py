"""Build harmless offline FTP segment fixtures; no sockets or file transfer."""
from pathlib import Path
import struct,ipaddress,datetime,hashlib
ROOT=Path(__file__).resolve().parents[1]/'assets/network-security/day02-lab20'
def checksum(data):
    if len(data)%2:data+=b'\0'
    n=sum(struct.unpack('!%dH'%(len(data)//2),data))
    while n>>16:n=(n&65535)+(n>>16)
    return (~n)&65535
def frame(src,dst,sport,dport,seq,ack,data,identity):
    a=ipaddress.IPv4Address(src).packed;b=ipaddress.IPv4Address(dst).packed
    tcp=struct.pack('!HHIIBBHHH',sport,dport,seq,ack,0x50,0x18,65535,0,0)+data
    pseudo=a+b+struct.pack('!BBH',0,6,len(tcp));tcp=tcp[:16]+struct.pack('!H',checksum(pseudo+tcp))+tcp[18:]
    ip=struct.pack('!BBHHHBBH4s4s',0x45,0,len(tcp)+20,identity,0,64,6,0,a,b);ip=ip[:10]+struct.pack('!H',checksum(ip))+ip[12:]
    client=bytes.fromhex('020000000025');server=bytes.fromhex('020000000020')
    ethernet=(server+client) if src=='192.0.2.25' else (client+server)
    return ethernet+b'\x08\x00'+ip+tcp
def build():
    ROOT.mkdir(parents=True,exist_ok=True);note=b'Training only.\n';(ROOT/'expected-note.txt').write_bytes(note)
    cseq=1000;sseq=2000;dseq=9000;frames=[]
    items=[('c',b'USER user-a\r\n'),('s',b'331 Password required\r\n'),('c',b'PASS training-only\r\n'),('s',b'230 User logged in\r\n'),('c',b'EPSV\r\n'),('s',b'229 Entering Extended Passive Mode (|||50000|)\r\n'),('c',b'TYPE I\r\n'),('s',b'200 Type set to I\r\n'),('c',b'STOR note.txt\r\n'),('s',b'150 Opening data connection\r\n'),('d',note[:9]),('d',note[9:]),('s',b'226 Transfer complete\r\n')]
    for n,(side,data) in enumerate(items):
        if side=='c':args=('192.0.2.25','198.51.100.20',50001,21,cseq,sseq);cseq+=len(data)
        elif side=='s':args=('198.51.100.20','192.0.2.25',21,50001,sseq,cseq);sseq+=len(data)
        else:args=('192.0.2.25','198.51.100.20',50002,50000,dseq,0);dseq+=len(data)
        frames.append(frame(*args,data,n+1))
    base=int(datetime.datetime(2026,11,7,9,tzinfo=datetime.timezone.utc).timestamp())
    for name,indices in [('ftp-complete.pcap',range(13)),('ftp-missing-data.pcap',[*range(11),12])]:
        raw=struct.pack('<IHHIIII',0xa1b2c3d4,2,4,0,0,65535,1)
        for i in indices:
            buf=frames[i];raw+=struct.pack('<IIII',base+i,0,len(buf),len(buf))+buf
        (ROOT/name).write_bytes(raw)
    print('Created offline FTP13/12-segment files; reference15bytes '+hashlib.sha256(note).hexdigest())
if __name__=='__main__':build()
