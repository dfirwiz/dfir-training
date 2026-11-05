# 첫째 날13·14강 범위와 검증

작성·공식 문서 확인일2026-11-04. 중단 후2026-11-05 예약 실행에서 검증된 기존 배치를 이어 게시하며 새 강의는 추가 집필하지 않는다. CURRENT-COURSE-WORK.md, SOURCE-MATERIALS.md, 최신 main6e0ceddaa71cedcbfbb6beb4fc2d26e00b4deada, editorial/progress/course.json, batch06 검토 기록을 읽었다. active_batch가 없어 다음13/14강을 선택했다. 기존 별도 작업 사본은 건드리지 않았으며 원본 다섯 권의 재지정·동일성 기록을 유지했다.

## 자료 확인과 범위 대응

실제 D:/SANS/SEC450/450_2022 (01).pdf를 pypdf로 열어 인쇄121~133/PDF123~135 각 페이지를 추출하고 해당 설명을 읽었다. 인쇄123/125/126/128/130을 별도 로컬 렌더용으로 묶어125의 구조를 시각 확인했다. 원문 도식·실제 악성 캠페인 값·화면·전문은 공개하지 않았다. 공식 자료 및 자체 가상 예제로 독립 집필했다.

| 인쇄 / PDF 쪽 | 원문 학습 항목 | 이번 강의 대응 |
|---|---|---|
| 121 / 123 | MISP 역할, 웹/API, 용량·유형·관계·공유·UI·경고 | 13강2~9절·12~18절, 그림1~3; 처리량·연동 실행 주장 없음 |
| 122 / 124 | 구조화, 입출력, 협업/제안, 피드, 위임, PyMISP, 분류·지식·모듈 | 13강2·7·13·15~17절; 피드의 세부 선정은 이전12강과 연결 |
| 122 / 124 | 관측/오탐/만료, STIX, 알림 서명/암호화 | 13강10·17절; 원문의 false-negative 표현을 2.5 코드와 대조해 false-positive로 정정 |
| 123 / 125 | 이벤트·속성·유형/범주·사이팅·태그·택소노미·갤럭시 | 13강3~7·10절; 일반 보안 이벤트와 MISP Event 구분 |
| 124 / 126 | 수동 생성/등록/분류/검토/게시, 도구 API·피드 연동 | 13강11~16절, 14강3~10·13~18절; 자료 수신에서 내부 관측·자동 경보로 건너뛰지 않음 |
| 125 / 127 | 같은 해시의 두 이벤트 관계·기존 분류 재사용 | 13강8~9절·그림2, 14강7·11~12절·그림2; 동일 행위자/새 인프라 귀속을 자동 확정하지 않음 |
| 126 / 128 | 조직 간 양방향 정보 교환 | 13강14~15절·그림3, 14강15절; push/pull·권한/필터·내부 예외 구분 |
| 127 / 129 | 이벤트 제목·날짜·공유 태그 | 13강3·11·14절, 14강3~6절; 날짜의 의미, WHITE→CLEAR, 보고서 참고값의 역할 보존 |
| 128 / 130 | 자유 텍스트 가져오기·유형 제안·범주 검토 | 13강4·11~12절, 14강5~10절·그림1; 인식 통과를 위한 값 조작을 권하지 않음 |
| 129 / 131 | 속성 목록·그래프·외부 피드 관계·피벗 | 13강8~9절, 14강11~12절; 합성 동일 해시 관계 직접 실행, 실제 피드 조회 아님 |
| 130 / 132 | 이벤트 목록의 조직·클러스터·태그 | 13강7~8절; 표시를 원출처 독립성·귀속 근거로 오인하지 않음 |
| 131 / 133 | TIP와 사건 관리 시스템·자동화·재사용·우선순위 | 13강16~18절, 14강17~18절; 내부 사건과 외부 이벤트의 의미 분리 |
| 132~133 / 134~135 | 로드맵·별도 워크북/위키의 Exercise1.2 안내 | 14강1~2절에서 접근 한계를 밝히고 독립 로컬 기록 실습 제공. 원래 실습 수행 완료 아님 |

자료 위치 D:/SANS/SEC450 및 PDF2022 하위 파일 목록, 현재 작업 폴더의 workbook/wiki/MISP/pcap 관련 경로·이전 기록을 확인했다. 본 교재 다섯 권과 복제본, 자체 PCAP·자체 이전 실습 등은 있으나 해당 원본 별도 워크북/가상 위키/VM 실습을 확보하지 못했다. 접근한 범위의 결론이며 모든 위치에 자료가 없다는 단정이 아니다. 다음은 인쇄134/PDF136 로드맵과135/PDF137부터 SIEM 모듈, 화면15/16강 순서다.

## 공식 근거와 적용 범위

