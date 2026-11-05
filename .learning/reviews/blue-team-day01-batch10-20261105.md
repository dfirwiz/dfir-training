# 첫째 날19·20강 범위와 검증

작성·공식 자료 확인일2026-11-05. CURRENT-COURSE-WORK.md·SOURCE-MATERIALS.md·editorial/progress/course.json·batch09 검토와 최신main을 읽었다. 시작 시 ff7055e5a255e9b86d42bcdf99ab270c43daa7cd까지 다른 과정 상태2파일 변경을fast-forward로 보존했다. 미완료 배치가 없어19/20을 선택했고 active_batch를 기록했다. 원래 dfir-training 작업 사본은 건드리지 않았다.

## 원문 학습 범위와 독립 설명 대응

1권 인쇄152~167/PDF154~169를 실제 PDF에서 pypdf로 열어 모두 읽었다. 이번 완료 범위는152~160/PDF154~162이며161~167은 다음 사례 강의를 위한 읽기일 뿐 완료로 기록하지 않는다. 인쇄157/PDF159 도식을Poppler로 렌더·시각 확인했다. 원문의 대상선택/영향 단순화와 날짜·이름 체계의 오래된 부분을 수정하며 독립적인 설명·가상 예제·SVG로 작성했다. 원문 문장·PDF·화면·추출 전문은 게시하지 않는다.

| 인쇄 / PDF 쪽 | 원문 학습 항목 | 독립 강의 대응 |
|---|---|---|
| 152 / 154 | 로드맵·공격자 모듈 연결 | 19강1·18절,20강1·19절. 자동화·지식 관리 다음에 목적/선택/이름·사례로 연결 |
| 153 / 155 | 상대의 목적·방식 이해의 필요성 | 19강1~5·15~18절·그림1/3. 인용문 재현 대신 문·열쇠 비유와 관측/가설/영향 연결 |
| 154 / 156 | 국가 연계·범죄·랜섬웨어·역사적 공개 분석 | 19강4~8절. 국가/IP/국적·도구/주체 구별, APT1 공개일2013-02-19 수정. 과거 국가·조직·도구 이름을 현행 고정 목록으로 반복 안 함 |
| 155 / 157 | 핵티비즘·DDoS·변조·절취/공개·독싱·명성/주장 | 19강9~10절. 공개 주장/실제영향 구별,2024 Google분석과 대조. 교재의 비공개 대화공간 침투 권유는 실행지시로 취급하지 않음 |
| 156 / 158 | 위탁·접근권 판매·RaaS·내부자·돈/자료/평판·DLP/UBA·권한악용 | 19강11~14절·그림2. 분업·오용/실수/탈취·개인정보/오탐 구별. 원문PNB금액은 검증된 사실로 재게시하지 않고 가상 지급업무/무결성 예제로 원리 보존. 내부위험=항상희귀/감정=악의 단순화 안 함 |
| 157 / 159 | 기회형/표적형·영향·BEC·봇넷/트로이/스팸/가짜백신 | 20강2~5·8~9절·그림1. 선택방식과 확인영향 독립. 악성파일·유인·자원사용과 실제실행 구별. 특정 악성코드명으로 감염확정 안 함 |
| 158 / 160 | 광범위 피싱/사회공학·웹유입·스캔/취약점·가짜백신·봇자원/스팸/DDoS/호스팅/DNS/접근판매 | 20강4~5·8절. 정상대안·단말/서버/메일/프록시/리졸버 대조, 영향확대/후속표적화 가능성 |
| 159 / 161 | 표적형/APT·맞춤유인·워터링홀·물리/USB·노출서비스/제로데이·공급망·이중협박 | 20강6~9절,19강8절. APT정의·개인화/귀속·제로데이필수 오해 교정, 관측/성공/피해 분리 |
| 160 / 162 | 여러 회사 명명·DEV/APT/FIN/UNC/TEMP·원소/동물/관련이름·그룹/악성코드 중복 | 20강10~19절·그림2/3·lab20. Microsoft2023날씨/Storm, GTIG2026두단어/UNC유지, CrowdStrike2022설명과 현재목록, MITRE관련군집/부분중첩/비전이성. Kaspersky과거‘고정규칙없음’을 모든현재정책의 부재로 단정 안 함 |

사례161~167(Mirai·Colonial·Conti·SolarWinds)은 다음21강부터 충분히 나눠 집필한다. Colonial 원문의2020표기는 다음 집필에서 실제2021근거를 공식 문서로 다시 확인해야 한다. 미완료 사례를 요약으로 대체하지 않는다.

D:/SANS/SEC450 및 PDF2022의5권·복제본·일부docx 목록과 관련 진행/대화를 다시 확인했다. 별도 원본 워크북·가상위키·VM은 이 범위에서 확보/실행하지 않았다. 제한적 접근 결론이며 전 시스템의 자료 부재를 단정하지 않는다. 자체lab20은 원본 실습의 복제/완료가 아니다.

19강d1-14는목적/역할, 새20강d1-14b는선택/이름/비교, 새계획21강d1-14c는사례다. 기존검토d1-15는22강,종합실습d1-16은23강으로 옮겼다. 기존공개24강번호/ID/URL/본문 유지. course.next_lesson=d1-14c지만 progress의완료/다음범위는배포검증후갱신한다.

## 현재 공식 근거와 수정

확인일2026-11-05. 1차문서의 직접 접근 범위만 사용한다.

