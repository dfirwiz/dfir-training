"""Generate local fictional ICMP records. No sockets or packet transmission."""
from pathlib import Path
import struct,ipaddress,datetime
ROOT=Path(__file__).resolve().parents[1]/'assets/network-security/day02-lab21'
def checksum(b):
 if len(b)%2:b+=b'\0'
 n=sum(struct.unpack('!%dH'%(len(b)//2),b))
 while n>>16:n=(n&65535)+(n>>16)
 return (~n)&65535
def ip(src,dst,proto,data,ident):
 h=struct.pack('!BBHHHBBH4s4s',0x45,0,20+len(data),ident,0,64,proto,0,ipaddress.ip_address(src).packed,ipaddress.ip_address(dst).packed)
 return h[:10]+struct.pack('!H',checksum(h))+h[12:]+data
def icmp(t,c,rest,data):
 b=struct.pack('!BBH',t,c,0)+rest+data
 return b[:2]+struct.pack('!H',checksum(b))+b[4:]
def build():
 a='192.0.2.25';b='198.51.100.20';router='203.0.113.1'
 rows=[(a,b,8,0,struct.pack('!HH',700,1),b'training-one'),(b,a,0,0,struct.pack('!HH',700,1),b'training-one'),(a,b,8,0,struct.pack('!HH',700,2),b'note-for-lab'),(b,a,0,0,struct.pack('!HH',700,2),b'changed-text'),(b,a,0,0,struct.pack('!HH',900,3),b'orphan')]
 udp=struct.pack('!HHHH',50001,33434,8,0);quoted=ip(a,b,17,udp,99)
 rows.append((b,a,3,3,b'\0'*4,quoted))
 raw=struct.pack('<IHHIIII',0xa1b2c3d4,2,4,0,0,65535,1);base=int(datetime.datetime(2026,11,7,tzinfo=datetime.timezone.utc).timestamp())
 for n,(src,dst,t,c,rest,data) in enumerate(rows):
  mac={a:bytes.fromhex('020000000025'),b:bytes.fromhex('020000000020')}
  frame=mac[dst]+mac[src]+b'\x08\x00'+ip(src,dst,1,icmp(t,c,rest,data),n+1)
  raw+=struct.pack('<IIII',base+n,0,len(frame),len(frame))+frame
 ROOT.mkdir(parents=True,exist_ok=True);(ROOT/'icmp-training.pcap').write_bytes(raw)
 print('Wrote6fictionalICMPframes; no packets sent.')
if __name__=='__main__':build()
