둘째 날8강 독립 가상 자료입니다. 실제 사건이나 원래 워크북 실습이 아닙니다.
complete.pcap 3프레임 / missing-tail.pcap 2프레임, 고정 IPv4/TCP/HTTP1.1 한 대화입니다. 연결 성립/종료 프레임은 생략했습니다.
내용은 Training only.와 줄바꿈뿐입니다. 악성 파일/스크립트/실제 인증정보는 없습니다.
python explore_encoding.py
python inspect_intervals.py intervals.csv
python inspect_http.py complete.pcap
python inspect_http.py missing-tail.pcap
앞의 두 프로그램은 Python 표준 라이브러리만, 마지막은 dpkt가 필요합니다. 검증 환경 Python3.12.14/dpkt1.9.8.
inspect_http.py는 이 작은 고정 자료 전용입니다. 일반 TCP/IPv6/다중대화/TLS/HTTP2/HTTP3/청크/임의압축 분석기가 아닙니다.
입력만 읽고 JSON을 출력합니다. 복원한 바이트를 실행하거나 외부로 보내지 않습니다. 추출 파일도 자동 저장하지 않습니다.
expected-note.txt는 비교용 원문, intervals.csv는 패킷과 별도로 만든 가상 요청 시각입니다. CSV를 PCAP 관측이라고 해석하지 않습니다.
정상 종료0은 계산 완료(불완전 본문 포함), 오류2는 지원 범위/입력 오류입니다. 침해 성공 판단은 미확인으로 유지합니다.
