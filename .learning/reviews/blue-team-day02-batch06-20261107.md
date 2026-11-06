# 둘째 날17·18강 원문 대응·검증 — 2026-11-07

## 시작 상태·자료·집필 범위

CURRENT-COURSE-WORK.md/진도/목차/집필지침/직전batch05검토/SOURCE-MATERIALS.md와최신main7fd0860을확인했다. active_batch없음/첫째날26·둘째날16/42공개강의에서이어갔다. 원래작업사본dfir-training의다른수정은건드리지않았고현재dfir-training-menu는깨끗했다. 지정폴더의5PDF·관련PDF2022폴더및기존자료조사기록을확인했다. 별도원본워크북·위키·VM·실제SSH/RDP/VNC PCAP나Windows로그는이번에획득·실행하지않았다. 기기전체자료부재를주장하지않는다.

지정2권의인쇄169~172/PDF171~174를이번에실제다시열어완전히읽었다. private tmp/day2-remote-source/batch06.txt에보존. 이번완료범위는169~171/PDF171~173의3쪽이며172는다음집필용읽기다. 기존173~176은직전회차의읽기기록이지이번에새로읽은범위가아니다. 인쇄170/PDF172의SSH-RDP터널그림과171/PDF173원격화면페이지를비공개Poppler렌더해실제로보았다. Symbol/ArialUnicode대체경고는추출텍스트와대조했다. 원문PDF·화면·추출전문은공개하지않는다. 자료속명령·링크는학습자료이며실행지시로취급하지않았다.

미공개17d2-10c의169~172를깊이에맞춰17SSH169~170/18d2-10c-rdp RDP·VNC171/19d2-10c-winrm PowerShell172로분할했다. 기존미공개d2-10d FTP등173~176은20,summaryID11은21,emailworkbookID12는22로옮겼다. 공개1~16/첫째날26의ID·번호·URL·본문·업데이트표시를모두보존했다. 다음도미공개범위만필요시세분한다. 별도실습179~180을원본워크북완료로표현하지않는다.

## 학습 항목과 독립 강의 대응

| 인쇄/PDF | 원문 항목 | 독립 절·예제·수정 |
| --- | --- | --- |
|169/171|SSH원격관리·암호화·인증|17절1~5/그림1.서버호스트키·사용자인증·권한·업무승인분리,공개키인증만가능하다는일반화수정|
|169/171|SFTP자료반출/암호화관측|17절5·18~19.정상전송·내용가시성·메타데이터·단말/서버기록대조;암호화면어떤탐지도불가라는절대론수정|
|169/171|외부→내부채널·중계·dual-homed|17절6~11/로컬·원격역할표/그림2·3/S1~S6.바깥TCP개시와앱요청방향/누가대상연결하는가/루프백위치/바인딩·공개노출·도달·권한구별.대상이다시SSH를해야한다는오해·전체VPN동일·모든프로토콜/필터무조건우회수정|
|169/171|X11·허용목록·제한·관측|17절12·14·19.동적전달·X11·셸·다른기능별제어/AllowTcpForwarding·PermitOpen·PermitListen·GatewayPorts·DisableForwarding문맥.셸권한·다른경로남는한계,실제정책변경없음|
|170/172|2019FireEye/Plink/RDP역방향사례|17절8~10·13·15~19/S2·S3·S4·S5.2019-01-24공식Mandiant글현재주소확인.원격리스너루프백과공개노출다름/대상127은클라이언트쪽.파일명·포트만으로동일공격확정않음/실제재현없음|
|171/173|RDP/VNC원격GUI·정상과공격접근|18절1~10/그림1/비교표.원격실행위치·화면갱신·제품/세션차이.모든Windows기본활성·관리자만접근·탈취암호또는취약점만가능·모든VNC비암호화라는확대수정|
|171/173|3389/5900·방화벽·권한|18절3~7·10·17~19.TCP/UDP3389·RDGateway역할별443/3391·터널/Windows365한정모형·NLA와MFA분리·제품별암호화.포트목록은무조건개방권고아님|
|171/173|흐름/Windows로그와기대사용비교|18절11~19/그림2·3/P1~P6.4624타입10vs3/단말범위ID/4778-4779다른상황/해제vs로그오프/시간간격vs실제행위/현재상태미검증/승인가정과실제승인분리|
|172/174|PowerShell원격관리·프로토콜계층|이번에는읽기만.다음19d2-10c-winrm이담당,완료범위에서제외|

