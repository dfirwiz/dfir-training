둘째 날13강 독립 가상 SPF 조건 계산입니다. 실제 SMTP·DNS·원본 워크북 자료가 아닙니다.
Python 표준 라이브러리만 사용합니다. python check_spf_subset.py cases.json
지원 범위는 v=spf1 뒤 ip4/ip6/all과 + - ~ ? 한정입니다. 형식을 먼저 검사한 뒤 앞에서부터 첫 일치를 계산합니다.
이 부분집합은 소문자 표기와 정규 네트워크 주소만 받습니다. 예컨대 192.0.2.0/24는 받지만 호스트 비트가 남는 192.0.2.25/24는 거부합니다. 실제 SPF의 모든 유효 표기·CIDR 처리와 같다는 뜻은 아닙니다.
include/a/mx/ptr/exists/redirect/매크로/DNS 조회·오류·조회 한도·실제 SMTP 신원 추출은 구현하지 않습니다.
미지원 입력의 오류2는 교육용 도구의 지원 범위 오류입니다. 실제 SPF permerror와 같지 않습니다.
record:null은 작성자가 SPF 자료가 없다고 넣은 가정입니다. 실제 DNS에서 정책 부재를 관측한 결과가 아닙니다.
표시 From을 바꿔도 이 계산은 사용하지 않습니다. 모든 출력에서 real_spf_verified와 displayed_author_verified는 false입니다.
입력을 읽고 결과만 출력합니다. 메일 발송·서버 접속·DNS 변경·스팸 차단은 하지 않습니다. 종료0은 계산 완료이며 사건 판정은 unresolved입니다.
