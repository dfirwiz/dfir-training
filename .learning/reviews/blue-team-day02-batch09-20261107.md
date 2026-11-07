# 둘째 날23·24강과 최종 범위 대응 점검 — 2026-11-07

## 시작 상태·자료 확인

CURRENT-COURSE-WORK.md/SOURCE-MATERIALS.md/집필 지침/진도/course.json/직전batch08 검토와 최신main3c07e80eb0b43d97227b7274ea8abc9c0c13bb45를 읽었다. active_batch없음/첫째날26·둘째날22/48공개강의. 깨끗한dfir-training-menu에서 이어갔으며 원래dfir-training의 다른 수정은 건드리지 않았다. 지정 다섯PDF/관련PDF2022/이전 워크북 조사 기록/기존 자체lab12를 확인했다. 별도 원본워크북·가상위키·VM·사건PCAP·수신서버로그를 이번에 확보·실행하지 않았다. 모든 저장장치에 자료가 없다는 주장은 하지 않는다.

지정2권 인쇄177–180/PDF179–182의 마지막4쪽을 실제 전부 다시 읽었다. 비공개tmp/day2-final-source/batch09.txt. 인쇄178종합정리와180별도실습안내를Poppler로 비공개렌더하여summary-180.png/workbook-pointer-182.png를 실제 보았다. Symbol/ArialUnicode 경고를 텍스트와 대조했다. 원문PDF·화면·추출전문·원문지시문은 공개/실행하지 않았다.180은 별도워크북/위키로 가라는 포인터뿐이며 원래 문제/데이터/정답은 본PDF에 없다는 범위를 확인했다.

추가로2권앞부분의표지·목차·로드맵·개요를 확인했다. 법률문서를 새 실행지시로 취급하지 않았으며 전체 라이선스를 이번에 완독했다고 주장하지 않는다.3권PDF1–8의목차·개요·첫주제머리부분만 다음범위선택용으로 확인했으며 부분추출(쪽당최대900자)이다.3권학습완료/새회차완료로 세지 않는다. 다음 시작은3권인쇄5/PDF7;5–27단말공격전술을 실제읽고 미공개만 깊이에맞춰 분할해야 한다.

## 이번 학습 항목 대응

| 인쇄/PDF | 본 교재 역할 | 독립 강의와 확인 |
| --- | --- | --- |
|177/179|네트워크 범위 로드맵|23절1·16, 기존22강·목차와연결. 원래식별자공개없음.|
|178/180|구조·구간·흐름·통제·수집위치와유형|23절2–4/그림1·2/비교표/가상경로·센서시간. 설치와실제기록보존/흐름vs내용vs실행 구별.|
|178/180|메일발판→서버이동→중간저장→외부전송에서무엇을볼수있나|23절3–4·8–14/그림3/S1–S6. 경로·시각·종류별부족근거/직접사실·가설·추가자료. 인과·실행·유출성공을자동완성하지않음.|
|178/180|DNS·HTTP(S)·SMTP우선·발신인증/헤더|23절5–8/24절5–15. 이름조회≠방문,요청·응답·바이트≠실행,암호화구간가시성,메일수락vs행동,검사신원·보고출처·정렬분리.|
|178/180|기타프로토콜·단말학습전환|23절9·15–16/24절16. DHCP주소단서/SMB접근vs명령/SSH-RDP-VNC-PSRP-RMM보호신원승인/ICMP·FTP구조를이전상세강의와연결. 네트워크한계를단말·파일·계정조사질문으로전환.|
|179–180/181–182|별도SMTP·이메일분석워크북/위키안내|24절1–17. 원본별도실습미수행을명시하고자체EML2/context/로컬읽기/시간4초/발신주장·수신책임·결과보고출처·엄격정렬조건연습으로연결. 원래문제·정답재현없음.14즉시Q&A.|

## 둘째 날 전체 개념 범위 점검

이 점검은 기존 상세검토표batch01–08의 대응범위와22공개원고의절제목목록,이번177–180완독을 연결했다.5–176을이번턴에다시한글자씩전체정독한것은아니다. batch01의기존5–106누락대응표와batch02/03/04/05/06/07/08표를다시확인하고범위목록을비공개coverage-batchNN.txt/published-section-audit.json에보존했다. 최초절제목출력은cp949/과다출력으로잘렸으므로UTF8로다시수집해각강의제목·절개수22개를확인했다. 구조점검과실제원문재독범위를구별한다.