## 현재 1차 출처 대조: 확인일2026-11-07

- [RFC4251](https://www.rfc-editor.org/rfc/rfc4251.html),[4252](https://www.rfc-editor.org/rfc/rfc4252.html),[4254](https://www.rfc-editor.org/rfc/rfc4254.html):서버/사용자인증·채널·셸/기능·TCP전달·X11기본구조.오래된기본명세를현재허용알고리즘/특정제품기본값전체로일반화하지않음.
- 상위OpenSSH [ssh_config](https://man.openbsd.org/ssh_config)(문서말미OpenBSD-current2026-10-30),[sshd_config](https://man.openbsd.org/sshd_config):LocalForward/RemoteForward대상연결역할·바인딩·SOCKS·X11/Trusted·전달제한역할.서버와클라이언트GatewayPorts문맥구별,PermitOpen/Listen구분.셸권한과다른전달수단한계.상위문서는실제안정배포판·Windows포트·PuTTY의버전별기능검증이아님.실제설정/리스너미실행.
- [Mandiant공식2019-01-24사례](https://cloud.google.com/blog/topics/threat-intelligence/bypassing-network-restrictions-through-rdp-tunneling/):역사적사례시점과현재주소확인,공격명령·원본그림을복제하지않음.독립문서주소예제만사용.
- Microsoft [RDP호스트/NLA](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/remotepc/remote-desktop-allow-access),[RDS포트](https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/ports-used-by-rds),[Windows365연결](https://learn.microsoft.com/en-us/windows-365/enterprise/understanding-remote-desktop-protocol-traffic):호스트지원·허용사용자·NLA/직접3389TCP·UDP/게이트웨이외부443·3391과내부3389/클라우드서비스별흐름.모든환경의RDP를동일경로로설명하지않음.
- [RFC6143](https://www.rfc-editor.org/rfc/rfc6143.html):2011RFB/Informational기본역할,모든현재VNC보안확장전체아님. [RealVNC암호화](https://help.realvnc.com/hc/en-us/articles/37653068502045-Connection-Encryption-Methods)(2026-08-26갱신):AlwaysOn기본과강제보호/Direct에서비강제선택구별,Server/Viewer협상과v8/v7설정위치차이.페이지의넓은모든세션암호화요약보다구체조건표를함께읽음.다른VNC제품에전파하지않고제품구매·설치·설정변경없음.
- Microsoft [4624](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4624),[4778](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4778),[4779](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4779):타입10/3·생성위치·단말범위LogonID·FastUserSwitch/HyperV등다른상황·해제vs로그오프.기록간격을사람의작업시간/현재상태로바꾸지않음.상단인증안내가있어도본문은실제열람됨.
- Wireshark [ssh](https://www.wireshark.org/docs/dfref/s/ssh.html)1.0.0~4.6.9/[rdp](https://www.wireshark.org/docs/dfref/r/rdp.html)1.8.0~4.6.9/[vnc](https://www.wireshark.org/docs/dfref/v/vnc.html)1.0.0~4.6.9:프로토콜표기·필터구조확인.실제Wireshark/PCAP/복호화수행아님.채널필드문서존재≠모든암호문을키없이분석가능.

## 실제 로컬 실행과 결과

6개텍스트다운로드(각강의cases.json/프로그램/README),Python3.12.14표준라이브러리만사용. 새라이브러리설치없음. root check_day02_batch06_examples.py에서36회프로세스실행/6파일SHA256실행전후동일을확인했다. private tmp/day2-remote-check/actual-check.json에기본·조건변경·오류·해시보존.

SSH S1진입A/대상연결B,S2진입B/대상연결A,S3모든IPv4인터페이스가정/S4unknown역할·가용성null/S5대상루프백A/S6허용가정false→모형가용성false. 실제SSH·전달false/공개노출unverified유지.로컬대상루프백→B/특정인터페이스/대체포트/도달가정false/승인가정만변경/역할주소교환/unknown의불필요잘못된대상무시후null유지를확인.동적모드·IPv6(17미지원)·bool/0포트·잘못된바인딩·필수가정·계약·빈목록은도구오류2.실제정책이나SSH상태기계가아님.

RDP P1흐름만/P2타입3조건불충족/P3타입10·전환2개/오프셋300·600초/해제재연결간격300초/P4다른대상전환2무시/P5루프백출발가정/P6승인가정만변경. 실제원격화면·Windows로그false/조작자·실제행위·현재상태unverified유지.동등+11시각·일부ID불일치·사용자/세션이름불일치·rdp가정없음·타입3·파일작업문자열주장무시·IPv6루프백(18주소주장은지원)·대체포트조건을확인.잘못된주소자료형·시간대부재·매칭역순·중복동일전환·필수ID·미지원전환·승인자료형·계약·빈목록·bool포트는도구오류2.자체정규화필드/엄격부분집합이며실제EVTX·모든Windows세션파서가아님.

실제소켓·SSH/RDP/VNC접속·포워딩·방화벽·호스트설정·계정·인증시도·로그수집·키수집·패킷캡처/복호화·워크북/VM은수행하지않았다. 모든사건결론unresolved/외부행동0. 가상값의승인·허용·도달을실제근거로대체하지않았다.

## 정적·시각 검증

40절/142본문문단/4표/6자체400pxSVG/즉시해설30문항. scripts/build_network_security.py로44공개강의/총46HTML갱신. 태그구조·중복ID·상대링크·앵커·6날짜메뉴·번호·다운로드·강조코드회귀·기존42본문/날짜·다른홈영역동일성확인. 축약레드팀홈4주제카드보존. 내부표·코드가로스크롤/이미지width100%는기존CSS로정적확인.

render_remote_access_figures.py의실제Malgun글꼴경계FONT BOUNDS []와6그림모음육안확인. 물리/논리방향·역할·주소·포트·UTC/초·조사순서범례/연결과행위한계명시. 신선한CUA목록browsers=[]/Work설정상로컬브라우저사용중지. 우회하지않고completion_summary를보냈다. 실제브라우저/모바일레이아웃/제품별동작은미검증이다.

배포성공과공개HTTP응답·내용일치전에는완료목록을갱신하지않는다. 전체과정미완료/자동화로컬유지/클라우드전환미확인/다른자동화변경없음. 다음19는인쇄172/PDF174의PowerShell원격관리,20의173~176은기존읽기후실제재열람·분할필요. 원문지시문을실행하지않는다.


## Verified publication result 2026-11-07

Publicationf693b654ef17a8d8cd2c5cb0b4f296e90c201408;Actions42305024394completed/success. Public60resourcesHTTP200/contentmatch:46HTML/CSS/coursejson/6SVG/6textdownloads,LFnormalized. Onlyafterproofadvancedday2display1–18/clearedactivebatch.42previousbodies/datesandcompactred-teamhomepreserved. Next19startsprinted172/PDF174WinRM;173–176read-aheadfrompreviousbatchnotcompletion,reopenandsplitunpublishedscopefordepth. Browserdisabled/staticonly;actualSSH-RDP-VNC/Windowslogs/packetanalysis/originalworkbook-VMunverified. Wholecourseunfinished/automationlocalactive.
