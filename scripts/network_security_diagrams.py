"""Vector versions of the reviewed lesson-two explanatory diagrams."""
from html import escape

def build_lesson02(out):
    def start(title, height):
        return [f'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="{height}" viewBox="0 0 400 {height}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8" fill="#71e3c0"/></marker></defs><style>text{{font-family:Pretendard,Arial,sans-serif;fill:#c3d7e7;font-size:16px}}.title{{font-size:19px;font-weight:700;fill:#e7f4ff}}.node{{font-size:17px;font-weight:700;fill:#e6f5ff}}.small{{font-size:13px}}.label{{font-size:14px;fill:#83dfcc}}</style><rect width="400" height="100%" rx="12" fill="#0c1522"/><text class="title" x="20" y="39">{escape(title)}</text>']
    def text(p,x,y,value,cls='',size=None):
        lines=value.split('\n')
        for i,line in enumerate(lines):
            p.append(f'<text x="{x}" y="{y+(i-(len(lines)-1)/2)*24}" text-anchor="middle" class="{cls}"'+(f' style="font-size:{size}px"' if size else '')+f'>{escape(line)}</text>')
    def box(p,x,y,w,h,title,sub='',color='#15312f'):
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="11" fill="{color}" stroke="#4c7c83"/>')
        text(p,x+w/2,y+(h/2+6 if not sub else 29),title,'node')
        if sub:text(p,x+w/2,y+62,sub,size=15)
    def line(p,points,arrow=True):
        p.append(f'<polyline points="{points}" fill="none" stroke="#71e3c0" stroke-width="2"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
    def save(p,name):
        (out/name).write_text(''.join(p)+'</svg>',encoding='utf-8')
    p=start('그림 1 · 같은 통신, 세 종류의 기록',650)
    box(p,55,70,310,60,'관측 지점을 지나는 통신')
    line(p,'55,100 30,100 30,525',False)
    for y,title,sub,label in [(185,'플로 요약','주소·포트·시간·양','장비가 통신을 요약해 전송'),(335,'애플리케이션 메타데이터','DNS 질문·HTTP 요청 등의 필드','센서가 패킷을 해석해 기록'),(485,'패킷 원본','캡처한 패킷 바이트와 시간','센서가 패킷을 파일로 저장')]:
        line(p,f'30,{y+40} 70,{y+40}')
        text(p,220,y-17,label,'label')
        box(p,70,y,305,83,title,sub)
    text(p,200,621,'화살표: 자료 생성 경로 · 세 자료는 별도 산출물','small')
    save(p,'lesson02-capture-records.svg')
    p=start('그림 2 · Wireshark의 세 가지 보기',625)
    box(p,20,75,360,105,'① 패킷 목록','한 줄은 캡처한 패킷 기록 하나\n시간 · 출발지 · 목적지 · 프로토콜')
    line(p,'200,180 200,235');text(p,285,214,'패킷 선택','label')
    box(p,20,235,360,120,'② 패킷 상세','선택한 패킷을 필드로 해석\nFrame → Ethernet → IP → TCP → HTTP')
    line(p,'200,355 200,410');text(p,285,391,'필드 선택','label')
    box(p,20,410,360,115,'③ 패킷 바이트','예: G E T에 해당하는 값\n16진수 47 45 54',color='#192a40')
    text(p,200,576,'화살표: 선택에 따른 보기의 연결',size=14)
    text(p,200,604,'실제 도구 화면이 아닌 설명용 구성도','small')
    save(p,'lesson02-wireshark-panes.svg')
    p=start('그림 3 · 요약에서 증거로 내려가는 조사',755)
    for y,title,sub in [(75,'① 플로 요약','누가 누구와, 언제, 얼마나 통신했나?'),(225,'② 애플리케이션 기록','어떤 요청과 응답을 해석했나?'),(375,'③ 관련 패킷 원본','당시 수집한 바이트가 무엇인가?'),(525,'④ 단말·서버 기록','어떤 프로그램이 실행·저장했나?')]:
        box(p,20,y,360,91,title,sub)
        if y<525:line(p,f'200,{y+91} 200,{y+150}')
    text(p,200,676,'화살표: 조사 자료를 연결하는 순서',size=14)
    text(p,200,714,'연결 기준: 시간 · 주소·포트 · 센서 · 연결 식별자','small')
    save(p,'lesson02-investigation-flow.svg')
