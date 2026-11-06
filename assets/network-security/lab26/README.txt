26강 독립 로그 검색 실습
events.jsonl/use-case.json/review_logs.py/README.txt를 같은 폴더에 둡니다. 모든 자료는 직접 만든 가상 기록입니다.
Python 표준 라이브러리 sqlite3로 메모리 안에서 실제 SQL을 실행합니다. Elastic·KQL·제품 API·원본 워크북·VM 실습이 아닙니다.
python review_logs.py events.jsonl use-case.json
python review_logs.py events.jsonl use-case.json --as-of 2026-11-01T09:06:00Z
python review_logs.py events.jsonl use-case.json --time-field received
python review_logs.py events.jsonl use-case.json --threshold 4
기본:12행/중복1/고유가용11/선택10/신원누락인증1/검토후보1. 후보auth-A/corp.example/lee/198.51.100.44의실패3·동일그룹성공1.
09:06가용기준에서는늦게도착한f3가없어후보0. 수신시각검색에서는같은3건이라도old/f1/f2로구성이바뀝니다.
실제단말·세션연결/침해성공은미확인. 후보는사람의검토대상이며외부행동0. 입력을읽고출력만하며원본/계정/제품변경없음.
종료0은계산완료(후보0포함),오류2는입력/조건오류입니다. 네트워크조회/로그인/차단/메시지/실제SIEM을실행하지않습니다.
