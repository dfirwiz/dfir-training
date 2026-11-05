# 첫째 날15·16강 범위와 검증

작성·공식 자료 확인일2026-11-05. CURRENT-COURSE-WORK.md, SOURCE-MATERIALS.md, 최신 main54d74c5043484f258b16a257cb4c71f1de6f731a, editorial/progress/course.json과 batch07 검토를 읽었다. 미완료 배치가 없어15/16강을 선택했다. 작업 사본 dfir-training-menu만 사용하고 원래 별도 사본의 다른 수정은 건드리지 않았다.

## 범위와 자료 역할

본 교재1권 인쇄134~145/PDF136~147을 실제 pypdf로 열어 읽었다. 이후146~168쪽은 모듈 경계·후속 계획 확인용으로 추출·일부 읽은 범위이며 이번 완료 범위가 아니다. 인쇄136/PDF138을 Poppler로 직접 렌더하고 처리 구조를 시각 확인했다. 원문 화면·문장·예제 주소·추출 전문은 공개하지 않았다.

15강 d1-12는 SIEM 입력·처리·품질·시간·검색·저장량을, 새16강 d1-12b는 사용 사례·Discover/KQL와 독립 조건 검증을 다룬다. 기존 자동화 d1-13은17강으로, 뒤의 준비 중 첫째 날 번호도1씩 이동한다. 계획은 첫째 날1~20강이며 이미 공개한 번호·ID·URL·교육 본문은 유지한다. 다음은 인쇄146/PDF148의 자동화다.

| 인쇄 / PDF 쪽 | 원문 학습 항목 | 자체 강의 대응 |
|---|---|---|
| 134~135 / 136~137 | 로드맵·SIEM과자동화 모듈 범위 | 15강1~3절,16강1·22절; 자동화146+를17강으로 보류 |
| 136 / 138 | 수집·파싱·필터·보강·색인·검색·시각화·경보·보고 | 15강2~14·18~19절·그림1~3; 생성/읽기/전송/저장/검색과 원관측·보강 구분 |
| 137 / 139 | 검색 언어·UI·시각화·경보·API·문서지원·에이전트·다중형식·성능·앱/갱신 | 15강4~7·11~13·15~18절; 가상EPS/원자료량 계산과 실제 성능 시험 구별 |
| 138 / 140 | 여러 제품 유형·실제 수집/검색/경보를 직접 시험 | 15강17~18절; 과거 업체 목록을 현행 추천·판매 목록으로 재게시하지 않음 |
| 139 / 141 | 사용 사례는 조건식보다 넓은 목적·결과·후속 절차 | 16강1~5·21절; 반복실패·업로드·다운로드·그룹추가·피싱 제출 관측 한계 |
| 140 / 142 | 조건·자료·양성/정상 시험·문서화·정기 재시험 | 16강7·15~21절·그림1; 실제 공격/제품시험 아님을 표시 |
| 141 / 143 | 제목·문제·목표·요건·주/보조출처·논리·근거·조사/오탐·분류 | 16강3~6절 및 lab16/use-case.json의 독립 UC-AUTH-01 |
| 142 / 144 | 사용 사례 저장/변경·업무/분류 연결·분석가 인수인계 | 16강5~7절; 위키/이슈/표/파일/DB 방식과 검토 책임 |
| 143 / 145 | Logstash→Elasticsearch→Kibana 구성 | 15강18절,16강8~9절; 현행 ingest pipeline 대안과 과거 예제 필수성 구분 |
| 144 / 146 | Discover의 대상·시간·필드·개별문서·히스토그램·검색 | 16강8~9·14절; 인덱스패턴→데이터뷰, 권한/범위/표시제한 |
| 145 / 147 | 자유검색·필드검색·범위·AND·OR·괄호 | 16강10~15절; 원문 고정값 대신 ECS 예시, KQL/정규식/집계 차이 |

