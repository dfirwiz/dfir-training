둘째 날15강 자체 가상 자료입니다. 실제 캡처·DHCP서버로그·원본워크북이 아닙니다.
Python3 표준라이브러리만 사용합니다. 이 폴더에서:
python inspect_dhcp.py dora.pcap
python inspect_dhcp.py missing-ack.pcap
python correlate_lease.py leases.json
PCAP은 오프라인에서 만든4프레임/3프레임이며 Ethernet/IPv4/UDP체크섬이 있습니다. 주소는문서용, MAC은 자체로컬관리값입니다.
실제망으로전송하거나DHCP서비스를실행하지않습니다.4메시지일치는실제단말설정·소유자·업무승인의확인이아닙니다.
읽기범위는 고정 little-endian classicPCAP/Ethernet(noVLAN)/비분할IPv4/UDP67-68/옵션오버로드·중복옵션없음/한교환의Discover-Offer-Request-ACK입니다. pcapng·IPv6·VLAN·릴레이교환·옵션전체·재전송상태기계의일반분석기는아닙니다. 지원밖오류2를실제망공격으로해석하지마세요.
leases.json은 별도로쓴교육가정이며PCAP에서자동추출한전체임대장부가아닙니다. start<=시각<end의반열린구간,정확한scope일치만사용합니다.
결과0후보는제공기록안에서없다는뜻이며실제단말부재가아닙니다.복수후보는모호함으로남깁니다.시간오차·NAT·IPv6·수집권위·실제소유자검증은별도입니다.
종료0은로컬계산완료,2는도구지원범위/자료오류입니다. 실제사건판정unresolved/외부행동0입니다.
