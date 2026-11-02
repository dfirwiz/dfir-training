"""Responsive, original explanatory figures for DNS fundamentals."""
from html import escape

def build_lesson03(out):
    def begin(title,h):
        return [f'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="{h}" viewBox="0 0 400 {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto-start-reverse"><path d="M0 0L8 4L0 8" fill="none" stroke="#78e3c5"/></marker></defs><style>text{{font-family:Pretendard,Arial,sans-serif;fill:#dceef1;font-size:16px}}.title{{font-size:18px;font-weight:700}}.label{{font-size:14px;fill:#96cfc5}}</style><rect width="400" height="100%" rx="12" fill="#0e1927"/><text class="title" x="17" y="34">{escape(title)}</text>']
    def text(p,x,y,s,cls='',size=None):
        lines=s.split('\n')
        for i,v in enumerate(lines):p.append(f'<text x="{x}" y="{y+(i-(len(lines)-1)/2)*23}" text-anchor="middle" class="{cls}"'+(f' style="font-size:{size}px"' if size else '')+f'>{escape(v)}</text>')
    def box(p,x,y,w,h,s):
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#15312f" stroke="#4c7c83"/>');text(p,x+w/2,y+h/2+6,s)
    def line(p,pts,both=False,arrow=True):
        p.append(f'<polyline points="{pts}" fill="none" stroke="#78e3c5" stroke-width="2"'+(' marker-end="url(#a)"' if arrow else '')+(' marker-start="url(#a)"' if both else '')+'/>')
    def save(p,name):(out/name).write_text(''.join(p)+'</svg>',encoding='utf-8')
    p=begin('그림 1 · DNS 질문을 맡기고 답을 구하는 경로',900)
    box(p,65,70,310,60,'단말 · 스텁 리졸버')
    line(p,'215,130 215,185',True);text(p,115,163,'질의 ↓ 응답 ↑','label')
    box(p,65,185,310,60,'회사 전달 서버 · 캐시 가능')
    line(p,'215,245 215,300',True);text(p,115,278,'질의 ↓ 응답 ↑','label')
    box(p,65,300,310,70,'재귀 리졸버\n최종 답을 구하고 캐시')
    line(p,'65,335 30,335 30,750',arrow=False)
    for y,s in [(460,'① 루트 쪽 서버\ncom의 담당 서버 안내'),(580,'② com 쪽 서버\nexample.com의 담당 서버 안내'),(700,'③ example.com 권한 서버\nportal.example.com의 주소 응답')]:
        line(p,f'30,{y+40} 75,{y+40}',True)
        box(p,75,y,300,80,s)
    text(p,200,820,'①②③의 질의 주체는 모두 재귀 리졸버','label')
    text(p,200,851,'가지의 양방향 선: 질의와 회신','label')
    text(p,200,878,'캐시가 없을 때의 단순화된 예제','label')
    save(p,'lesson03-resolution-path.svg')
    p=begin('그림 2 · TTL 300초의 기본 캐시 시간선',590)
    for y,s in [(80,'처음 응답 · 경과 0초\nTTL 300초'),(250,'같은 질문 · 경과 120초\n남은 TTL 180초 · 캐시로 응답'),(420,'경과 300초 · 기본 만료 시점\n새 조회 등 갱신 필요')]:
        box(p,20,y,360,82,s)
        if y<420:line(p,f'200,{y+82} 200,{y+170}')
    text(p,200,550,'단위: 초 · 정책·사전 갱신·serve-stale는 별도','label')
    save(p,'lesson03-cache-ttl.svg')
    p=begin('그림 3 · 이름과 주소의 다대다 관계',590)
    box(p,15,85,175,65,'portal.example.com')
    box(p,15,245,175,65,'files.example.net')
    box(p,235,85,150,65,'203.0.113.20')
    box(p,235,245,150,65,'203.0.113.21')
    line(p,'190,117 235,117');text(p,212,98,'A','label')
    line(p,'190,135 210,135 210,270 235,270');text(p,220,205,'A','label')
    line(p,'190,277 200,277 200,140 235,140');text(p,170,220,'A','label')
    box(p,65,425,270,65,'edge.example.com')
    line(p,'310,150 370,150 370,457 335,457');text(p,310,370,'PTR · 별도 관리','label')
    text(p,200,535,'A: 이름 → IPv4 · PTR: 역방향 이름 공간','label')
    text(p,200,566,'같은 주소 ≠ 같은 운영 주체·같은 콘텐츠','label')
    save(p,'lesson03-many-to-many.svg')
    p=begin('그림 4 · CNAME 연결과 순환',780)
    for y,s in [(75,'www.example.com · 별칭'),(205,'edge.example.com · 대상 이름'),(335,'203.0.113.20 · 주소')]:
        box(p,40,y,320,60,s)
        if y<335:line(p,f'200,{y+60} 200,{y+130}')
    text(p,280,177,'CNAME','label');text(p,270,307,'A','label')
    text(p,200,446,'아래는 최종 주소에 도달하지 못하는 순환','label')
    box(p,80,485,240,60,'a.example.com')
    box(p,80,625,240,60,'b.example.com')
    line(p,'80,515 35,515 35,655 80,655');text(p,70,590,'CNAME','label')
    line(p,'320,655 365,655 365,515 320,515');text(p,330,590,'CNAME','label')
    text(p,200,743,'화살표: 이름을 따라가는 방향 · HTTP 이동 아님','label')
    save(p,'lesson03-cname-chain.svg')