D:/SANS/SEC450의 본 교재 및 PDF2022 복제본, 관련 대화/상태와 기존 workbook/wiki/VM 확인 기록을 검토했다. 이 범위는 본 교재의 개념/제품 예제이며 별도 원본 워크북·VM·실제 Elastic 로그는 확보·실행하지 않았다. 기존 자체 PCAP·JSON 파일은 원래 실습 자료가 아니므로 구별한다. lab16은 새 자체 합성 자료와 계산이다. 이전 제한적 접근 기록을 모든 시스템의 자료 부재로 확대하지 않는다.

## 현재 공식 근거

- Logstash 처리 https://www.elastic.co/docs/reference/logstash/how-logstash-works 및 큐 https://www.elastic.co/docs/reference/logstash/queues-data-resiliency :입력/필터/출력·메모리/PQ/DLQ·활성화와 실패 범위. 실제 제품 실행/설정 아님.
- ingest pipeline https://www.elastic.co/docs/manage-data/ingest/transform-enrich/ingest-pipelines :Logstash가 모든 현행 구성의 필수라는 과거 단순화 수정.
- ECS 기본 https://www.elastic.co/docs/reference/ecs/ecs-base 및 이벤트 https://www.elastic.co/docs/reference/ecs/ecs-event :@timestamp 대체 가능성·event.created/ingested·시간차의 의미. 수집 지연과 공격 길이 구분.
- ECS 사용자 https://www.elastic.co/docs/reference/ecs/ecs-user / 출발 https://www.elastic.co/docs/reference/ecs/ecs-source / 목적지 https://www.elastic.co/docs/reference/ecs/ecs-destination / HTTP https://www.elastic.co/docs/reference/ecs/ecs-http :이름·영역·주소역할·포트/상태코드 자료형. 자체 JSON은 ECS 전체 스키마·매핑 검증 아님.
- 매핑 keyword https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/keyword / text https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/text :전체값/분석·구문검색과 바이트일치 차이.
- KQL https://www.elastic.co/docs/reference/query-languages/kql / 개요 https://www.elastic.co/docs/explore-analyze/query-filter/languages/kql :값/범위/AND/OR/NOT/괄호/와일드카드/존재 의미, 집계·변환·정렬 아님. text/keyword·화면언어·필드명 확인. 실제 KQL·API 실행 아님.
- 데이터뷰 https://www.elastic.co/docs/explore-analyze/find-and-organize/data-views / Discover https://www.elastic.co/docs/explore-analyze/discover/discover-get-started / 시간필터 https://www.elastic.co/docs/explore-analyze/query-filter/filtering :과거 index pattern 명칭과 현재 구성, 조회대상/권한/시간필드/추가필터 교집합. 화면·설치버전 미검증.
- ATT&CK https://attack.mitre.org/ / VERIS https://verisframework.org/ :분류의 목적만 연결, 이름=탐지전체검증·귀속 확정으로 해석하지 않음. VERIS 사이트의 오래된 버전 문구를 현행 최신으로 반복하지 않음. KillChain 제작사 공식 페이지 https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html 는403이어서 역사적 분류명과 미확인 범위를 구별.

과거의 “모든로그가있다”, “실패뒤성공=침해”, “query=집계”, “화면0=활동없음”을 쓰지 않는다. 버전 번호를 확인·설치하지 않았으므로 현재 최신 제품이라고 명명하지 않는다. 확인일은2026-11-05이며 과거 문서와 현행 개념 차이를 해당 본문에 적었다.

## 실제 자체 실행

Python3.12.14, tmp/day1-siem-check/actual-check.json. lab16 네 파일 logs.jsonl/review_logs.py/use-case.json/README.txt. 기록9줄 모두 가상이고 공격·인증 시도를 실행한 것이 아니다. 프로그램은 고정창 계산이며 KQL 파서·Elastic 규칙·스케줄러·슬라이딩창·ECS 스키마 검사기가 아니다.

