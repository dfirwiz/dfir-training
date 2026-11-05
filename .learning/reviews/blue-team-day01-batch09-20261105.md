# 첫째 날17·18강 범위와 검증

작성·공식 자료 확인일2026-11-05. CURRENT-COURSE-WORK.md·SOURCE-MATERIALS.md·editorial/progress/course.json·batch08 검토와 최신 main을 읽었다. 시작 시 원격d2cc698cb584fafa785cfd2b64463f34dba4d3b4까지 다른 과정의 상태2파일 변경을 fast-forward로 보존했다. 미완료 배치가 없어17/18강을 선택했다. 원래 별도 dfir-training 작업 사본은 건드리지 않았다.

## 원문 범위와 독립 설명 대응

1권 인쇄146~151/PDF148~153을 실제 PDF에서 pypdf로 열어 전부 읽었다. 인쇄149/PDF151의 도구 교환 그림을 Poppler로 렌더·시각 확인했다. 원문 도식·화면·문장·추출 전문은 게시하지 않고 제품 로고 없는 독립 SVG와 자체 가상 자료로 집필했다. 다음152/PDF154는 로드맵,153/PDF155부터 공격자 모듈이다.

| 인쇄 / PDF 쪽 | 학습 항목 | 이번 자체 강의 대응 |
|---|---|---|
| 146 / 148 | 작업 자동화와 조건 있는 오케스트레이션, 플레이북, 표준화·용량·적응·반복부담 | 17강1~5·12·15·18절·그림1/3. 단일 작업·순서/분기·실패·실제효과를 구별하고 자체 시간 계산 실행 |
| 147 / 149 | SOAR·범용 흐름 도구·제품 선택·TheHive/Cortex | 17강16~17절. 현재Node-RED·n8n 라이선스·TheHive6/Flow/Cortex 문서 대조, 설치·연동·무료전체기능 주장 없음 |
| 148 / 150 | 메일파동검색·도메인차단·C2보강·단말격리·계정만료·DNS/Whois/GeoIP·재구축요청 | 17강6~14절·그림2. 조회와 외부전달·상태변경·메시지·권한·효과를 구별. passive DNS 수작업 오해/WHOIS→RDAP 범위/위치추정 한계 보충 |
| 148 / 150 | 노드·입출력·조건·분기·저코드 흐름 | 17강2~5·8~14절,18강8~15절의 자체 offline-replay. 코드/제품 실행의 차이와 재시도·계획 멱등성의 범위를 명시 |
| 149 / 151 | SIEM·IMS/SIRP·TIP·SOAR의 자료교환 방향과 API | 18강1~7·16절·그림1,17강5·13절. 경보/케이스/침해·찾을조건/관측·조회/수행기록·수락/실제완료 구별 |
| 150 / 152 | 일반지식/비정형·반정형자료·코드저장소·공동편집·검색·버전·주석·동기화·쉬운사용·서식/그림·변경알림 | 18강17~19절·그림3. 팀 지식과 검토된 운영절차, Git 판본·보안·공유 범위를 독립 예제로 설명 |
| 151 / 153 | SIEM검색·TIP재사용·사건할당/플레이북·자동화보강·연동개선 | 17강18절,18강2~7·16~20절. 모든 경보가 침해 사건이라는 단순화를 사용하지 않고 담당·근거·상태·이력·재사용 피드백 연결 |

원문의 과거 상품명 Swimlane/FortiSOAR/NetWitness/D3/Komand/Siemplify/SplunkSOAR/XSOAR/StackStorm/Huginn/Airflow 등을 현행 판매·소유·무료 추천 목록으로 반복하지 않았다. 제품 유형·연동 요구·실제 시험 관점은 유지하며 현재 확인한 대표 범용2개와 기존 학습 제품의 문서 범위만 설명했다. 임의로 “오픈 소스면 모든 기능무료·내장연동자동”이라고 확대하지 않았다.

자료는 D:/SANS/SEC450 및 PDF2022 목록과 관련 상태·대화 기록을 다시 확인했다. 본 교재5권·복제본·일부docx와 기존 자체 실습은 접근 가능하지만 원래 별도 워크북/가상위키/VM은 이 범위에서 확보·실행하지 않았다. 제한적 접근 결론이며 전 시스템의 자료 부재를 단정하지 않는다. 자체 lab18은 원본 실습 복제/완료가 아니다.

17강 d1-13은146~148의 자동화·사람의판단, 새18강 d1-13b는149~151의 연동·지식/코드·독립재생이다. 기존 공격자 d1-14는19강으로, 뒤 준비 중 번호도1씩 이동해 첫째날 계획21개다. 기존 공개22개 강의의 번호·ID·URL·본문은 유지한다.

## 현재 공식 근거

