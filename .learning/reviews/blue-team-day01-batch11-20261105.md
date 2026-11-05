# 첫째 날21·22강 범위와 검증

작성·공식자료확인일2026-11-05. CURRENT-COURSE-WORK.md·SOURCE-MATERIALS.md·editorial/progress/course.json·batch10검토와최신main을읽었다. no active_batch/첫째날1~20완료를확인한뒤21/22를예약했다. 원격a7ae6321053547950a2ae737b132b428171774d1의다른과정62파일변경은fast-forward로보존했다. 원래별도dfir-training의미커밋작업은건드리지않았다. 집필중다음시간heartbeat가도착했으나같은배치를계속했고다음23/24의중복실행을시작하지않았다.

## 원문 범위·대응·미완료

원본1권 인쇄161~167/PDF163~169를실제pypdf로다시열어전부읽었다. private tmp/day1-cases-source.txt. 이번완료범위는161~163/PDF163~165이고164~167은읽기만한미완료범위다. 인쇄161/PDF163을Poppler로렌더해시각확인했다(원문폰트대체경고있음,시각/추출교차확인). 원문문장·PDF·화면·추출전문은공개하지않는다.

| 인쇄/PDF | 학습항목 | 독립강의·예제대응 |
|---|---|---|
| 161/163 | Mirai기회형사례·코드공개/파생·IoT/NAS/DVR/카메라·약점/기본암호·작은장치합산 | 21강1~7·11~16절·그림1/2/3. 정상기능과비인가활동/원계열과변형/장치와주소수/노출·시도·인증·실행·영향구별 |
| 161/163 | 광범위스캔·취약점탐색(Log4j)·DDoS·스팸·사기·자원악용 | 21강6~13절. 필터2개설명/수집·응답·재조립한계·합계200Mbps/25MBps·150상한. Microsoft당시Log4j관측과Intel471당시관측분리. 원문의‘현재수백만’을2026실측으로반복하지않음 |
| 162/164 | Colonial연표·접근/VPN계정·단일요소·계정미폐기·자료절취·중단과대중/운송영향 | 22강1~9·11~12·18~19절·그림1. 원문2020을공식2021로수정. 4월29=당시식별한가장이른증거/실제최초구별. 자격증명획득경위미확인/유출구매·재사용단정안함. 100GB=공개발언/자체패킷검증아님 |
| 162/164 | 중단/복귀·물리적검사·연료부족/항공·가격/불안의파급 | 22강2·6~8절·그림1/2. IT위협에대한운영중단/OT직접감염구별. 5월12서비스복귀시작/13일공급상태발표/완전정상화구별. 29,000마일=차량점검이동거리,배관길이아님. 주유소87%·사상가격같은범위미대조수치를확정값으로옮기지않음 |
| 163/165 | 6월7일자금압수·63.7/75비트코인·당시USD·개인키 | 22강10절. DOJ발표직접대조,키보유/거래추적/암호깨기구별. 자체84.9%근사자산단위비율과다른시점가격/전체피해회복구별. 지급권고·거래·키접근없음 |
| 162~163/164~165 | 공개사건을조사흐름에연결 | 22강11~17절·그림3·lab22. 독립가상4이벤트/시간대·구간·순서·인과/결정·실제효과구별. 실제사건자료재현아님 |

Conti164~165·SolarWinds166·모듈정리167은다음23/24로남긴다. 소스에나온공격명령을실행하지않았다. Conti유출날짜·SolarWinds발견/공개일·GoldenSAML‘최초’·계열명관련성은다음집필에서1차자료대조필요. 이번완료로앞당기지않음.

D:/SANS/SEC450와PDF2022목록(5권·복제본·docx)·관련대화/진행기록을확인했다. 별도원워크북/가상위키/VM/원본사건PCAP는이접근범위에서확보·실행하지않았다. 전시스템자료부재로단정안함. 자료역할은본교재=범위,공개1차자료=사실/현행검증,독립lab=원리실습이며원본실습완료를주장하지않는다.

기존d1-14c를21강Mirai로구체화했고새22=d1-14dColonial,23=d1-14eConti,24=d1-14fSolarWinds를추가했다. 기존복습d1-15와실습d1-16은25/26강으로이동. 공개26강번호·ID·URL·본문유지. 진행완료는배포검증전까지1~20을유지한다.

## 1차근거·현행보충

확인일2026-11-05. 현재수치·버전·권고를과거사건과섞지않음.

