22강 독립 가상 시간 비교
events.json, review_time.py, field-notes.txt, README.txt를 같은 폴더에 둡니다.
Python 표준 라이브러리만 사용합니다. 실제 Colonial Pipeline 기록·제품 API·PCAP 분석이 아닙니다.
python review_time.py events.json
python review_time.py events.json --left decision --right paused
python review_time.py events.json --left decision --right paused --extra-uncertainty-seconds 60
기본: 명목 시각 차이20초, 각 ±30초로 순서 미해결. decision/paused:120초 차이, 엄격 시간 순서는 before.
추가 불확실성60초를 양쪽에 더하면 순서 미해결입니다. 인과관계는 모든 경우 미검증입니다.
종료0: 비교 계산 성공. 종료2: 입력 오류. 입력을 읽고 화면에 출력하며 파일 변경·외부 조회·조치 없음.
