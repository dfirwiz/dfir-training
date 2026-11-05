14강 자체 로컬 기록 검토 실습
모든 자료는 가상이며 MISP import JSON/API가 아닙니다. Python 표준 라이브러리만 사용합니다.
fixture.txt는 직접 만든 무해한 텍스트이며 악성 코드가 아닙니다.
다운로드 파일: README.txt, fixture.txt, report.txt, records-start.json, records-reviewed.json, review_intel.py
같은 폴더에서 실행:
python review_intel.py check records-start.json
python review_intel.py check records-reviewed.json
python review_intel.py correlate records-reviewed.json
python review_intel.py plan records-reviewed.json
검토 필요 또는 잘못된 입력은 종료 코드2, 이 연습의 조건 통과는0입니다.
검사 통과는 자료의 진실·MISP 스키마·악성 판정·공유 권한을 검증하지 않습니다.
plan은 표준 출력만 표시합니다. 네트워크 요청·차단·게시·파일 수정은 없습니다.
reports.example/files.example은 예시 도메인입니다. 접속할 필요가 없습니다.
자세한 설명과 조건 변경 과제는 웹사이트14강에 있습니다.