- DOJ2017 Mirai https://www.justice.gov/archives/opa/pr/justice-department-announces-charges-and-guilty-pleas-three-computer-crime-cases-involving :2016계열·IoT·코드공개·다른주체변형. 오늘감염수/동일운영자주장아님.
- CERT-In https://www.csk.gov.in/alerts/mirai.html :2016발행/2017갱신의기본/고정자격증명·메모리/재감염·다른포트변형. 모든현재변형/재부팅치료규칙으로확대안함.
- Intel471직접연구 https://www.intel471.com/blog/iot-cybersecurity-threats-mirai-botnet :2022-01-25및2020~2021자체관측,판매/파생. 원문의Log4j근거로이페이지에없는내용을귀속하지않음.
- Microsoft직접관측 https://www.microsoft.com/en-us/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/ :Mirai등기존봇넷의Log4j이용추가. 과거보안패치버전을오늘최신으로옮기지않음.
- Wireshark https://www.wireshark.org/docs/dfref/t/tcp.html 및 https://www.wireshark.org/docs/man-pages/wireshark-filter :tcp.flags.syn/ack, tcp.dstport, 논리&&/||/괄호. 필드버전문서1.0.0~4.6.9범위확인,4.6.9를영구최신으로안함. 표시/캡처·줄수/세션/성공·IPv4/TCP/방향·포트의한계설명. 실제Wireshark/parser/PCAP실행없음.
- NISTIR8259A https://csrc.nist.gov/pubs/ir/8259/a/final 및 https://nvlpubs.nist.gov/nistpubs/ir/2020/NIST.IR.8259A.pdf :2020-05장치기본능력6관점·적용맥락/제조자/통합/사용자출발점. 모든제품지원/의무/완전예방보장아님.
- DOE https://www.energy.gov/ceser/articles/ceser-2021-emergency-response-recap 및 https://www.energy.gov/ceser/colonial-pipeline-cyber-incident :2021-05-07 IT위협대응선제중단,5월10FBI DarkSide발표,13일재시작/공급상태정리. 본문5월12복귀시작은아래하원증언대조.
- 상원2021-06-08 https://www.govinfo.gov/content/pkg/CHRG-117shrg46569/html/CHRG-117shrg46569.htm :특정옛VPN단일요소/복잡암호,그조사시점OT증거미확인,100GB발언의수준. 실제계정·사람·전체망직접검증아님.
- 하원2021-06-09 https://www.govinfo.gov/content/pkg/CHRG-117hhrg45085/html/CHRG-117hhrg45085.htm :조사자당시최초증거2021-04-29,옛VPN/일회용코드요구없음,자격증명획득경위조사중,5월12저녁복귀시작,29,000마일차량검사이동. 연도·배관길이오독교정.
- DOJ2021-06-07 https://www.justice.gov/archives/opa/pr/department-justice-seizes-23-million-cryptocurrency-paid-ransomware-extortionists-darkside :63.7비트코인압수·약75지급·공개원장추적·개인키보유. 당시달러/전체회복/암호체계깨기와구별. 발표하지않은키취득수단만들지않음.
- NISTSP800-63B-4 https://csrc.nist.gov/pubs/sp/800/63/B/4/final 및 https://pages.nist.gov/800-63-4/sp800-63b.html :2025-07확정/이전63B대체,요소/인증보증/피싱저항성·적용목적,단일MFA체크/세션전체안전보장안함.
- USENIX/Google연구PDF접근실패,회사옛colpipe페이지404,FBI직접페이지timeout. 우회/전체읽기주장안함. 공개DOE/Federalhearing/DOJ직접접근범위로근거정리.

## 실제실행과제한

Python3.12.14. 자체lab22 events.json/review_time.py/README.txt/field-notes.txt, training-time-v1. 가상2026-11-01의4이벤트/출처.example,Colonial기록/제품API아님. 16회실행과4입력SHA256불변확인. 보고 tmp/day1-case-check/actual-check.json.

- 기본vpn/endpoint:20초명목차,08:59:30~09:00:30/08:59:50~09:00:50겹침40초,순서미해결.
- decision/paused:120초명목차·범위09:04:55~09:05:05/09:06:55~09:07:05,엄격시간before/여유110초. 반대지정after. 같은기록은미해결.
- 추가오차60초:각65초범위09:03:55~09:06:05/09:05:55~09:08:05,10초겹침/미해결. 실제시계/입력변경아님.
- +09오프셋동일시각은기본결과와동일. 두구간끝점접촉은미해결,1초더떨어지면before.
- 없는ID/음수extra/boolean오차/시간대없음/중복ID/출처누락/불가능날짜/깨진JSON오류2. 미해결정상종료0과구별.
- 모든정상결과causationnot_tested/real_incidentnot_analyzed/external_actions0. 출처진실/원본증거/인과/상관/동일세션판정아님.
- 자체산술400×0.5=200Mbps,÷8=25MB/s,1000×0.2=200Mbps,공유구간단순상한min200/150=150Mbps,63.7/75×100≈84.9%. 실측트래픽/성능/피해회복률아님.
- 실제카메라/장치설정·재부팅·봇넷·스캔·공격·부하·VPN·계정/MFA/세션·OT/공정·지갑/금전·API/외부조회·VM/PCAP·악성코드실행·설치/구매없음.

## 구성과검증

21강18절/64문단/표1/SVG3/즉시복습12. 22강20절/71문단/표2/SVG3/즉시복습12. 합38절/135문단/표3/SVG6/즉시해설24.

HTML30구조/중복ID/내부앵커/상대링크/실제다운로드href/6일메뉴/첫째날1~26번호/28공개·22첫째날/기존26본문일치/다른홈내용일치검증통과. 인라인별표/지수/코드강조회귀유지,lab22허용링크·LF추가. 공개원과정식별자없음.

SVG6 XML/한국어폰트경계[]·정적접촉시트 output/network-security/case-studies-contact-sheet.png 시각검토. 읽는방향·범례·단위·실측아님표시/400폭/표와코드내부스크롤유지. CUA브라우저목록재확인[]로실제브라우저/모바일미검증,우회없음.

배포와공개42파일(HTML30/CSS/course.json/SVG6/실습4)의HTTP응답·내용일치후에만완료진도를갱신한다. 현재검토원고시점은게시대기다.
