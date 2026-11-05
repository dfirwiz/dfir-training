20강 출처별 이름 관계 비교 실습
네파일을같은폴더에저장:comparison.json,compare_names.py,analysis-notes.txt,README.txt
Python표준라이브러리만사용.실제TIP/API/위협조사/네트워크조회가아닙니다.
python compare_names.py comparison.json
python compare_names.py comparison.json --label "Training Lark"
python compare_names.py comparison.json --record-id B-2026
기본결과:같은출처정체성A-2022/A-2026,직접중첩후보B-2026,같은이름의별도기록C-2026.
Training Lark는두기록이있어ambiguous_label이며자동병합하지않습니다.
종료0은계산성공으로실제행위자판명이나이름의유일성을보장하지않습니다.입력오류는2입니다.
프로그램은입력을읽고화면출력만합니다.외부조회/귀속확정/파일변경/차단이없습니다.
