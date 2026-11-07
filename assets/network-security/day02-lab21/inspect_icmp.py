"""Inspect the course's fixed nonfragmented Ethernet IPv4 ICMP subset, offline."""
from pathlib import Path
import struct,ipaddress,json,argparse
def checksum(b):
 if len(b)%2:b+=b'\0'
 n=sum(struct.unpack('!%dH'%(len(b)//2),b))
 while n>>16:n=(n&65535)+(n>>16)
 return (~n)&65535
def inspect(path,mtu,header):
 if not 28<=mtu<=65535 or header not in range(20,61,4) or mtu<header+8:raise ValueError('MTU28-65535/header20-60in4byteunits and room for echo required')
 raw=Path(path).read_bytes();offset=24;rows=[];requests={};pairs=[];orphans=[];errors=[]
 if len(raw)<24 or struct.unpack('<IHHIIII',raw[:24])!=(0xa1b2c3d4,2,4,0,0,65535,1):raise ValueError('fixed classic PCAP required')
 while offset<len(raw):
  if offset+16>len(raw):raise ValueError('record header truncated')
  sec,usec,size,orig=struct.unpack_from('<IIII',raw,offset);offset+=16
  if size!=orig or offset+size>len(raw) or usec>=1000000:raise ValueError('record truncated/invalid')
  frame=raw[offset:offset+size];offset+=size
  if len(frame)<42 or frame[12:14]!=b'\x08\x00':raise ValueError('Ethernet IPv4 required')
  ip=frame[14:];data=ip[20:]
  if ip[0]!=0x45 or ip[9]!=1 or int.from_bytes(ip[6:8],'big')&0x3fff:raise ValueError('fixed IPv4ICMP/nonfragmented subset')
  if len(ip)!=int.from_bytes(ip[2:4],'big') or checksum(ip[:20]) or checksum(data):raise ValueError('length/IP-or-ICMP-checksum')
  src=str(ipaddress.IPv4Address(ip[12:16]));dst=str(ipaddress.IPv4Address(ip[16:20]));t,c=struct.unpack('!BB',data[:2]);i=len(rows)+1
  row=dict(frame=i,source=src,destination=dst,type=t,code=c,time_us=sec*1000000+usec)
  if t in (0,8) and c==0:
   ident,seq=struct.unpack('!HH',data[4:8]);row.update(identifier=ident,sequence=seq,data_bytes=len(data)-8)
   key=(src,dst,ident,seq)
   if t==8:
    if key in requests:raise ValueError('ambiguous repeated request key outside subset')
    requests[key]=(i,row['time_us'],data[8:])
   else:
    key=(dst,src,ident,seq)
    if key not in requests:orphans.append(i)
    else:
     n,ts,payload=requests.pop(key)
     if row['time_us']<ts:raise ValueError('reply time precedes request')
     pairs.append(dict(request_frame=n,reply_frame=i,elapsed_us=row['time_us']-ts,payload_equal=payload==data[8:]))
  elif (t,c)==(3,3):
   q=data[8:]
   if len(q)!=28 or q[0]!=0x45 or q[9]!=17 or checksum(q[:20]):raise ValueError('fixed quotedIPv4+UDPheader required')
   sport,dport=struct.unpack('!HH',q[20:24]);errors.append(dict(frame=i,quoted_protocol=17,quoted_source_port=sport,quoted_destination_port=dport,quoted_source=str(ipaddress.IPv4Address(q[12:16])),quoted_destination=str(ipaddress.IPv4Address(q[16:20]))))
  else:raise ValueError('unsupported ICMP type/code')
  rows.append(row)
 return dict(frames=len(rows),packets=rows,pairs=pairs,orphan_reply_frames=orphans,unanswered_request_frames=[x[0] for x in requests.values()],errors=errors,ipv4_echo_data_limit=65535-header-8,mtu_echo_data_limit=mtu-header-8,assumed_mtu=mtu,assumed_header=header,actual_path_mtu_verified=False,actual_network_test=False,incident_verdict='unresolved',external_actions=0)
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('pcap',type=Path);p.add_argument('--mtu',type=int,default=1500);p.add_argument('--ip-header',type=int,default=20);a=p.parse_args()
 try:print(json.dumps(inspect(a.pcap,a.mtu,a.ip_header),indent=2));return 0
 except (OSError,ValueError,struct.error) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