- MISP 기능 https://www.misp-project.org/features/ : 저장·관계·UI/API·모듈·협업·입출력·서명/암호화 기능을 현재 공식 안내와 대조. 성능 비교나 실제 연결 시험은 하지 않음.
- 자료 모델 https://www.misp-project.org/datamodels/ 및 객체 https://www.circl.lu/doc/misp/misp-objects/index.html : 유형/범주, 객체·템플릿과 관계 보존. MISP JSON 자체 예제로 가장하지 않음.
- 택소노미 https://www.circl.lu/doc/misp/taxonomy/index.html 및 갤럭시 https://www.circl.lu/doc/misp/galaxy/index.html : 분류와 분석 근거·귀속을 분리.
- 사이팅 https://www.circl.lu/doc/misp/sightings/index.html 및 2.5 구현 https://github.com/MISP/MISP/blob/2.5/app/Model/Sighting.php :0관측/1오탐/2만료 직접 대조. 오탐과 미탐, 횟수와 단말 수, 제공자 관측과 내부 관측 구분.
- MISP2.5 속성 구현 https://github.com/MISP/MISP/blob/2.5/app/Model/MispAttribute.php :to_ids·배포0~5 뜻 대조. 최초 Attribute.php 경로404 후 현재 MispAttribute.php로 확인했으며 미확인 내용을 추정하지 않음.
- API https://github.com/MISP/MISP/blob/2.5/docs/API_Doc.md 및 공식 2.5 OpenAPI https://raw.githubusercontent.com/MISP/MISP/2.5/app/webroot/doc/openapi.yaml :실제 제품 요청·자료와 자체 로컬 형식 구분. 2.5는 대조한 계열이며 최신/설치 실행 버전이라는 주장 없음.
- 보고서 입력 https://www.circl.lu/doc/misp/create-event-report/index.html 및 이벤트 수명주기 https://www.circl.lu/doc/misp/using-the-system/ :자유 텍스트 제안·검토·저장·게시의 의미와 제안 협업. 실제 화면/클릭 미검증.
- 공유 https://www.circl.lu/doc/misp/sharing/index.html :push/pull·필터·내부 인스턴스 예외, 위임 게시·권한·수신 결과를 구분. 태그·메일 없이 게시를 전달 차단으로 보지 않음.
- 워닝리스트 https://www.misp-project.org/warninglists/ :알려진 값의 맥락이며 무해 확정 아님.
- FIRST https://www.first.org/tlp/ :TLP2.0 WHITE→CLEAR, AMBER+STRICT 범위와 실제 통제 차이.
- Zeek https://zeek.org/2018/10/renaming-the-bro-project/ :Bro 명칭 변경 공식 발표. 과거 메뉴 호환 이름과 현재 도구명을 구별.

## 실제 실행한 독립 실습

assets/network-security/lab14의6파일: README.txt, report.txt, fixture.txt, records-start.json, records-reviewed.json, review_intel.py. 모두 자체 생성이며 training-cti-v1은 MISP 스키마/API가 아니다. 가상 보고서·도메인을 외부로 조회하지 않는다.

Python3.12.14로 검사11회와 본문의 파일 해시 계산 명령을 실행했다. report.txt의 해시는 fixture.txt 실제 바이트에서 계산한19fb78b143afba673bd5b59aacee55c99907c85864d5560c44f4dde648a120e9와 일치한다. 생성한 무해한 같은 바이트를 두 가상 기록에 재사용했으므로 실제 위협·독립 관측의 발견이 아니다.

- 시작본 check2, 참조 답안 check0, correlate0: E1/E2 같은 해시·귀속unknown, plan0:고유후보1·외부전달NOT-PERFORMED.
- B1만 다른64글자 값:검사0이지만 정확 일치 상관관계 출력 없음. 모든to_idsfalse:plan0·후보0.
- 상태만 완료/불리언 문자열/필수키 누락/깨진JSON 각각2.
- 근거 없는 seen_locally=true 사본은0. 이는 검사기의 의미 검증 한계를 의도적으로 검증한 것, 실제 관측 또는 완료 답안이 아님.
- 모든 원본 입력·프로그램·보고서 파일의 실행 전후 SHA256 일치. 파일 수정·게시·전송 없음.
- 실제 MISP/TIP/API/서버/피드/VM/PCAP/단말/공격/차단·메일·외부 공유를 실행하지 않음.

## 구성·검증

- 13강20절·74문단·표1·SVG3·복습/즉시해설12개, 14강19절·68문단·표1·SVG3·복습/즉시해설12개. 마지막 빌드 통계가 우선한다.
- HTML22개 구조·중복ID·상대 링크/다운로드·내부 앵커·날짜/번호 참조, 기존18개 공개 강의 본문 및 홈페이지 과정 카드 밖 내용 일치 검증.
- SVG6개 XML·한국어 글꼴 경계 검사 통과, 접촉 시트 output/network-security/misp-contact-sheet.png 직접 시각 확인. 모바일용400폭 도식·가변 이미지·표/코드 내부 가로 스크롤 CSS 유지.
- 브라우저 getState 재시도는 kernel-assets 경로 오류. 우회하지 않았으며 실제 브라우저·모바일·제품 화면 검증은 수행하지 못함.
- 배포 커밋57991e40967d60d5a1925a5be66423a45d66043f, Pages 실행41979704169 success. 공개36개 파일(HTML22·CSS·course.json·SVG6·실습6) 전부 HTTP200 및 내용 일치, fixture 실제 바이트와 SHA256도 별도 일치 확인. 완료 목록은 이 검증 뒤에만 첫째 날1~14강으로 갱신했다. 다음은15/16강이며 SIEM 범위를 깊이에 따라 더 분할할 수 있다.
- 2026-11-05 재개 시 최신 main279cb5078df53756ca2c9b2ec0d02154022462d2의 다른 과정18개 후속 커밋을 통합했다. 홈페이지는 최신 원격의 다른 과정 내용을 유지하고 이 과정 카드만 다시 생성하여 충돌을 해결했다. 통합 후 HTML·보존·예제 검사를 다시 통과했다. 실습14 텍스트는 .gitattributes의 LF 규칙으로 고정해 다운로드한 fixture의 해시를 보존한다.
