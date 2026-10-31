# DFIR Training

한국어 중심의 디지털 포렌식 및 침해사고 분석 학습 플랫폼입니다.

## 시작하기

`index.html`을 브라우저에서 열거나 GitHub Pages로 배포하세요.

## 첫 번째 코스

**네트워크 트래픽 분석과 위협 탐지** — 네트워크 패킷, 프로토콜, 탐지 전략, 암호화 트래픽의 관찰 가능성을 배우는 독립적인 교육 과정입니다.

## 디자인

- Pretendard: 한국어 UI
- Inter: 영문 UI
- JetBrains Mono: 로그, 명령어 및 코드

## 배포

Settings → Pages → Build and deployment → Deploy from a branch → `main` / `(root)` → Save.

본 프로젝트의 콘텐츠는 독립적으로 작성하며 타사 교육 자료의 원문을 복제하지 않습니다.


## 학습 노트 갱신

`content/course.json`과 `content/notes/`의 본문을 수정한 뒤 `python3 scripts/build_notes.py`로 목록과 페이지를 갱신합니다. 진행 상태는 `.learning/progress.json`, 작성 기준은 `.learning/EDITORIAL.md`에서 관리합니다. GitHub Pages는 main 브랜치의 루트 파일을 배포합니다.