| 원문 인쇄 범위 | 공개 강의 | 개념 대응 |
| --- | --- | --- |
|1–4|과정안내·1/23강|표지·목차·로드맵·개요,독립기술누락범위아님|
|5–17|1|구조·구역·흐름·스위치/TAP/SPAN·방화벽·분리·신뢰|
|18–30|2|수집종류·요약·프로토콜·PCAP·도구·가시성|
|31–50|3|DNS기본·레코드·질의·응답·캐시·TTL|
|51–85|4|DNS조사·중계·정보보강·오용·관측한계|
|86–87|5|원본별도실습포인터/독립DNS실습,원본수행미확인|
|88–106|6|HTTP기본·메시지·메서드·헤더·자료/현대판본|
|107–116|7|HTTP분석·평판·도구·헤더·사용자에이전트·쿠키|
|117–123|8|인코딩·자료전달·파일·빈도·관측예외|
|124–129|9|공격흐름·리다이렉트·역사사례·행위/성공분리|
|130–136|10|TLS·복호화조건·프록시·인증서·지문·관측한계|
|137–138|11|원본별도실습포인터/독립HTTP·HTTPS연습|
|139–149|12|SMTP전달·명령·봉투·헤더·Received·시각|
|150–155|13|발신주장·SPF·결과보고·신뢰경계|
|156–160|14|DKIM·DMARC정렬·정책/조치·내용위험|
|161–165|15|DHCP·주소와단말·임대·불완전성|
|166–168|16|SMB·협상·보호·인증·접근vs실행|
|169–170|17|SSH·전달·역할·리스너·허용·관측|
|171|18|RDP·VNC·인증·세션·행위|
|172|19|PowerShell·PSRP·WinRM·보호/신원/권한|
|173|20|FTP제어·데이터·완료·수집·참조·승인|
|174|21|ICMP·Echo·오류·자료·크기·MTU|
|175–176|22|원격도구·기준·DPI·다층관측·외부정책|
|177–178|23|종합조사·범위·근거·공백·개선|
|179–180|24|원본별도실습안내/독립이메일근거실습|

5–180의176개인쇄쪽을서로겹치지않는24배정범위로검사했다. 개념에배정되지않은기술범위는이번점검에서발견되지않았다.86–87/137–138/179–180은독립대체실습과원본실습미확인을함께기록하며원본수행완료로조용히세지않는다. 전체과정은3–5권및종합실습이남아있으므로자동화를끄지않는다.

## 현재1차출처 — 확인일2026-11-07

