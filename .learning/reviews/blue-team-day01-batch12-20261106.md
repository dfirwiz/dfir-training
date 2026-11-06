# 첫째 날23·24강 범위와 검증

확인·집필일2026-11-06. CURRENT-COURSE-WORK.md·SOURCE-MATERIALS.md·editorial/progress/course.json·batch11검토와최신main을읽고active_batch없음/1~22완료확인후23/24를예약했다. 시작main bcdf7daba7af923639acc3a74c7a4fe84b9426ca의다른과정여러공개/그림/진행변경은fast-forward보존. 원래dfir-training의별도작업은초기화·덮어쓰기하지않았다.

## 원문학습항목대응

원본1권 인쇄164~167/PDF166~169를pypdf로실제다시열어전부읽었다. private tmp/day1-conti-solarwinds-source.txt. 인쇄166/PDF168은Poppler렌더·시각검토(원문폰트대체경고는추출과교차확인). 원문PDF·화면·전문·공격명령은공개/실행하지않는다.

| 인쇄/PDF | 학습항목 | 자체강의대응 |
|---|---|---|
| 164/166 | Conti플레이북·유출·상세절차와기술수준/진입장벽 | 23강1~3·19절·그림1. 유출2021-08-05/번역발표09-02구별. 문서/실제수행·흔한도구/피해규모·운영자별차이. 공격매뉴얼의지시문은사용자지시로취급안함 |
| 165/167 | 공개회사/매출·계정·그룹·도메인탐색·ADFind/Seatbelt/SharpView·도구목록 | 23강4~6·10절. 회사가치/직책정보·AD DS·그룹·도메인·.NET·구성수집vs비밀획득을정의후설명. 표로역할설명을대신하지않음 |
| 165/167 | Kerberoasting/Mimikatz/브라우저·SharpChrome·쿠키/자격증명·반복인증 | 23강7·10절. 티켓요청/정상업무/실제비밀획득·후속사용구별. SMBAutoBrute역할·실패수/성공/인가구별. 추출·해독·인증시도미실행 |
| 165/167 | PowerShell공유탐색·nltest신뢰·NTDS/DC·공유위치준비 | 23강6·8·11~13절. 공유조회/자료읽기·신뢰/권한·DC/NTDS·준비/배포/실행구별. 구체공격명령게시안함 |
| 165/167 | rclone/Mega반출·GMER/PowerShell방어약화·암호화·Armitage/CobaltStrike·AnyDesk/Atera지속성 | 23강9~18절·그림2/3. 정상제품/인가맥락·요청/상태·전송/내용/수신·실행/성공·파일제거/접근해결구별. 과거상품기능/지원/해시효과를영구현재추천으로안함 |
| 166/168 | SolarWinds공급망·서명된Orion/SUNBURST·연표·대규모설치/선택후속·발견/공개 | 24강1~7절·그림1. 빌드/서명/내용안전·당시의심활동과고객침해·Feb20삽입과배포·2020-12-13공개/14SEC보고구별. 원문의12일발견+공개단일화수정. 18,000미만당시설치가능성/모든후속유출구별 |
| 166/168 | 지연활성화·후속TEARDROP/Raindrop·대상선택·OPSEC/DGA/지표·온프렘→클라우드 | 24강6~7·12·18절. 제한사례/추정시각·모든피해자고유지표단정안함·단말/인증/망기록대조 |
| 166/168 | SAML서명자료/키·토큰·GoldenSAML·추적이름APT29/CozyBear/UNC2452 | 24강3·8~18절·그림2/3·lab24. 출처별이름/2022병합/현행MidnightBlizzard·발급자/대상/기간/신뢰/권한·위조/키침해·검사범위·MFA/암호변경한계. ‘최초’는비교근거부족으로보류,기법소개/현장최초관측구별 |
| 167/169 | 주체·목적·가능경로·방어/관측질문·분석과대응연결 | 24강19절과양강가상사례/복습. 국가·금전·위탁·내부자겹침/기회형→표적형변화/기술수준≠영향·이름미확정과영향대응병행. 전체첫째날복습/종합실습은25/26으로남김 |

원문의사실목록을그대로복제하지않고독립상황·비유·설명·작은가상예제·조건변경·관측해석·즉시해설로구성했다. 본교재=범위,공개원분석/표준=사실및보충,자체lab=검사한계시연. 자료목록D:/SANS/SEC450/PDF2022·관련기록에서5PDF/복제/docx확인. 별도원본워크북/위키/VM/사건PCAP는이접근범위에서확보·실행하지않음. 전시스템부재주장아님.

23=d1-14e/24=d1-14f. 기존28공개강의번호/ID/URL/본문과다른과정보존. 계획번호1~26불변. 다음25=d1-15첫째날전체복습,26=d1-16독립종합실습은미완료. 배포검증후에만완료진도1~24로갱신.

## 공식·1차근거 (2026-11-06확인)

