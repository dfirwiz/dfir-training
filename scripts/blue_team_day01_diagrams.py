"""Original mobile-sized diagrams for the first two day-one lessons."""
from html import escape

def drawing(title, boxes, arrows, foot, height):
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="{height}" viewBox="0 0 400 {height}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(foot)}</desc>',
    '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8" fill="none" stroke="#78e3c5"/></marker></defs>',
    '<style>text{font:16px sans-serif;fill:#deeee9}.heading{font-size:18px;font-weight:700}.label{font-size:14px;fill:#a8c9d5}</style>',
    f'<rect width="400" height="{height}" rx="14" fill="#0e1927"/>',f'<text class="heading" x="200" y="31" text-anchor="middle">{escape(title)}</text>']
    for points,label,x,y in arrows:
        out.append(f'<polyline points="{points}" fill="none" stroke="#78e3c5" stroke-width="2" marker-end="url(#arrow)"/>')
        if label:out.append(f'<text class="label" x="{x}" y="{y}" text-anchor="middle">{escape(label)}</text>')
    for x,y,w,h,lines in boxes:
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#152d3a" stroke="#426c7c"/>')
        for n,line in enumerate(lines):out.append(f'<text x="{x+w/2}" y="{y+(h-len(lines)*24)/2+18+n*24}" text-anchor="middle">{escape(line)}</text>')
    for n,line in enumerate(foot.split('\n')):out.append(f'<text class="label" x="200" y="{height-37+n*20}" text-anchor="middle">{escape(line)}</text>')
    out.append('</svg>');return ''.join(out)

def build_day01(assets):
    rows={
    'day01-01-mission':drawing('기록을 업무 보호로 연결하기',[
        (40,60,300,68,['수집한 활동 기록','계정 · 단말 · 네트워크']),
        (40,185,300,68,['근거와 맥락을 함께 분석','관측 범위와 가설 검증']),
        (40,310,300,68,['필요한 사람과 조치 연결','권한 · 업무 영향 · 복구']),
        (40,435,300,68,['피해 가능성과 영향 줄이기','수집 · 탐지 · 절차 개선'])],
        [('190,128 190,185','무엇을 뜻할까?',265,161),('190,253 190,310','무엇을 할까?',267,285),('190,378 190,435','효과를 확인',262,410),('340,469 370,469 370,94 340,94','',0,0)],
        '아래: 판단과 행동의 연결\n오른쪽 되돌림: 운영 개선',565),
    'day01-01-evidence':drawing('사실과 가설을 나누어 조사하기',[
        (40,60,320,74,['관측 사실','인증 성공으로 기록됨']),
        (40,192,320,74,['검증할 가설','비인가 계정 사용 가능성']),
        (40,324,320,74,['추가 증거 대조','사용자 · 단말 · 자료 접근']),
        (40,456,320,74,['판단과 남은 한계','확정 · 기각 · 추가 조사'])],
        [('185,134 185,192','맥락 추가',270,169),('185,266 185,324','반증도 찾기',270,301),('185,398 185,456','범위 명시',270,433)],
        '화살표: 조사 순서\n가설은 검증 중 바뀔 수 있음',590),
    'day01-01-time':drawing('가상 사건에서 구간별 시간 읽기',[
        (40,60,320,65,['09:00 · 최초 확인된 침입']),
        (40,185,320,65,['09:12 · 첫 유효 경보']),
        (40,310,320,65,['09:20 · 분석가 확인']),
        (40,435,320,65,['09:35 · 확산 억제 조치'])],
        [('175,125 175,185','12분 · 탐지까지',270,161),('175,250 175,310','8분 · 확인까지',270,286),('175,375 175,435','15분 · 조치까지',270,411)],
        '아래로 시간 진행 · 같은 시간 기준\n합계 35분 · 자체 가상 예제',560),
    'day01-02-boundary':drawing('호스트 자원 위에서 동작하는 VM',[
        (40,60,320,80,['실제 컴퓨터와 호스트 운영체제','CPU · 메모리 · 저장 장치']),
        (40,205,320,65,['가상화 프로그램']),
        (40,335,320,80,['게스트 운영체제와 도구','가상 CPU · 디스크 · 어댑터']),
        (40,480,320,65,['별도로 확인할 통로','공유 폴더 · 클립보드 · 네트워크'])],
        [('180,140 180,205','자원 관리',270,180),('180,270 180,335','가상 장치 제공',270,309),('180,415 180,480','설정에 따라 연결',270,454)],
        '화살표: 구성 관계와 설정 확인\nVM 사용만으로 완전 격리는 아님',610),
    'day01-02-restore':drawing('되돌리기 전에 결과 보존하기',[
        (40,60,300,68,['기준 상태 확인','설정 · 시간 · 자료 출처']),
        (40,185,300,68,['무해한 작은 실험','실행 위치와 명령 기록']),
        (40,310,300,68,['결과와 필요한 기록 보존','해시 · 조건 · 한계']),
        (40,435,300,68,['기준 상태로 복원','시간과 연결 상태 재확인'])],
        [('185,128 185,185','실험 시작',270,162),('185,253 185,310','복원보다 먼저',270,287),('185,378 185,435','복원 시험',270,412),('340,468 370,468 370,94 340,94','',0,0)],
        '되돌림: 다음 실험을 위한 재확인\n외부에 미친 효과는 취소되지 않음',565),
    'day01-02-hash':drawing('파일 내용과 해시의 비교',[
        (40,60,320,68,['직접 만든 텍스트','원본 내용과 SHA-256 기록']),
        (40,185,320,68,['바이트를 그대로 복사','사본의 해시와 비교']),
        (40,310,320,68,['작업 대상에 내용 추가','변경한 명령과 시각 기록']),
        (40,435,320,68,['변경 후 해시 다시 비교','원래 사본은 비교용으로 보존'])],
        [('185,128 185,185','내용 동일 확인',275,161),('185,253 185,310','의도한 변경',270,286),('185,378 185,435','내용 차이 확인',275,411)],
        '아래: 복사 · 변경 · 비교 순서\n해시는 안전성 판정과 별개',565)
    }
    for name,svg in rows.items():(assets/(name+'.svg')).write_text(svg,encoding='utf-8')