- [RFC9846공식정보](https://www.rfc-editor.org/info/rfc9846/)/[실제읽은txt](https://www.rfc-editor.org/rfc/rfc9846.txt):2026-07TLS1.3문서/RFC8446대체. 이전10강의대조기록을확인하고이번23강에현재근거로연결.22강등의RFC8446보호목적설명은역사적근거로여전히맞지만현재전체명세와구별한다. 기존승인본문·표시날짜를임의변경하지않았다.
- [RFC8484](https://www.rfc-editor.org/rfc/rfc8484.html):DNS-over-HTTPS와일반DNS관측범위구별. [NIST800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final):사고대응과위험관리·개선연결. 실제조직통제인증아님.
- [RFC5321](https://www.rfc-editor.org/rfc/rfc5321.html):데이터뒤성공응답의수신책임vs최종배달/행동. SMTP5321bis는공식검색상진행문서이며새RFC번호를만들어완료표준처럼표현하지않음. [RFC5322](https://www.rfc-editor.org/rfc/rfc5322.html):메시지필드와추적구조. 기본역할범위로만사용.
- [RFC8601](https://www.rfc-editor.org/rfc/rfc8601.html):Authentication-Results/authserv-id/신뢰경계와외부위조보고. 이름·헤더위치만으로신뢰안함. [RFC7208](https://www.rfc-editor.org/rfc/rfc7208.html):SPF의봉투/연결검사신원. [RFC6376](https://www.rfc-editor.org/rfc/rfc6376.html):서명자와표시작성자구별. 실제조회/암호검증안함.
- [RFC9989](https://www.rfc-editor.org/rfc/rfc9989.html):2026-05/7489·9091대체,정렬된성공SPF또는DKIM/엄격과완화구별. 실습은엄격조건만고정하고DNS정책·조직도메인TreeWalk·수신판정미구현. [RFC9990](https://www.rfc-editor.org/rfc/rfc9990.html)/[9991](https://www.rfc-editor.org/rfc/rfc9991.html)은보고명세와구별,보고생성·전송없음. 제품별실제채택판은검증안함.
- Wireshark [IPv4](https://www.wireshark.org/docs/dfref/i/ip.html)/[SMTP](https://www.wireshark.org/docs/dfref/s/smtp.html)/[표시필터](https://www.wireshark.org/docs/man-pages/wireshark-filter.html):ip.addr/smtp.response.code1.0.0–4.6.9. 실제Wireshark실행·설치판검증아님.250은여러단계에서쓰이므로고립응답을데이터수락/사용자열람으로확대안함.

## 실제 자체 실행과 결과

8다운로드:lab23cases.json/map_evidence.py/README3;lab24EML2/context.json/inspect_email.py/README5. 새생성기scripts/build_network_final_labs.py는로컬가상자료만생성. Python3.12.14표준라이브러리34별도프로세스실행/8입력SHA256전후동일;설치없음. 비공개tmp/day2-final-check/actual-check.json. 독립rawCRLF·헤더개수·원문/문맥해시·실제DKIM서명없음·수동UTC4초계산도확인했다.

가시성기본S1수신보고/S2이름조회/S3TLS종류입력있음→좁은요구종류충족. S4프로세스/S5서버파일쓰기/S6파일신원빠짐→불충족. SMB흐름이나외부바이트종류가그근거를대신하지않음. 수집시작09:04/경로불일치/09:30끝경계로기록제외,동등+11시각동일,빈기록모두불충족,호스트종류·파일식별추가시해당조건만충족. 실제단계·센서검증은모두false. 잘못된계약·시간대부재·미등록센서·역전창·빈단계·중복단계ID·빈필수근거는도구오류2.

EML A작성자example.org/SPF보고mailer.example.net/DKIM보고example.org/수신자생성문맥가정true→보고기반엄격비교true. B는같은식별자·pass지만문맥가정false→null. 둘다Received4초/첨부0/실제DNS·서명·수신출처·SMTP/배달·사용자행동false. 실제유효DKIM서명·키가없는가상보고이므로실제pass를검증한것이아님.

문맥false/기대이름다름/다른헤더선택→null,가상B문맥참→계산만true;DKIMfail또는다른서명도메인/하위도메인엄격불일치→false;SPF정렬성공단독→true;서명도메인대소문자정규화→동일;데이터수락가정false여도정렬계산독립. 해시변경/중복From/인덱스범위/문맥자료형/미지원softfail/Received누락·잘못된시각은도구오류2. 프로그램은pass/fail/none의작은AR문법/단일작성자/2Received/엄격도메인비교만지원. DNS·암호검증·일반다중서명/MIME/SMTP상태기계·완화정렬·정책발견미구현. 해시일치≠진실·수신출처인증. 모든사건unresolved/외부0.

실제메일전송·DNS조회·링크열기·첨부실행·소켓·서버/계정/방화벽변경·원격접속·원본워크북/위키/VM·실제PCAP/메일로그수집은없음. 자기자료의조건계산·파싱결과와실제인증/공격판정을구별했다.

## 정적·시각·보존 검증

두강의34절/113본문문단/3표/6자체400pxSVG/즉시해설28문항. build_network_security.py로50공개강의/총52HTML생성. validate_day02_batch09.py로HTML구조·중복ID·상대링크·앵커·6날짜메뉴·번호/ID·다운로드·인라인코드·48기존본문과표시날짜·다른홈영역불변확인. 레드팀홈축약4주제/6링크와전체13장58강보존. git기본diff-check가-text보존EML의CR을후행공백으로표시하여CRLF를유지한채cr-at-eol조건으로다시검사했다. 실제공백검사는유지하며원문바이트를정규화하지않았다. 표·코드내부가로스크롤/그림width100%는정적CSS확인.

render_network_final_figures.py의Malgun폰트실측FONT BOUNDS []/6그림모음실제육안확인. 제목·흐름/질문방향·가상성·정렬범위·보고vs실제결과·단위표시. 신선한CUA목록browsers=[]/Work설정상브라우저사용중지,우회없이completion_summary전달. 실제브라우저/모바일화면·Wireshark·제품동작은미검증.

배포Actions성공과공개HTTP200/작성내용일치후에만둘째날24완료와개념범위점검결과를갱신한다. 다음셋째날1강으로번호를다시시작하며실제3권범위를읽고미공개를필요시세분한다. 전체과정미완료/로컬자동화유지/클라우드전환미확인/다른자동화변경없음.


## Verified publication result 2026-11-07

Publication 0433d3c2d61285b68fbc79bae9467fbf8cf9d27c; Actions 42337369104 completed/success. Public68resourcesHTTP200/contentmatch:52HTML/CSS/coursejson/6SVG/8downloads;2EMLexactCRLFbytes/othertextLFnormalized. Onlyafterproofadvancedday2display1–24/clearedactivebatch/recordedconceptualcoverageauditwithoriginalworkbookexecutionlimit.48previousbodies/datesandcompactredhomepreserved. Nextday3display1/2startsvolume3printed5/PDF7;actuallyread5–27andsplitonlyunpublishedfordepthbefore28–52defense. Browserdisabled/staticonly;actualDNS-SMTP-signature-receiver-provenance-useraction/workbook-VMunverified. Wholecourseunfinished/localautomationactive.
