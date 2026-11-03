# 4장 UI 보강 검토 — 2026-11-03

## 변경 범위

사용자 피드백: 개념 위주 설명에 실제 Cobalt Strike 화면과 설정 위치·절차가 부족함.

| 장/강 | 추가한 실제 공식 화면 | 수 |
| --- | --- | --- |
| 4장 1강 | Client 접속 | 1 |
| 4장 2강 | HTTP, 수동 프록시, DNS, Guardrails | 4 |
| 4장 3강 | SMB, TCP, Pivot Graph | 3 |
| 4장 4강 | Stageless Generator, Windows Stageless | 2 |
| 4장 5강 | Sessions Table, Beacon Console, Job Browser | 3 |

13개 이미지는 Fortra의 공개 공식 안내서에서 원본 바이트를 받아 사용했고 각각 직접 시각 확인했다. 수정·AI 재생성·비공개 교재 화면 재사용은 하지 않았다. 출처 페이지·이미지 URL·확인일·원본 해시·크기는 screenshots/sources.json에 기록했다. 이미지의 예시 주소·계정·암호·작업 결과는 공개 문서의 예시이며 사용자의 자격증명이나 이 과정의 실측값이 아님을 본문에 명시했다.

## 구체적인 보강

- Client Host·Port·User·Password·Connect, 관리 포트와 C2 포트 구분.
- Cobalt Strike → Listeners → Add, 실제 Channel·Template 필드와 구버전 Payload 표기 구분.
- HTTP Hosts의 +·선택 제거·목록 비우기, 포트·Profile·stager·proxy·Guardrails·Save와 목록 확인.
- 프록시의 별도 …·Set·Reset 및 인증 정보의 용도, DNS Hosts·Stager·Bind·Resolver 구분.
- SMB 파이프, TCP 포트와 localhost 체크박스, 대기 정의와 실제 실행·연결 구분.
- Visualization의 Table·Pivot Graph 전환, 노드 우클릭/빈 배경 우클릭, Hide/Show 표시 효과 구분. 현행 공식 범례의 주황/파랑 링크 설명으로 수정.
- 생성 메뉴와 창 제목, Listener …·Output·Exit·System Call·HTTP Library·x64·Override·Payload Store·Generate의 위치·기능.
- Sessions Table 대상 선택, Interact 콘솔의 입력/출력/상태줄, Jobs·View → All Jobs의 열·기능과 대기열 차이.
- 페이지 상단에 실제 화면 바로가기, 각 스크린샷에 원본 확대 링크와 좁은 화면 내부 스크롤 제공.

## 검증

- stdlib 빌드 성공. 4장 기존 55절·40복습 해설과 개념도 10개 유지, 실제 화면 13개 추가.
- 모든 PNG의 서명·크기·SHA256 확인, 출처 메타데이터와 원본 일치.
- 로컬 링크·화면/본문 앵커·그림 수·복습 수 검증. 1~3장 본문 HTML 비교 동일.
- 브라우저에서 HTTP 화면 바로가기와 PNG 로딩·원본 링크 확인.
- 390px iframe의 document clientWidth=scrollWidth=375. 440px 설정 이미지와 1283px 세션 표가 327px 내부 영역에서 스크롤하며 본문 폭을 넘기지 않음.
- 실제 Cobalt Strike 설치·리스너 저장·생성물 제작·에이전트 실행은 수행하지 않았으며 본문에서도 구분.

배포는 최신 main의 동시 변경을 보존한 뒤 기존 GitHub Pages 경로로 진행하고 공개 HTML·PNG·CSS 응답을 별도 확인한다.