- Mandiant https://cloud.google.com/blog/topics/threat-intelligence/mandiant-exposes-apt1-chinas-cyber-espionage-units :공개안내2013-02-19. 원문2012소개 수정,과거지표를현재귀속규칙으로 안 씀.
- Canadian Centre for Cyber Security https://www.cyber.gc.ca/en/guidance/ransomware-playbook-itsm00099 :암호화없는자료절취/협박·RaaS/분업·기밀성/가용성구별. 국가통계/법률/대금결정으로확대하지않음.
- NCSC https://www.ncsc.gov.uk/guidance/reducing-data-exfiltration-by-malicious-insiders :신뢰권한/반출방어. 사람의감정/이상단서=악의로단정안함.
- Google https://cloud.google.com/blog/topics/threat-intelligence/global-revival-of-hacktivism/ :2024-06-27분석. 주장/활동·복합동기·수준다양성,고정단일조직단정안함.
- NIST https://csrc.nist.gov/glossary/term/advanced_persistent_threat :출처별정의맥락·지속성/자원/적응,표적메일=APT/국가/제로데이필수로확대안함.
- Microsoft https://www.microsoft.com/en-us/security/blog/2023/04/18/microsoft-shifts-to-a-new-threat-actor-naming-taxonomy/ 와 https://learn.microsoft.com/en-us/defender-xdr/microsoft-threat-actor-naming :2023전환및현재날씨/Storm설명. 국적/IP판정법아님,옛기록보존.
- GTIG https://cloud.google.com/blog/topics/threat-intelligence/updated-cyber-threat-actor-naming-system :2026-07-24발표/07-30추가. 두단어·COMET예·순차전환·옛이름검색·UNC유지·출처간정확일대일드묾. Mandiant옛접두어만을현행전체정책으로소개안함.
- MITRE https://attack.mitre.org/groups/ 및 https://attack.mitre.org/groups/G0007/ :추적활동군집·AssociatedGroups부분중첩·공개기법부분집합,APT28/G0007관련ForestBlizzard/STRONTIUM/FancyBear/Sofacy. Sofacy/Sednit그룹/악성코드문맥차이. 우리사건귀속증거로바꾸지않음.
- CrowdStrike https://www.crowdstrike.com/en-us/blog/naming-adversaries-and-why-it-matters-to-security-teams/ 및 https://www.crowdstrike.com/en-us/adversaries/ :2022-05-31설명과현재공개목록을분리. SPIDER=모든비국가활동이라고확대안함.
- CISA일부원페이지/원PDF는403,호주ransomware옛짧은경로404. 우회하지않고직접읽었다고주장하지않음. 본문은접근한공식근거로한정.

## 직접 실행한 자체 자료

lab20 네 파일 comparison.json/compare_names.py/analysis-notes.txt/README.txt. 가상Research-A/B/C·TrainingCedar/Birch/Lark·reports.example·training-names-v1. 실제보고서/제품API/스키마가아니다. Python3.12.14의14회실행과원본4파일SHA256불변확인.

- 기본A-2026:같은출처이름변경A-2022/A-2026,직접중첩B-2026,동일표시이름별도C-2026. 현실귀속unresolved/외부조회0/중첩전이false.
- labelTrainingLark:2건ambiguous_label/자동병합false/정상종료0. record-idB:동일묶음B만/직접후보A-2026/충돌C. 옛Cedar검색:동일A두기록.
- 없는이름/ID:no_record_in_this_dataset,종료0. 미관측/현실행위자부재/침해부재와구별.
- 임시자료에B-C부분중첩추가/C표시이름Dove변경:A기준직접후보B만,충돌없음. 중첩의연쇄확장안함확인.
- 출처다른rename/중복ID/없는관계참조/필수값누락/불가능날짜/허용외가상URL/깨진JSON:오류종료2. 형식검사는출처내용진실검증아님.
- 실제외부조회/API/위협플랫폼/제품설치/계정/차단/메시지/워크북/VM/PCAP/악성코드실행/구매없음. 로컬파일읽기/출력만,임시변형시험은배포자료변경아님.

## 구성·정적 검증·남은 게시 확인

19강19절/64문단/표1/SVG3/즉시복습해설12. 20강20절/75문단/표2/SVG3/즉시해설12. 합39절/139문단/표3/SVG6/복습24.

HTML28구조/중복ID/내부앵커/상대링크/실제다운로드href/6일메뉴/첫째날1~23번호/26공개·20첫째날/기존24본문동일/다른홈내용동일검증통과. 인라인코드내별표/지수·코드강조회귀유지. lab20허용링크와LF규칙만추가. 공개원식별자없음.

SVG6 XML·한국어폰트경계검사[]·정적렌더접촉시트 output/network-security/adversary-contact-sheet.png 시각검토. 400폭·읽는방향/제목/범례·확률아닌칸/중첩비전이성설명. 표·코드내부스크롤/CSS기존디자인보존. CUA브라우저목록재확인[]로실제브라우저/모바일미검증,우회없음.

배포와공개40파일(HTML28/CSS/course.json/SVG6/실습4)의응답·내용일치확인후에만완료진도를갱신한다. 이원고시점은게시대기이며완료로간주하지않는다.


## 게시 완료 확인

배포커밋6ddc1a3f2ed227703ad5f5d52662e54bb5f8eeb4; Pages실행42004526214 success. 공개40파일(HTML28/CSS/course.json/SVG6/실습4) 전부HTTP200·LF정규화내용일치확인후첫째날1~20완료/active_batch해제/다음21사례범위를기록했다. 최신main a4f7ad55b3ee52eedd6e53c74d7287dfbb58fda1까지다른과정후속변경을통합했고홈페이지충돌은최신원격의다른내용보존후자체카드만재생성했다. 통합후구조/링크/기존24본문/홈밖내용검증재통과. 최신main부모+expected_sha+force=false사용. 실제브라우저/모바일/원본VM/PCAP는미검증이다.
