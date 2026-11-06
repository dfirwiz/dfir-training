# 둘째 날15·16강 — 원문 대응·실제 검증 2026-11-07

## 자료와 범위

사용자가 재지정한 5권·SOURCE-MATERIALS.md·CURRENT-COURSE-WORK.md·진도·목차·직전회차검토/집필지침과 최신main6baa552를 확인했다. active_batch없음/첫째날26·둘째날14공개/총40강이었다. 지정D:/SANS/SEC450에는5PDF와PDF2022관련폴더가있고 이전기록의중복본·docx/워크북조사범위를확인했다. 별도원본워크북·위키·VM·사건PCAP를이번에획득·실행한것은아니다. 접근범위와미확인자료를구별하며기기전체부재라고단정하지않는다.

2권은182PDF쪽이다. 인쇄161~176/PDF163~178의16쪽을실제로열어완전히읽었으며출력은잘리지않았다. private tmp/day2-protocol-source/batch05-read-ahead.txt에보존. 이중이번완료는161~168/PDF163~170의8쪽뿐이며169~176은다음회차계획을위한읽기다. 인쇄165/PDF167(DHCP)·168/PDF170(SMB)그림을Poppler로비공개렌더해실제로보았다. Symbol/ArialUnicode대체경고가있었고텍스트와대조했다. 원문PDF·그림·추출전문은공개하지않는다.

추가프로토콜161~176을한강으로얕게요약하지않기위해미공개만분할했다. 공개1~14/첫째날1~26의번호·ID·URL·본문·표시업데이트날짜를보존한다. 새15=numericID10/DHCP,16=d2-10b/SMB. 다음17=d2-10c/SSH·RDP·VNC·PowerShell169~172,18=d2-10d/FTP·ICMP·원격도구·통신기준173~176은잠정이며다음실행에서다시열고깊이에맞춰미공개만세분한다. 이전미공개summaryID11→19/emailworkbookID12→20,현재둘째날계획20이다. 별도실습179~180을완료처리하지않는다.

## 학습 항목 대응

| 인쇄/PDF | 학습 항목 | 독립 강의의 절·예제·수정 |
| --- | --- | --- |
|161/163|과정전환·추가프로토콜범위|15절1/16절1및목차.원문식별자는공개하지않음|
|162/164|DHCP·SMB·다른원격관리/전송개요|15·16상세화.나머지169~176은다음17/18계획에남기며완료가아님|
|163/165|IP→단말이름→소유자;비인가장치;이름목록·OUI|15절1~2·10~14·17·19/가상장부Q1~Q4/그림3.당시시각·scope·자기주장·자산대조·NAC와DHCP구별|
|164/166|이름·MAC복제/실수탐지·불완전성|15절12~13/실제48비트6옥텟vs원문8옥텟사례수정.지역관리·무작위MAC정상가능/등록주체≠소유자|
|165/167|UDP67/68/DORA/복수Offer/요청·승인/임대|15절3~9·14~18/그림1·2/자체4프레임+ACK없는3프레임.브로드캐스트목적지오타·Offer0.0.0.0고정·서브넷불일치그림을그대로재현하지않음.선택은항상첫Offer가아님/상태·ciaddr·giaddr·플래그·갱신·릴레이차이|
|166/168|SMBWindows/Samba·445/파일공유/원격관리·공유관리암호|16절1~5·10~13·21/그림1.일반공유는관리자필수아님,SMB파일접근≠원격명령내장.자격증명·권한·경로·승인조건/LAPS|
|167/169|CIFS/SMB1·2·3/판본협상·SMB1제거·SMB2권고|16절6~10/역사비교표/클라이언트제시와서버선택/3.1.1정확표기.공유스택때문에SMB2활성화스위치가SMB3도영향,적용판본에맞는min/max기능.서명·암호화·QUIC/역할기본값보충|
|168/170|피싱발판→자격증명/서비스취약점두경로/차단·확산·후속탈취|16절11~21/그림2·3/6자체가상주장.관리자·포트·같은암호조건을자동전면침해로단정않음;MS17-010역사범위·모든로그인사용자평문암호항상획득아님.로그온/공유/서비스설치/프로세스/원인·승인분리|

## 현재 1차 출처 확인일2026-11-07

