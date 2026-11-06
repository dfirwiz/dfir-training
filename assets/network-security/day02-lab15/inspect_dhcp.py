"""Read only the course's classic-PCAP Ethernet/IPv4/UDP DHCP subset, without network I/O."""
import argparse,struct,ipaddress,json,datetime
from pathlib import Path
NAMES={1:'Discover',2:'Offer',3:'Request',5:'ACK'}
def checksum(data):
    if len(data)%2:data+=b'\0'
    n=sum(struct.unpack('!%dH'%(len(data)//2),data))
    while n>>16:n=(n&65535)+(n>>16)
    return (~n)&65535
def ip(b):return str(ipaddress.IPv4Address(b))
def inspect(path):
    raw=Path(path).read_bytes();rows=[]
    if len(raw)<24 or struct.unpack('<IHHIIII',raw[:24])!=(0xa1b2c3d4,2,4,0,0,65535,1):raise ValueError('fixed classic PCAP contract required')
    offset=24
    while offset<len(raw):
        if offset+16>len(raw):raise ValueError('truncated record header')
        sec,usec,size,original=struct.unpack_from('<IIII',raw,offset);offset+=16
        if size!=original or offset+size>len(raw) or usec>=1000000:raise ValueError('truncated/invalid record')
        buf=raw[offset:offset+size];offset+=size
        if len(buf)<42 or buf[12:14]!=b'\x08\x00':raise ValueError('non-VLAN Ethernet IPv4 required')
        packet=buf[14:]
        if packet[0]!=0x45 or packet[9]!=17 or int.from_bytes(packet[6:8],'big')&0x3fff:raise ValueError('fixed nonfragmented IPv4 UDP required')
        if len(packet)!=int.from_bytes(packet[2:4],'big') or checksum(packet[:20]):raise ValueError('IPv4 length/checksum')
        udp=packet[20:];sport,dport,length,check=struct.unpack('!HHHH',udp[:8])
        if (sport,dport) not in ((68,67),(67,68)) or length!=len(udp) or not check:raise ValueError('fixture UDP ports/length/checksum required')
        if checksum(packet[12:20]+struct.pack('!BBH',0,17,length)+udp):raise ValueError('UDP checksum')
        m=udp[8:]
        if len(m)<240 or m[1:4]!=b'\x01\x06\x00' or m[236:240]!=bytes.fromhex('63825363'):raise ValueError('Ethernet DHCP header required')
        options={};i=240;ended=False
        while i<len(m):
            code=m[i];i+=1
            if code==255:ended=True;break
            if code==0:continue
            if i>=len(m) or i+1+m[i]>len(m):raise ValueError('option length')
            n=m[i];i+=1
            if code in options or code==52:raise ValueError('duplicate/overloaded options outside teaching subset')
            options[code]=m[i:i+n];i+=n
        if not ended or len(options.get(53,b''))!=1 or options[53][0] not in NAMES:raise ValueError('supported message type/end required')
        kind=options[53][0]
        if m[0]!=(2 if kind in (2,5) else 1):raise ValueError('message operation mismatch')
        def address(code):
            if code not in options:return None
            if len(options[code])!=4:raise ValueError('address option length')
            return ip(options[code])
        if 51 in options and len(options[51])!=4:raise ValueError('lease length')
        rows.append(dict(frame=len(rows)+1,time_utc=datetime.datetime.fromtimestamp(sec+usec/1e6,datetime.timezone.utc).isoformat(),source=ip(packet[12:16]),destination=ip(packet[16:20]),source_port=sport,destination_port=dport,xid=hex(int.from_bytes(m[4:8],'big')),client_mac=':'.join(f'{b:02x}' for b in m[28:34]),client_id=options.get(61,b'').hex(),broadcast_flag=bool(int.from_bytes(m[10:12],'big')&0x8000),message=NAMES[kind],ciaddr=ip(m[12:16]),yiaddr=ip(m[16:20]),giaddr=ip(m[24:28]),server_id=address(54),requested_ip=address(50),lease_seconds=int.from_bytes(options[51],'big') if 51 in options else None,hostname_claim=options[12].decode('ascii') if 12 in options else None))
    if not rows:raise ValueError('no packets')
    same=len({(r['xid'],r['client_mac'],r['client_id']) for r in rows})==1
    correlated=same and [r['message'] for r in rows]==['Discover','Offer','Request','ACK']
    if correlated:
        correlated=rows[1]['yiaddr']==rows[2]['requested_ip']==rows[3]['yiaddr'] and rows[1]['server_id']==rows[2]['server_id']==rows[3]['server_id']
    return dict(frames=rows,same_fixture_exchange_key=same,four_message_consistency=correlated,ack_observed=any(r['message']=='ACK' for r in rows),actual_device_configured='unverified',owner_identity='unverified',incident_verdict='unresolved',external_actions=0)
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('pcap',type=Path);a=p.parse_args()
    try:print(json.dumps(inspect(a.pcap),indent=2));return 0
    except (OSError,ValueError,struct.error,UnicodeError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
