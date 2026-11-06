둘째날20강 자체 오프라인 FTP자료입니다.실제FTP서버·캡처·사건·원본워크북이아닙니다.사용자·암호도모두가짜교육값입니다.
이폴더에서 python inspect_ftp.py ftp-complete.pcap expected-note.txt
다음은 python inspect_ftp.py ftp-missing-data.pcap expected-note.txt
Python3표준라이브러리만사용하며캡처와참조를읽고출력만합니다.네트워크전송·인증·파일실행·복원파일쓰기·FTP접속없음.
PCAP은13/12개의payload TCP세그먼트로만들었습니다.3-way handshake/FIN/실제FTP세션전체는없습니다.Ethernet/비분할IPv4/TCP체크섬검증과고정한개EPSV/TYPE I/STOR교환의작은재조립만지원합니다.
지원밖:pcapng/VLAN/IPv6/IP-TCP옵션/부분겹침/복잡한세션/FTPS/다중전송/다른주소·명령/완전한FTP응답상태기계.서버클라이언트제어방향은완전해야하며gap이면도구오류2,데이터gap은관측prefix와gap표시로남깁니다.
캡처시작이늦어첫바이트가없으면이부분집합은TCP기준점을독립확인하지못합니다.참조파일은별도로만든15바이트가정이며FTP의전송길이를항상아는것이아닙니다.
서버226주장과수집바이트·참조일치는다른근거입니다.데이터가9바이트만보이는파일에도226은남겨놨습니다.부족6바이트/일치null로표시하며실제서버전송실패라고단정하지않습니다.
출력의PASS는가상값도마스킹합니다.공개PCAP의가상암호를실제인증정보로사용하지마세요.참조SHA256/바이트일치도실제서버파일저장·유출·악성여부확인은아닙니다.
실제인증/저장검증false/사건unresolved/외부행동0.종료0은분석완료,2는입력/도구지원범위오류입니다.
