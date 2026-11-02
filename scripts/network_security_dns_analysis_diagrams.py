"""Original mobile-readable figures for DNS investigation."""
from html import escape


def build_lesson04(out):
    def begin(title, height):
        return [f'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="{height}" viewBox="0 0 400 {height}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto-start-reverse"><path d="M0 0L8 4L0 8" fill="none" stroke="#78e3c5"/></marker></defs><style>text{{font-family:Pretendard,Arial,sans-serif;fill:#dceef1;font-size:16px}}.label{{font-size:14px;fill:#a4cfc9}}.heading{{font-size:18px;font-weight:700}}</style><rect width="400" height="100%" rx="12" fill="#0e1927"/><text x="18" y="35" class="heading">{escape(title)}</text>']
    def text(p, x, y, value, cls=''):
        for i,s in enumerate(value.split('\n')):
            p.append(f'<text x="{x}" y="{y+i*23}" text-anchor="middle" class="{cls}">{escape(s)}</text>')
    def box(p, y, value, h=76, fill='#15312f'):
        p.append(f'<rect x="30" y="{y}" width="340" height="{h}" rx="10" fill="{fill}" stroke="#4c7c83"/>')
        lines=len(value.split('\n'));text(p,200,y+(h-(lines-1)*23)/2+5,value)
    def line(p,y1,y2,both=False,gap=None):
        path=f'M200 {y1}V{gap[0]} M200 {gap[1]}V{y2}' if gap else f'M200 {y1}V{y2}'
        p.append(f'<path d="{path}" fill="none" stroke="#78e3c5" stroke-width="2" marker-end="url(#arrow)"'+(' marker-start="url(#arrow)"' if both else '')+'/>')
    def save(p,name): (out/name).write_text(''.join(p)+'</svg>',encoding='utf-8')

    p=begin('그림 1 · DNS 수집 위치와 출발지',760)
    box(p,80,'직원 단말\n192.0.2.25')
    line(p,156,300,gap=(180,250));text(p,200,207,'관측점 A · 질문 출발지','label');text(p,200,232,'192.0.2.25','label')
    box(p,300,'회사 전달 서버\n192.0.2.53')
    line(p,376,520,gap=(400,470));text(p,200,427,'관측점 B · 질문 출발지','label');text(p,200,452,'192.0.2.53','label')
    box(p,520,'상위 재귀 리졸버\n198.51.100.53')
    text(p,200,650,'화살표: 질문 방향 · 응답은 반대 방향','label')
    text(p,200,684,'B에서 최초 단말을 바로 특정할 수 없음','label')
    text(p,200,717,'캐시가 있으면 B의 질문은 줄어듦','label')
    save(p,'lesson04-observation.svg')

    p=begin('그림 2 · 경보를 조사 판단으로 연결',760)
    for y,value in [(75,'수집 위치·시간·누락 확인'),(205,'원본 질문·응답과 단말 연결'),(335,'평판·나이·정상 기준선 보강'),(465,'실행·연결·파일·서버 기록 대조'),(595,'사실 / 가설 / 미확인 결론 기록')]:
        box(p,y,value,65)
        if y<595:line(p,y+65,y+130)
    text(p,200,704,'아래 방향: 조사 진행 · 경보 ≠ 침해 확정','label')
    save(p,'lesson04-investigation.svg')

    p=begin('그림 3 · 승인 DNS를 경유하는 터널',810)
    box(p,80,'단말의 프로그램\n192.0.2.25')
    line(p,156,315,True,gap=(180,265))
    text(p,200,207,'질문 ↓ 데이터 조각을 이름에 표현','label')
    text(p,200,242,'응답 ↑ 레코드 데이터로 회신','label')
    box(p,315,'승인 리졸버\n질의를 권한 서버로 전달')
    line(p,391,550,True,gap=(415,500))
    text(p,200,444,'새 이름이면 캐시로 답하지 못할 수 있음','label')
    text(p,200,477,'이름·종류·정책에 따라 동작이 달라짐','label')
    box(p,550,'터널 운영자의 권한 서버\ncollect.example.net')
    text(p,200,688,'양방향 화살표: 질문·응답','label')
    text(p,200,724,'직접 외부 DNS만 막아서는 충분하지 않음','label')
    text(p,200,760,'외부 서버에 직접 질문하는 별도 경로도 가능','label')
    save(p,'lesson04-tunnel.svg')

    p=begin('그림 4 · 닮은 글자와 다른 식별자',650)
    box(p,80,'영문 a · U+0061\n키릴 문자 а · U+0430',95)
    text(p,200,215,'모양이 비슷해도 문자 번호는 다름','label')
    box(p,260,'Unicode 레이블 예제\nexаmple')
    line(p,336,430);text(p,280,386,'표현 변환','label')
    box(p,430,'ASCII 레이블 표현\nxn--exmple-4nf')
    text(p,200,565,'예제 접미사: .example · 실제 접속 없음','label')
    text(p,200,601,'변환 ≠ 암호화 · IDN 자체는 정상 기능','label')
    save(p,'lesson04-idn.svg')

    p=begin('그림 5 · HTTP/2 DoH의 캡슐화',690)
    for x,y,w,h,fill in [(25,80,350,400,'#152d3a'),(50,170,300,285,'#15312f'),(75,270,250,125,'#203d45')]:
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="#6fabb3"/>')
    text(p,200,124,'TLS · 내용 보호')
    text(p,200,217,'HTTP/2 · 요청·응답 스트림')
    text(p,200,315,'DNS 메시지\n질문 이름·종류·응답')
    text(p,200,528,'밖에서: 주소·시간·양 등','label')
    text(p,200,563,'복호화 후: HTTP와 DNS 내용 확인 가능','label')
    text(p,200,609,'요청 → 리졸버 / 응답 → 단말','label')
    text(p,200,649,'예: HTTP/2 · HTTP/3와 DoQ는 다른 구조','label')
    save(p,'lesson04-doh.svg')
