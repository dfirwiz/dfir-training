둘째날17강 자체 가상 경로 비교입니다. 실제 SSH설정·로그·PCAP·원본워크북이 아닙니다.
이폴더에서 python map_routes.py cases.json (Python3표준라이브러리만사용)
프로그램은입력파일을읽고출력만합니다. SSH/소켓/리스너/원격접속/포워딩/방화벽변경을수행하지않습니다.
local은SSH클라이언트쪽리스너/서버쪽대상연결,remote는서버쪽리스너/클라이언트쪽대상연결이라는가정의역할을나눕니다.
127.0.0.1의대상은대상연결을시도하는호스트의루프백입니다.0.0.0.0리스너가정은모든IPv4인터페이스라는뜻이며인터넷노출검증이아닙니다.
unknown이면전달종류·대상·경로가용성을null로남깁니다.포트22통신만으로포워딩을만들지않습니다.
지원범위는IPv4/고정TCP local-remote두모형뿐입니다.실제설정문법·IPv6·DNS·SOCKS·X11·명령행파싱·일반SSH상태기계를구현하지않습니다.
modeled_path_available는입력의forwarding_permitted_in_fixture와target_reachable_in_fixture의AND일뿐입니다.실제권한·라우팅·포트존재·인증·업무승인을검증하지않습니다.
출력의actual_ssh_verified/actual_forwarding_verified는항상false,public_exposure는unverified/사건unresolved/외부행동0입니다.종료0은로컬계산완료,2는입력/지원범위오류입니다.