- 기본:전체9/가용9/구간7/중복1/식별누락1/선택5/묶음3/후보1, 주묶음 고유L1·L2·L3=3.
- 가용시각09:06, ingest시각선택, 임계4 각각 후보0; 계산 성공0이며 위협 부재가 아님.
- 끝09:06이면 주묶음3,09:06:01이면4. 성공자료를 구간 안으로 옮겨도 실패선택5 유지.
- 시간대 누락/임계0/역전구간/중복ID 내용충돌/필수키 누락/깨진JSON/빈파일 각각 오류2. 합계 프로그램14회.
- 원본 네 파일의 실행 전후 해시 일치. 파일 변경·네트워크·API·발송·차단 없음.
- 15강 본문 Python을 그대로 추출해 실행:69120000000바이트/69.12GB/64.37GiB/30일2.0736TB. 색인·복제·보강·백업·압축 제외한 원자료 계산.09:04→09:04:02→09:12를 datetime으로2/478/480초 검산.
- 실제 Elastic/Kibana/KQL·규칙 스케줄/VM/PCAP/계정/공격/센서/자동대응을 실행하지 않았으며 그 결과를 만들지 않음.

## 렌더링 수정과 검증

- 15강20절·71문단·표3·SVG3·복습/즉시해설12,16강23절·72문단·표2·SVG3·복습/즉시해설12. 총43절·143문단·표5·그림6·복습24.
- 새 본문의 인라인 지수코드에서 별표가 강조로 잘못 해석돼 HTML검사가 실패한 것을 발견해 수정했다. 인라인코드 임시 보존으로 **`uid`** 같은 기존 강조를 보존하면서 코드의 거듭제곱을 그대로 출력한다. 실제 회귀 예제3개와 전체HTML검사 통과.
- 다운로드 렌더 허용 경로가 lab05/10만 지원해 이전14강의6개 다운로드가 Markdown 텍스트로 남아 있던 문제를 확인했다. lab14/16 지원을 추가해 실제 클릭 가능한 링크로 수정했다.14강 설명·예제·해설 문장은 그대로이며6개 링크의 HTML표현만 변환. 기존20개 중19개 강의본문HTML 완전일치,14강은 해당 변환만 일치 확인했다. 과정 밖 홈페이지도 일치.
- HTML24개 구조·중복ID·내부 앵커·상대링크·다운로드존재/실제href·6일 목차·첫째날1~20순서·ID번호 검증. 모든새SVG XML·한국어글꼴경계[]·정적렌더 접촉시트 output/network-security/siem-contact-sheet.png 시각 확인. 표/코드 내부 스크롤·가변400폭그림 CSS 유지.
- 이번 CUA 초기화는 성공했지만 브라우저 목록이 비어 있고 iab 생성이 “Browser is not available: iab”로 실패했다. 우회하지 않았으며 실제 브라우저/모바일 화면은 미검증. 이전 kernel-assets 오류와 이번 제한을 구별한다.
- 배포 커밋781ff99654b5e8be162bcf2940e6676b53b1e2cc, Pages 실행41988675852 success. 공개42파일(HTML24·CSS·course.json·새SVG6·lab16의4파일·복구한lab14의6파일) 전부HTTP200 및 LF정규화 내용 일치. lab14 fixture 바이트·기존SHA256도 확인. 그 뒤에만 첫째날1~16 완료와 다음17/18을 기록했다.
- 게시 전 최신 다른 과정 커밋fadab5efa95d6cae14248a8a13097a085bb366ce의 후속3커밋을 통합했다. 홈페이지는 최신 원격의 과정 밖 내용을 보존하고 이 과정 카드만 재생성했다. 통합 후 구조·링크·다운로드href·기존본문 검증을 다시 통과했다. 최신main을 부모로 expected_sha/force=false 조건을 사용했다.
