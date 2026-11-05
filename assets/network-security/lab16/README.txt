16강 독립 로그 조건 검증 실습
네 파일을 같은 폴더에 저장합니다: logs.jsonl, review_logs.py, use-case.json, README.txt
자료는 모두 가상이며 실제 계정·공격·제품/원본 VM 로그가 아닙니다.
ECS와 비슷한 일부 이름을 사용하나 전체 ECS 스키마/Elasticsearch 매핑은 검증하지 않습니다.
Python 표준 라이브러리만 사용하며 파일 읽기/화면 출력 외의 동작은 없습니다.
python review_logs.py logs.jsonl
python review_logs.py logs.jsonl --available-by 2026-11-05T09:06:00Z
python review_logs.py logs.jsonl --time-field ingest
python review_logs.py logs.jsonl --threshold 4
기본값은 사건 시각09:00포함~09:05제외,09:15까지 도착한 자료,고유 실패3건 이상입니다.
종료0은 계산 성공,2는 입력/조건 오류입니다. 후보0건도 계산 성공이면0입니다.
KQL 파서·Elasticsearch·Kibana·SIEM규칙·반복 스케줄·API·차단을 실행하지 않습니다.
자세한 조건/결과/해석/실제 제품 미검증 범위는16강 본문에 있습니다.
