"""Build domain trust and directory audit diagrams."""


def build_domain_diagrams(assets, diagram):
    items = {
        '79-replication-flow.svg': ('정상 디렉터리 복제', [
            ['원본 변경', 'DC에 기록'], ['변경 요청', '수신 DC'], ['응답 처리', '변경분 확인'], ['사본 갱신', '범위별 반영'],
        ], '도메인 컨트롤러 사이에서 요청과 응답이 오가는 흐름입니다.'),
        '79-replication-rights.svg': ('권한과 업무 승인', [
            ['복제 요청', '주체와 범위'], ['유효 권한', '그룹과 상속'], ['승인 자료', '업무와 대상'],
        ], '기술적 접근 권한과 업무 승인을 별도로 확인합니다.'),
        '79-replication-evidence.svg': ('복제 사건의 관측 단계', [
            ['권한', '설정 상태'], ['요청', '주체와 경로'], ['처리', 'DC 감사'], ['노출', '반환 범위'],
        ], '권한과 실제 반환을 서로 다른 증거로 기록합니다.'),
        '80-dcsync-correlation.svg': ('증거를 묶는 기준', [
            ['동일 DC', '호스트와 시간'], ['디렉터리 감사', '객체와 권한'], ['로그온과 흐름', '주체와 출발지'],
        ], '이벤트와 흐름 자료에서 관측 범위를 대조합니다.'),
        '80-dcsync-join.svg': ('로그온과 작업 연결', [
            ['로그온 기록', '같은 DC'], ['세션 대조', 'ID와 계정'], ['객체 감사', '권한과 시각'], ['흐름 보강', '출발지 확인'],
        ], '로그온 ID를 같은 DC에서 대조하고 네트워크 기록으로 보강합니다.'),
        '80-dcsync-triage.svg': ('정상 기준선 대조', [
            ['요청 확인', '계정과 호스트'], ['업무 예외', '승인 내역 대조'], ['미확인 경로', '영향 범위 조사'],
        ], '승인된 동기화 예외와 예상 밖의 요청을 나눠 조사합니다.'),
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
