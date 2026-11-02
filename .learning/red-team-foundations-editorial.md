# 레드팀 기초 과정 작성·게시 기준

공개 과정명은 **레드팀 기초: 공격 이해와 보안 검증**이다. 기존 두 과정의 디자인과 글꼴을 유지하며 독립적인 회차 번호를 사용한다.

- 본문: `content/red-team-foundations/*.md`
- 과정 메타데이터: `content/red-team-foundations/course.json`
- 빌드: `python3 scripts/build_red_team_foundations.py`
- 배포: `courses/red-team-foundations/`
- 전용 스타일과 SVG: `assets/red-team-foundations/`
- 진행 정보: `.learning/red-team-foundations-progress.json`

2026년 11월 2일 사용자는 채팅에서 검토한 첫 단원의 세 회차 전체를 새 과정으로 게시하도록 승인했다. 설명 순서·문단·비유·예제·표·복습 해설을 축약하지 않는다. 공개 과정명과 회차 표기, 내부 출처 표기를 웹용으로 조정한다. 비공개 자료의 파일명·식별자, 원문·화면·파일은 공개하지 않는다.

다이어그램은 원래 노드·분기·되돌아가는 관계를 보존한 SVG로 만든다. 비교표·코드·그림은 좁은 화면에서 내부 스크롤을 제공한다. 복습 해설은 접지 않고 바로 읽을 수 있게 한다. 공식 근거 링크와 확인일, 가상 예제·미실행 절차의 구분을 유지한다.

새 강의는 별도 지시가 있을 때 추가한다. 다른 과정의 진도나 자동화 설정은 변경하지 않는다.
