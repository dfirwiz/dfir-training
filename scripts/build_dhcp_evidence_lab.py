"""Create an offline documentation-only Ethernet/IPv4/UDP DHCP fixture; no sockets."""
from pathlib import Path
import struct,ipaddress,datetime

ROOT=Path(__file__).resolve().parents[1]/'assets/network-security/day02-lab15'
def checksum(data):
    if len(data)%2:data+=b'\0'
    n=sum(struct.unpack('!%dH'%(len(data)//2),data))
    while n>>16:n=(n&65535)+(n>>16)
    return (~n)&65535
def ip(value):return ipaddress.IPv4Address(value).packed
def option(n,value):return bytes([n,len(value)])+value
def frame(kind):
    client=bytes.fromhex('020000000025');server=bytes.fromhex('020000000001')
    reply=kind in (2,5);src='192.0.2.1' if reply else '0.0.0.0';dst='255.255.255.255'
    msg=struct.pack('!BBBBIHH',2 if reply else 1,1,6,0,0x45000001,0,0x8000)
    msg+=ip('0.0.0.0')+ip('192.0.2.25' if reply else '0.0.0.0')+b'\0'*8+client+b'\0'*10+b'\0'*192
    msg+=bytes.fromhex('63825363')+option(53,bytes([kind]))+option(61,b'\x01'+client)
    if not reply:msg+=option(12,b'workstation-a')+option(55,bytes([1,3,6,51]))
    if kind==3:msg+=option(50,ip('192.0.2.25'))+option(54,ip('192.0.2.1'))
    if reply:msg+=option(54,ip('192.0.2.1'))+option(51,struct.pack('!I',3600))+option(1,ip('255.255.255.0'))+option(3,ip('192.0.2.1'))+option(6,ip('192.0.2.53'))
    msg+=b'\xff';msg=msg.ljust(300,b'\0')
    length=8+len(msg);udp=struct.pack('!HHHH',67 if reply else 68,68 if reply else 67,length,0)+msg
    pseudo=ip(src)+ip(dst)+struct.pack('!BBH',0,17,length)
    udp=udp[:6]+struct.pack('!H',checksum(pseudo+udp) or 65535)+udp[8:]
    header=struct.pack('!BBHHHBBH4s4s',0x45,0,20+len(udp),kind,0,64,17,0,ip(src),ip(dst))
    header=header[:10]+struct.pack('!H',checksum(header))+header[12:]
    return b'\xff'*6+(server if reply else client)+b'\x08\x00'+header+udp
def build():
    ROOT.mkdir(parents=True,exist_ok=True)
    base=int(datetime.datetime(2026,11,7,9,tzinfo=datetime.timezone.utc).timestamp())
    frames=[frame(k) for k in (1,2,3,5)]
    for name,count in [('dora.pcap',4),('missing-ack.pcap',3)]:
        data=struct.pack('<IHHIIII',0xa1b2c3d4,2,4,0,0,65535,1)
        for i,buf in enumerate(frames[:count]):data+=struct.pack('<IIII',base+i,0,len(buf),len(buf))+buf
        (ROOT/name).write_bytes(data)
    print('Created offline DHCP files: 4 frames / 3 frames; no network I/O.')
if __name__=='__main__':build()
