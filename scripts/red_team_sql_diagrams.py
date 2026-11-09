"""Build the SQL Server chapter diagrams."""


def build_sql_diagrams(assets, diagram):
    items = {
        '73-sql-evidence.svg': ('서버 연결의 증거 층', [
            ['이름 확인', 'DNS와 SPN'], ['리스너', 'TCP 도달'], ['SQL 교환', '연결 보안'], ['엔진 로그인', '세션 성립'],
        ], '이름과 네트워크, 연결 보안과 로그인은 서로 다른 근거입니다.'),
        '73-sql-browser.svg': ('명명된 인스턴스 연결', [
            ['클라이언트', '포트 선택'], ['Browser 조회', 'UDP 1434'], ['포트 직접 지정', '엔진 TCP'],
        ], 'Browser를 통해 포트를 확인하거나 알려진 엔진 포트로 직접 연결할 수 있습니다.'),
        '73-sql-triage.svg': ('연결 실패 지점 확인', [
            ['주소와 이름', '대상 식별'], ['포트 응답', '경로 확인'], ['인증서', '신뢰 확인'], ['로그인 기록', '엔진 처리'],
        ], '실패한 단계와 그 단계의 기록을 대조합니다.'),
        '74-sql-principal-map.svg': ('SQL 권한의 경계', [
            ['인스턴스', '로그인 확인'], ['DB 매핑', '사용자 문맥'], ['유효 권한', '역할과 부여'], ['객체 요청', '결과 확인'],
        ], '로그인과 DB 사용자 및 실제 객체 권한을 구별합니다.'),
        '74-sql-metadata.svg': ('객체 가시성과 데이터 권한', [
            ['데이터베이스', '선택 범위'], ['메타데이터', '정의와 이름'], ['데이터 권한', '객체별 판정'],
        ], '객체가 보이는 조건과 데이터를 읽을 수 있는 조건을 따로 확인합니다.'),
        '74-sql-query-triage.svg': ('세션 조사 순서', [
            ['원래 로그인', '세션의 시작'], ['현재 문맥', '실행 주체'], ['현재 DB', '사용자와 범위'], ['작업 결과', '허용 또는 거부'],
        ], '세션의 시작과 현재 문맥을 함께 기록합니다.'),
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
