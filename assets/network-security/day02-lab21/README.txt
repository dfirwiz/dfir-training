자체 가상 PCAP6프레임입니다. 실제 ping·네트워크·사건·워크북 수행이 아닙니다.
Python3표준라이브러리로 로컬파일만 읽습니다: python inspect_icmp.py icmp-training.pcap --mtu 1500 --ip-header 20
Echo두쌍(내용동일1/의도적다름1),요청없는Reply1,UDP원래헤더를인용한type3/code3오류1. 오류속33434는인용UDP목적지포트이지ICMP포트가아닙니다.
고정classicPCAP/Ethernet/옵션없는IPv4/비분할ICMP부분집합. IPv6/VLAN/pcapng/재조립/중복요청키/다양한오류확장·실제호스트행동분석미지원. Ethernet주소도자체가상값으로방향에맞춰생성했으며실제호스트식별근거가아닙니다.
--ip-header는크기계산가정이며입력패킷옵션지원설정이아닙니다. --mtu는사용자가준계산가정이며경로측정결과가아닙니다.
다른내용의응답은모형의의도적변형이지실제공격관측이아닙니다.실제네트워크검사/경로MTU검증false,사건unresolved/외부행동0. 종료2는도구지원범위/입력오류.
