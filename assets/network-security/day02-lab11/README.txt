둘째 날11강 독립 실습입니다. 원본 워크북·실제 사건·실제 TLS 자료가 아닙니다.
같은 폴더에 case.json/correlate_case.py와 앞선8강의 inspect_http.py/complete.pcap/missing-tail.pcap을 내려받으세요.
Python과 dpkt가 있는 환경에서 실행합니다. 실제 검증 Python3.12.14/dpkt1.9.8. 이번 검증에는 기존 설치 자료를 사용했고 새 설치를 하지 않았습니다.
python correlate_case.py case.json complete.pcap
python correlate_case.py case.json missing-tail.pcap
PCAP 해석은 기존 inspect_http.py의 제한된 고정 Ethernet/IPv4/TCP/HTTP1.1 자료 전용입니다. 범용 패킷 분석기가 아닙니다.
case.json의 단말·TLS·시간은 패킷과 별도로 만든 가상 주장입니다. 동일 해시 비교와 시차 계산이 실제 단말·실행·인과관계를 검증하지 않습니다.
기준 시각은 분석가가 입력한 가상 시각입니다. PCAP 시각과 단말 시각을 연결한 계산이 아닙니다.
불완전 본문은 해시 비교를 null로 남깁니다. false(계산해서 불일치)와 null(자료 부족으로 미계산)을 구별하세요.
입력 자료만 읽고 JSON을 출력합니다. 네트워크 요청·TLS 연결·복호화·입력 내용 실행·제품 설정 변경은 하지 않습니다.
종료0은 계산 완료(자료 부족·불일치 포함),오류2는 입력/의존성/지원 범위 오류입니다. 모든 사건 판정은 unresolved입니다.
