"""Original responsive figures for HTTP fundamentals."""
from html import escape

def build_lesson06(out):
    def start(title,h):
        return [f'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="{h}" viewBox="0 0 400 {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto-start-reverse"><path d="M0 0L8 4L0 8" fill="none" stroke="#78e3c5"/></marker></defs><style>text{{font-family:Pretendard,Arial,sans-serif;fill:#dceef1;font-size:16px}}.label{{font-size:14px;fill:#a4cfc9}}.heading{{font-size:18px;font-weight:700}}</style><rect width="400" height="100%" rx="12" fill="#0e1927"/><text x="16" y="35" class="heading">{escape(title)}</text>']
    def text(p,x,y,s,cls=''):
        for i,t in enumerate(s.split('\n')):p.append(f'<text x="{x}" y="{y+i*23}" text-anchor="middle" class="{cls}">{escape(t)}</text>')
    def box(p,y,s,h=76,x=30,w=340,fill='#15312f'):
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="#4c7c83"/>')
        text(p,x+w/2,y+(h-(len(s.split('\n'))-1)*23)/2+5,s)
    def arrow(p,points):p.append(f'<polyline points="{points}" fill="none" stroke="#78e3c5" stroke-width="2" marker-end="url(#a)"/>')
    def save(p,name):(out/name).write_text(''.join(p)+'</svg>',encoding='utf-8')

    p=start('그림 1 · 웹 동작의 단계와 증거',790)
    items=[(75,'DNS · 주소 안내\n어디로 연결할지 확인'),(205,'연결과 통신 보호\nTCP+TLS 또는 QUIC 등'),(335,'HTTP 요청\n어느 자원에 무엇을 요청했는가'),(465,'HTTP 응답\n코드·헤더·본문을 무엇으로 받았는가'),(595,'클라이언트의 후속 처리\n화면 표시·저장·실행은 별도 단계')]
    for y,s in items:
        box(p,y,s)
        if y<595:arrow(p,f'200,{y+76} 200,{y+130}')
    text(p,200,725,'아래: 단순화한 진행 · 캐시·기존 연결은 생략 가능','label')
    text(p,200,760,'한 단계의 성공 ≠ 다음 단계의 성공','label')
    save(p,'lesson06-web-flow.svg')

    p=start('그림 2 · 요청 ↓ 응답 ↑ 구조 읽기',820)
    box(p,75,'클라이언트 · 브라우저 등')
    box(p,230,'메서드 · 요청 대상\nHTTP 버전\nHost 등 헤더\n빈 줄\n필요한 요청 본문',h=260,x=20,w=175)
    box(p,230,'상태 코드\n응답 헤더\nContent-Type 등\n빈 줄\n응답 본문',h=260,x=225,w=155,fill='#183047')
    box(p,650,'서버 · 프록시·애플리케이션 등')
    arrow(p,'108,151 108,230');arrow(p,'108,490 108,520');arrow(p,'108,580 108,650')
    arrow(p,'303,650 303,580');arrow(p,'303,520 303,490');arrow(p,'303,230 303,151')
    text(p,108,552,'요청 방향 ↓','label');text(p,303,552,'응답 방향 ↑','label')
    text(p,200,770,'HTTP/1.1 설명 · 메시지와 패킷은 다른 단위','label')
    save(p,'lesson06-message.svg')

    p=start('그림 3 · 조각에서 읽을 수 있는 본문까지',750)
    text(p,200,78,'필요한 복호화 자료를 확보한 상황을 가정','label')
    for y,s in [(110,'전송 데이터 재조립\n누락·순서·세션 범위 확인'),(250,'메시지 프레이밍 해석\n예: HTTP/1.1 청크 구분 제거'),(390,'Content-Encoding 처리\n예: gzip 압축 해제'),(530,'문자·콘텐츠 해석\n예: UTF-8로 HTML 읽기')]:
        box(p,y,s)
        if y<530:arrow(p,f'200,{y+76} 200,{y+140}')
    text(p,200,674,'도구가 이미 처리한 단계는 중복 적용하지 않기','label')
    text(p,200,711,'압축 해제 후 크기 ≠ 압축된 전송 크기','label')
    save(p,'lesson06-decoding.svg')

    p=start('그림 4 · 한 연결에서 두 스트림 추적',800)
    items=[(85,'스트림 1 · 요청 HEADERS\nGET /reports','#15312f'),(235,'스트림 3 · 요청 HEADERS\nGET /style.css','#183047'),(385,'스트림 3 · 응답 HEADERS·DATA\n200 · 스타일 데이터','#183047'),(535,'스트림 1 · 응답 HEADERS·DATA\n200 · 보고서 데이터','#15312f')]
    for y,s,c in items:box(p,y,s,h=90,x=50,w=300,fill=c)
    arrow(p,'50,130 22,130 22,580 50,580')
    arrow(p,'350,280 378,280 378,430 350,430')
    text(p,200,686,'위 → 아래: 관측 순서 · 선: 같은 스트림의 대응','label')
    text(p,200,721,'번호는 동일 TCP 연결 안에서 해석','label')
    text(p,200,756,'각 상자는 패킷 한 개를 뜻하지 않음','label')
    save(p,'lesson06-streams.svg')

    p=start('그림 5 · 확보한 자료와 판단 범위',780)
    for y,s in [(75,'네트워크 외부 관측\n주소·시각·양 · 본문은 숨겨질 수 있음'),(215,'필요한 추가 자료 선택\n프록시·서버·단말 로그와 보존 범위'),(355,'필요한 경우 해석·복호화\n같은 세션·키·도구 지원 확인'),(495,'내용과 후속 행동 대조\n메시지 완전성·파일·인증·실행 기록')]:
        box(p,y,s)
        if y<495:arrow(p,f'200,{y+76} 200,{y+140}')
    arrow(p,'200,571 200,635');box(p,635,'관측 사실 / 지지되는 가설 / 미확인 결론',h=60)
    text(p,200,747,'아래 방향: 필요한 자료를 확인하며 판단','label')
    save(p,'lesson06-visibility.svg')