- ASD ACSC 등 공동지침2025-05-27 https://www.cyber.gov.au/publication/implementing-siem-and-soar-platforms-practitioner-guidance :안정적인 로그·분석 기반과 숙련자·구현/유지관리 필요, 사람의대체가 아닌지원. 제품이 반드시 한 종류의 구성을 따른다고 일반화하지 않음.
- Node-RED https://nodered.org/about/ / https://nodered.org/about/license/ :IBM시작·OpenJS·Apache2.0 확인. n8n https://support.n8n.io/article/can-i-use-your-license-for-my-use-case / https://github.com/n8n-io/n8n/blob/master/LICENSE.md :Community SUL/별도Enterprise 조건 확인. 원래 docs/sustainable-use-license 경로는 이동 후PageNotFound여서 공식지원·실제저장소라이선스로 대조. 개별법적사용승인·구매·설치·가격추천 미수행.
- TheHive6 Functions https://docs.strangebee.com/thehive/user-guides/organization/configure-organization/manage-functions/about-functions/ :Enabled/Disabled/Dry-run, 엔터티생성/수정제한·null반환 범위. 모든 외부부작용부재로 확대하지 않음.
- TheHive6 Flow https://docs.strangebee.com/flow/user-guides/about-flow/ :6.0·One 표시와 흐름/노드/기존자동화 역할을 확인. Responder https://docs.strangebee.com/thehive/user-guides/analyst-corner/cases/run-responders-on-a-case/ :작업실행과결과검토·연결권한의 의미. 버전/에디션/라이선스·실제설치와 구별, 영구최신이라고 하지 않음.
- CIRCL https://www.circl.lu/services/passive-dns/ :관측 DNS 자료. MaxMind https://support.maxmind.com/knowledge-base/articles/maxmind-geolocation-accuracy :GeoIP를 개인·가정의 정확한위치/행위자증거로 쓰지 않음.
- ICANN https://www.icann.org/en/announcements/details/icann-update-launching-rdap-sunsetting-whois-27-01-2025-en :2025-01-28 gTLD 등록정보의RDAP전환. 모든 등록/주소/ccTLD환경에서WHOIS완전소멸로 확대하지 않음.
- GitHub https://docs.github.com/en/get-started/using-git/about-git / https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository :커밋/저장소/판본관리와 현재파일삭제/과거이력·사본차이. 실제비밀변경·삭제·이력재작성 미수행.

본문의 현재 확인일2026-11-05를 유지한다. 자체 계산은 제품벤치마크·실제대응성과가 아니다. 도메인·위협문자열·포트로 공격/감염/침해성공을 확정하지 않고 조회·재배포·관측·가설·조치권한을 분리한다.

## 실제 실행한 자체 예제

Python3.12.14. lab18 네 파일 deliveries.json/replay_workflow.py/workflow-contract.json/README.txt. training-workflow-v1은 제품API/스키마가 아니다. 모든 조회응답이 미리 적힌 가상상태이며 API·대기·제품·실제보강을 실행하지 않는다. 프로그램13회와17강 본문 코드를 그대로 추출해 실행했다.

- 기본:전달4·모의조회5(2+0+2+1)·중복계획생략1·로컬노트계획2·미해결1. no_match도human_review_required. 외부요청/실제케이스쓰기/차단0.
- 같은파일재실행 결과동일. 상태는실행중메모리에만있어프로세스간멱등성/분산exactly-once보장 아님.
- 전달별max-attempts1:모의조회4·노트계획1·미해결2. 전역재시도예산/실제지연/스케줄러 아님.
- 후속 정상 모의전달:계획3·미해결0·시도6,기존timeout3회 이력 유지. 다른케이스는별도계획,같은키의다른관측값은오류.
- permission_denied는뒤의ok를읽지않고중단:시도4·권한검토미해결. 입력충돌/외부허용true/필수키누락/비허용상태(중복전달포함)/시도0/깨진JSON은오류2.
- 원본4파일 실행전후SHA256일치. 입력변경·네트워크/API·케이스쓰기·계정/단말/방화벽·VM/PCAP/악성코드·차단·외부메시지/티켓·실제보강·설치/구매 미수행.
- 시간계산:독립조회3/5/2초+정리4초 =>순차14/병렬9초,공통대기60초 포함74/69초,전체5초감소6.76%. 독립성·동시처리가능 가정 및대기/다른병목 한계를 명시.

## 구성과 검증

- 17강19절·67문단·표1·그림3·즉시복습해설12,18강21절·70문단·표1·그림3·즉시복습해설12. 합계40절·137문단·표2·SVG6·복습24.
- HTML26개 구조·중복ID·내부앵커·상대링크/다운로드실제href·6일그룹·첫째날1~21순서·ID번호·기존22본문일치·홈페이지과정카드밖내용일치 검증. lab18 렌더허용경로와LF규칙만 추가. 기존인라인코드/강조회귀검사 유지.
- SVG6 XML·한국어폰트경계검사[]·정적접촉시트 output/network-security/automation-contact-sheet.png 시각검토. 도구교환그림은화살표와겹친표시를옆으로수정후최종개별렌더확인.400폭가변이미지·표/코드내부스크롤 유지.
- CUA브라우저목록재확인[]로실제브라우저/모바일미검증. 우회·브라우저설치·제품실행 없음.
- 배포커밋e9d2ac173bda7a5ba0b359b06d9264c7bf708882, Pages실행41995964142 success. 공개38파일(HTML26·CSS·course.json·SVG6·실습4) 전부HTTP200·LF정규화내용일치. 검증후에만첫째날1~18완료와다음19/20을기록했다.
- 게시전최신main fc392dd328c5977b4ab6690179c1b0a30d85261c의다른과정후속2커밋을통합했다. 홈페이지충돌은최신원격과정밖내용보존후자체카드만재생성,통합후전체구조/링크/기존22본문검증재통과. 최신main부모·expected_sha·force=false사용.
