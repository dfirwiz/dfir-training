"""Draw the Pivoting chapter's independent evidence diagrams."""


def build_pivot_diagrams(assets, diagram):
    items = {
        '63-pivot-path.svg': (
            '서로 다른 연결 구간',
            [['조사 앱 A', '최초 요청'], ['프록시', 'Team Server'], ['중계 지점 B', '목적지 연결'], ['문서 서비스 C', '서버 로그']],
            '왼쪽부터 요청의 진행 방향입니다. 각 구간의 연결 주소와 관측 지점을 구별합니다.',
        ),
        '63-pivot-stages.svg': (
            '프록시 요청의 처리 단계',
            [['프런트엔드', '협상과 요청'], ['세션 작업', '다음 체크인'], ['목적지 연결', 'TCP 응답'], ['서비스 요청', 'HTTP 결과']],
            '등록과 협상, 세션 처리, 목적지 연결, 응용 계층 결과는 별도의 증거입니다.',
        ),
        '63-pivot-failures.svg': (
            '실패 지점 찾기',
            [['등록 확인', 'Team Server'], ['작업 확인', '세션 기록'], ['도달 확인', '흐름 기록'], ['응답 확인', '서비스 기록']],
            '왼쪽부터 처음으로 확인되지 않은 경계를 찾아 다음 관측 지점을 정합니다.',
        ),
        '64-client-selection.svg': (
            '클라이언트 규칙과 경로 선택',
            [['규칙에 일치?', '앱 · 이름 · 포트'], ['일치', '규칙의 Action'], ['미일치', '기본 동작']],
            '위에서 아래로 분기합니다. 규칙이 일치하면 지정된 동작, 미일치하면 기본 동작을 확인합니다.',
        ),
        '64-resolution-paths.svg': (
            '프록시로 넘긴 주소형',
            [['목적지 지정', '이름 또는 숫자'], ['로컬에서 해석', '숫자 주소 전달'], ['이름을 전달', '중계 쪽에서 해석']],
            '로컬 해석으로 얻은 숫자 주소를 전달하는 경우와 이름을 전달하는 경우를 비교합니다.',
        ),
        '64-client-checks.svg': (
            '클라이언트 기록 대조',
            [['규칙 선택', '앱과 목적지'], ['주소 확인', '숫자 또는 이름'], ['TCP 연결', '응답 또는 대기'], ['서비스 처리', 'TLS · HTTP']],
            '왼쪽부터 규칙과 주소 처리, 전송 연결, 서비스 응답을 구분해 확인합니다.',
        ),
    }
    for filename, (title, labels, description) in items.items():
        if len(labels) == 3:
            positions = [(230, 25), (90, 155), (370, 155)]
            edges = [
                ('340,99 340,122 200,122 200,155', [], 0, 0),
                ('340,99 340,122 480,122 480,155', [], 0, 0),
            ]
            nodes = [(x, y, 220, 74, lines, 'decision' if i == 0 else '') for i, ((x, y), lines) in enumerate(zip(positions, labels))]
            svg = diagram(title, 680, 254, nodes, edges, description)
        else:
            nodes = [(16 + i * 180, 35, 150, 84, lines, '') for i, lines in enumerate(labels)]
            edges = [(f'{x + 150},77 {x + 180},77', [], 0, 0) for x, *_ in nodes[:-1]]
            svg = diagram(title, 722, 154, nodes, edges, description)
        (assets / filename).write_text(svg, encoding='utf-8')