- Talos https://blog.talosintelligence.com/conti-leak-translation/ :2021-09-02번역/실제대응비교·도구역할·여러기술수준. 문서와실제행동구별. 원문September유출단정수정.
- Northwave직접조사 https://northwave-cybersecurity.com/threat-intel-research/inside-the-world-of-ransomware-3-3 :유출2021-08-05/번역09-02구별,협력역할변동. 특정기법으로모든브랜드동일주체판정안함.
- MicrosoftAD DS https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview :디렉터리·인증/조회·개체,적용Server2016/2019/2022/2025. 실제조직설치/설정아님.
- rclone https://rclone.org/overview/ :정상파일전송/여러저장소·Mega역할. 서비스/도구존재만으로반출판정안함. 실제접속/업로드없음.
- MITRE https://attack.mitre.org/software/S0575/ :Conti소프트웨어식별/공개기법,개인/우리환경감염증거아님.
- SolarWinds https://www.solarwinds.com/blog/new-findings-from-our-investigation-of-sunburst :2021-01-11당시조사,2019-09가장이른의심·Feb20코드삽입·고객배포/6월제거,시점의성격유지.
- FireEye/Mandiant https://cloud.google.com/blog/topics/threat-intelligence/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor :공개2020-12-13·서명된구성요소·지연/위장·DGA·UNC2452/2022-05 APT29병합. 출처와시점없이영구동일집합안함.
- Microsoft https://www.microsoft.com/en-us/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/ :제한사례후속로더/실행분리·추정시점,모든고객공통시퀀스안함.
- SEC제작사보고 https://www.sec.gov/Archives/edgar/data/1739942/000162828020017451/swi-20201214.htm :2020-12-14/당시18,000미만설치가능성추정. 확인된모든후속피해/유출수치로안함. 투자/법적판단미수행.
- Microsoft현재명명 https://learn.microsoft.com/en-us/defender-xdr/microsoft-threat-actor-naming :NOBELIUM/MidnightBlizzard관계. 20강의출처별이름원칙연결,새경보귀속확정안함.
- Microsoft https://www.microsoft.com/en-us/security/blog/2020/12/28/using-microsoft-365-defender-to-coordinate-protection-against-solorigate/ :서명권한/연합신뢰변경·클라우드권한·세션/자료접근조사. 실제모든피해자/모든앱관리자권한으로확대안함.
- OASIS https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf :SAML2.0Core 2005-03-15/NotBefore·NotOnOrAfter·Audience·Issuer. 현재구현은Microsoft https://learn.microsoft.com/en-us/entra/identity-platform/single-sign-on-saml-protocol 와대조. 표준역사/서비스구현/교육용JSON구별.
- CyberArk옛GoldenSAML제작사URL은현재다른제품페이지로redirect/다른옛경로접근실패. 우회없이원문전체읽기주장안함. 2017검색메타데이터만으로최초실제관측판정안함. 교재의‘최초’수식은이번확인범위에서보류한다고본문명시.

현재수정버전을영구최신으로부르지않고원문의과거해시/제품동작/상품관계를오늘의포괄권고로재게시하지않음.

## 직접실행한독립예제

lab24네파일 metadata.json/check_metadata.py/README.txt/field-notes.txt. 직접정한training-claims-v1,가상.example/4기록/2026-11-01/모의signature필드. SAML/XML/API가아니고키/암호/실제토큰없음. Python3.12.14총16회실행,4입력SHA256불변. tmp/day1-trust-check/actual-check.json.

- 기본11:00Z:R1/R4조건일치,R2audience불일치,R3끝경계기간밖. 서명검사/실제토큰/접근판단/외부조치모두0.
- 11:05끝경계:모두기간밖,10:54:59시작전:모두기간밖,10:55시작포함:R1/R3/R4기간일치. +09오프셋동일순간결과동일.
- fixturefalse와issuer다른임시자료:해당이유표시. R4상황설명변경은결과영향없음. 코드가키신뢰침해·출처진실을판정하지않는한계시연.
- 중복ID/시간대없음/역기간/길이0기간/문자열true/빈정책/깨진JSON/필수필드누락은오류2. 정상불일치/조건일치는종료0이나인증허용아님.
- 실제공격명령/디렉터리/자격증명/인증시도/도구설치/원격접속/파일반출/보안해제/키생성·탈취·서명·토큰위조/실제SAML·제품·API·VM·PCAP·차단·삭제·구매없음. 로컬가상파일읽기·비교·출력만.

## 구성·검증·게시대기

23강20절/65문단/표1/SVG3/즉시복습12;24강20절/68문단/표2/SVG3/즉시복습12. 합40절/133문단/표3/SVG6/즉시해설24.

HTML32구조/중복ID/앵커/상대링크/다운로드href/6일그룹/첫째날1~26/30공개·24첫째날/기존28본문동일/홈과정밖동일통과. 인라인지수/별표코드와강조회귀유지. lab24허용링크/LF추가. 공개원과정식별자없음.

SVG6 XML/한국어폰트경계[]·정적렌더 output/network-security/trust-contact-sheet.png 시각검토. 400폭/방향·제목·범례/표·코드내부스크롤유지. CUA브라우저목록재확인[]여서실제브라우저/모바일미검증·우회없음.

배포성공·공개44파일(HTML32/CSS/course.json/SVG6/실습4)의응답/내용일치후에만완료목록갱신. 현재검토원고는게시대기.


## 게시완료확인

배포커밋e8cde84bb6b1ae018d408544c4ee4b9b7fbad7e8; Pages실행42152560267 success. 공개44파일(HTML32/CSS/course.json/SVG6/실습4) 전부HTTP200·LF정규화내용일치확인후첫째날1~24완료/active_batch해제/다음25·26복습·독립실습범위를기록했다. 최신main bcdf7daba7af923639acc3a74c7a4fe84b9426ca를부모로expected_sha/force=false사용,게시직전fetch에서도추가원격변경없음. 기존28본문/홈과정밖내용보존. 실제브라우저/모바일·원본VM/PCAP·인증/서명구현은미검증. 첫째날전체누락점검과25/26은미완료,전체과정자동화유지.
