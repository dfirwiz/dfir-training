"""Create protocol and evidence diagrams for the Kerberos chapter."""


def build_kerberos_exchange_diagrams(assets, diagram):
    items = {
        '67-as-exchange.svg': ('첫 발급의 흐름', [
            ['클라이언트', '주체와 렐름'], ['AS 요청', '사전 인증'], ['KDC 판단', '요청 검증'], ['AS 응답', 'TGT와 키'],
        ], '클라이언트의 AS 요청, KDC의 검증, 첫 티켓 발급을 순서대로 확인합니다.'),
        '67-as-key-copies.svg': ('AS 응답의 두 영역', [
            ['AS-REP', '두 암호화 영역'], ['클라이언트 영역', '응답 키로 확인'], ['TGT 내부', 'TGS 키로 확인'],
        ], '같은 세션 키가 서로 다른 장기 신뢰 경계에 맞춰 보호됩니다.'),
        '67-as-outcomes.svg': ('사전 인증과 발급', [
            ['AS 요청 도착', '정책과 자료 대조'], ['자료 필요·실패', '방식과 코드 확인'], ['검증 성공', 'TGT 발급 관측'],
        ], '정책과 실제 자료에 따라 다른 결과를 관측합니다.'),
        '68-tgs-ap-flow.svg': ('서비스 요청의 세 경계', [
            ['서비스 이름', '요청 대상'], ['KDC', '티켓 발급'], ['서비스', '티켓 인증'], ['자원 정책', '동작 인가'],
        ], '발급과 서비스 인증, 실제 자원 인가를 왼쪽부터 구분합니다.'),
        '68-tgs-key-copies.svg': ('서비스 세션 키 전달', [
            ['TGS-REP', '두 암호화 영역'], ['응답 영역', 'TGT 키 또는 하위 키'], ['서비스 티켓', '서비스 장기 키'],
        ], '클라이언트와 서비스가 각각 다른 보호 영역에서 서비스 세션 키를 얻습니다.'),
        '68-ticket-observation.svg': ('관측을 연결하는 순서', [
            ['DC 기록', '요청과 결과'], ['대상 연결', '이름과 시각'], ['인증 기록', '계정과 방식'], ['서비스 감사', '동작과 결과'],
        ], '발급부터 실제 작업까지 시각과 문맥을 대조합니다.'),
    }
    for name, (title, labels, description) in items.items():
        if len(labels) == 3:
            nodes = [
                (230, 25, 220, 74, labels[0], 'decision'),
                (90, 155, 220, 74, labels[1], ''),
                (370, 155, 220, 74, labels[2], ''),
            ]
            edges = [
                ('340,99 340,122 200,122 200,155', [], 0, 0),
                ('340,99 340,122 480,122 480,155', [], 0, 0),
            ]
            svg = diagram(title, 680, 254, nodes, edges, description)
        else:
            nodes = [(16 + i * 180, 35, 150, 84, lines, '') for i, lines in enumerate(labels)]
            edges = [(f'{x + 150},77 {x + 180},77', [], 0, 0) for x, *_ in nodes[:-1]]
            svg = diagram(title, 722, 154, nodes, edges, description)
        (assets / name).write_text(svg, encoding='utf-8')