- [RFC2131](https://www.rfc-editor.org/rfc/rfc2131.html),[RFC2132](https://www.rfc-editor.org/rfc/rfc2132.html):초기선택·응답목적지·필드·옵션·타이머/상태.주소제안yiaddr≠IP목적지,항상같은DORA형태아님.프로토콜기본과자체범위실습을구별.
- [RFC6842](https://www.rfc-editor.org/rfc/rfc6842.html):클라이언트식별자서버응답갱신.예제옵션61반환. [RFC3046](https://www.rfc-editor.org/rfc/rfc3046.html):릴레이옵션82/관리신뢰를함께확인,이번자료에는없음.
- [MicrosoftDHCP](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top):주소·설정자동관리/적용범위. [IEEE식별자지침](https://standards-support.ieee.org/hc/en-us/articles/4888705676564-Guidelines-for-Use-of-Extended-Unique-Identifier-EUI-Organizationally-Unique-Identifier-OUI-and-Company-ID-CID),[RFC9724](https://www.rfc-editor.org/rfc/rfc9724.html)(2025년3월):48비트/조직접두/지역관리·무작위주소.제조사·사람인증과구별.
- [WiresharkDHCP](https://www.wireshark.org/docs/dfref/d/dhcp.html),[BOOTP](https://www.wireshark.org/docs/dfref/b/bootp.html):dhcp.id/hw.mac_addr/option.dhcp등3.0.0~4.6.9,구형bootp1.0.0~2.6.20.세필터는문서대조예시이며실제Wireshark실행아님.
- [SMB개요](https://learn.microsoft.com/en-us/windows-server/storage/file-server/file-server-smb-overview),[협상·세션·공유장애](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/negotiate-session-setup-tree-connect-fails),[판본관리](https://learn.microsoft.com/en-us/windows-server/storage/file-server/manage-smb-dialects):3.1.1·최고상호판본/정책·Win11 24H2/Server2025최소최대기능. [공유스택](https://learn.microsoft.com/en-us/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3):SMB2/3활성화관계.
- [서명상세](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-signing):Win11 24H2Enterprise/Pro/Education송수신/Server2025송신/Home동일기본요구아님.소개·요약페이지일부는Server2025도양방향이라고넓게쓰므로상세문서의정확범위를우선하고실제설정대조. [보안](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-security):서명과암호화별도. [QUIC](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-over-quic):서버적용에디션/클라이언트/기본UDP443/TLS1.3/관리활성화,TCP445노출과구별.
- [PsExec](https://learn.microsoft.com/en-us/sysinternals/downloads/psexec),[MS17-010](https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010),[LAPS](https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-overview):관리도구·서비스관계/2017SMBv1범위와현재패치구별/암호관리적용.실제실행·보호설정변경없음.
- Microsoft감사 [4624](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4624),[5140](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-5140),[5145](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-5145),[4697](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4697),[4688감사조건](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/component-updates/command-line-process-auditing):타입3네트워크로그온은SMB전용아님/공유검사vs전송/설치vs실행/감사·명령줄누락/대상단말범위ID.일부구형URL오류는공식previous-versions로직접열어내용확인.페이지상단인증안내가있어도본문은실제열람됨.
- [WiresharkSMB2](https://www.wireshark.org/docs/dfref/s/smb2.html):프로토콜표기1.0.0~4.6.9.2필터는미실행.네트워크단독관측의암호화·재조립·포트/전송한계.

## 실제 수행한 계산·패킷 검증

Python3.12.14/표준라이브러리프로그램,기존private tmp/lab-deps의dpkt1.9.8로독립교차해석(새설치없음). root check_day02_batch05_examples.py는38회프로세스실행,9개공개입력/프로그램/README의실행전후SHA256동일을확인했다. private tmp/day2-protocol-check/actual-check.json에모든출력/오류/해시저장. 자체생성기는네트워크소켓을쓰지않으며재현가능하게scripts/build_dhcp_evidence_lab.py에있다.

DHCP4프레임Discover/Offer/Request/ACK,UTC09:00:00~03,UDP68→67/67→68,전부브로드캐스트목적지,제안/요청/승인192.0.2.25/서버192.0.2.1/임대3600초. xid0x45000001/chaddr02:00:00:00:00:25/client-ID01020000000025대응. IPv4/UDP길이·체크섬및독립dpkt4프레임옵션/주소확인. ACK없는3프레임은관측부재/완료조건false,실제임대실패단정아님. 재정렬·다른xid의ACK·ACK주소변경·재전송추가로단순4순서일치조건의한계를확인. 잘못된IP/UDP체크섬·잘린레코드·VLAN/형식미지원·옵션길이·중복·end부재는도구오류2. 일반DHCP전체파서가아님.

가상장부Q1a/Q2b경계/Q3다른scopec/Q4없음. 겹친구간→ambiguous,동등+11시각→같은a,범위없음/임대전시각→후보없음.시차없는시각·잘못된구간·IP·client·입력계약거부. start≤시각<end는자체규칙이고실제서버로그의모든만료의미와같다는주장없음.

SMB주장C1인증없음/C2공유조건/C3서비스+프로세스후보/C4다른서버연결실패/C5설치만/C6동일조건승인가정변경. 다른공유ID·늦은서비스/프로세스·역순프로세스·이미지/대상변경·로그온타입변경을비교.필수ID없음/시간대없음/포트오류/승인자료형/계약오류는오류2.120초는자체가정,같은시간·경로≠실제인과관계. flow와실제단말대응/Windows로그파싱/SMB프로토콜/원격실행원인은확인하지않음. 모든실제인증·사건결론미확인/외부행동0.

## 정적·시각 검증 및 한계

42절/153본문문단/3표/6자체400pxSVG/바로읽는복습해설30문항. builder로42공개강의/총44HTML갱신. HTML태그구조·중복ID·상대링크·앵커·날짜별메뉴·번호·다운로드·강조/코드회귀·기존40본문및업데이트표시/다른홈영역의동일성을확인했다. 축약레드팀홈4주제카드유지. code·표내부가로스크롤/이미지width100%는기존CSS에서정적확인.

render_protocol_evidence_figures.py의실제Malgun글꼴경계검사FONT BOUNDS []와6그림모음이미지육안확인. DORA그림은역할방향/브로드캐스트목적지구분,다른도식은조사순서·시간단위·판단한계범례를표시. 현재CUA신선한목록browsers=[]/Work설정상로컬브라우저사용중지. 우회하지않았고completion_summary를보냈다. 실제브라우저·모바일레이아웃은미검증이며정적검증을그것으로표현하지않는다.

실제DHCP/SMB서버·서비스·스캔·PCAP캡처·Windows감사로그분석·원격도구·자격증명수집·정책변경·워크북/VM실행은수행하지않았다. 게시·배포성공·공개HTTP응답/내용일치후에만진도를완료로바꾼다. 전체과정은미완료/자동화로컬유지/클라우드이전미확인/다른자동화변경없음.
