"""Original explanatory SVGs for the offline DNS lab."""
from html import escape

def build_lesson05(out):
    def start(title,h):
        return [f'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="{h}" viewBox="0 0 400 {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto-start-reverse"><path d="M0 0L8 4L0 8" fill="none" stroke="#78e3c5"/></marker></defs><style>text{{font-family:Pretendard,Arial,sans-serif;fill:#dceef1;font-size:16px}}.label{{font-size:14px;fill:#a4cfc9}}.heading{{font-size:18px;font-weight:700}}</style><rect width="400" height="100%" rx="12" fill="#0e1927"/><text x="16" y="35" class="heading">{escape(title)}</text>']
    def text(p,x,y,s,cls=''):
        for i,t in enumerate(s.split('\n')):p.append(f'<text x="{x}" y="{y+i*23}" text-anchor="middle" class="{cls}">{escape(t)}</text>')
    def box(p,y,s,h=76,x=30,w=340,dashed=False):
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#15312f" stroke="#4c7c83"'+(' stroke-dasharray="7 5"' if dashed else '')+'/>')
        text(p,x+w/2,y+(h-(len(s.split('\n'))-1)*23)/2+5,s)
    def arrow(p,points,dashed=False):p.append(f'<polyline points="{points}" fill="none" stroke="#78e3c5" stroke-width="2" marker-end="url(#a)"'+(' stroke-dasharray="7 5"' if dashed else '')+'/>')
    def save(p,f):(out/f).write_text(''.join(p)+'</svg>',encoding='utf-8')
    p=start('그림 1 · 역할별 DNS 경로와 관측점',800)
    box(p,75,'직원 단말 WS25 · WS26\n192.0.2.25 · 192.0.2.26')
    arrow(p,'180,151 180,280');text(p,92,206,'단말 쪽\nPCAP','label')
    box(p,280,'승인 전달 서버\n192.0.2.53')
    arrow(p,'180,356 180,505');text(p,95,415,'상위 쪽\nPCAP','label')
    box(p,505,'상위 리졸버\n198.51.100.53')
    arrow(p,'370,113 385,113 385,543 370,543',True)
    text(p,200,635,'실선: 역할별 승인 경로의 질문 방향','label')
    text(p,200,670,'점선: 직원의 직접 질문 · 예제 정책과 다름','label')
    text(p,200,705,'상위 PCAP은 일부 대화만 담은 별도 파일','label')
    text(p,200,750,'실제 수집·전송 없는 자체 합성 자료','label')
    save(p,'lesson05-topology.svg')
    p=start('그림 2 · 같은 ID, 서로 다른 응답 짝',700)
    for y,s in [(80,'1번 · WS25 질문\nportal.example.com A'),(215,'2번 · WS26 질문\nfiles.example.net AAAA'),(350,'3번 · WS26에 응답\n2번 질문의 주소·포트와 대응'),(485,'4번 · WS25에 응답\n1번 질문의 주소·포트와 대응')]:box(p,y,s,x=60,w=280)
    arrow(p,'60,118 25,118 25,523 60,523')
    arrow(p,'340,253 375,253 375,388 340,388')
    text(p,200,610,'네 메시지 모두 ID 0x1001','label')
    text(p,200,642,'위 → 아래: 파일 순서 · 연결선: 실제 대응','label')
    text(p,200,674,'주소·포트·이름·종류·시각을 함께 확인','label')
    save(p,'lesson05-pairing.svg')
    p=start('그림 3 · 증거를 연결해도 남는 질문',730)
    box(p,75,'PCAP에서 읽은 내용\nTXT 질문 8행 · 고유 이름 6개')
    box(p,205,'가상 단말 기록의 맥락\n같은 실행의 파일 읽기·질의')
    arrow(p,'200,151 200,205')
    arrow(p,'200,281 200,360')
    box(p,360,'조사 가설\n데이터 전송 목적이 있었을 가능성')
    arrow(p,'200,436 200,525',True)
    box(p,525,'별도 근거가 필요한 결론\n그 파일의 외부 수신·복원·유출 성공',dashed=True)
    text(p,200,655,'실선: 자료 대조 · 점선: 추가 확인 필요','label')
    text(p,200,690,'이번 PCAP의 내용은 무해한 학습 표식','label')
    save(p,'lesson05-evidence.svg')
    p=start('그림 4 · UDP 잘림 뒤의 TCP 조회',900)
    items=[(75,'39번 · UDP 질문\nlarge.example.org TXT'),(205,'40번 · UDP 응답\nTC=1 · 답 레코드 없음'),(335,'41~43번 · TCP 연결 수립\nSYN → SYN/ACK → ACK'),(465,'44번 · TCP DNS 질문\n길이 2바이트 + DNS 메시지'),(595,'45번 · TCP DNS 응답\nTraining response over TCP.'),(725,'46번 · TCP 수신 확인\nDNS 본문은 없음')]
    for y,s in items:
        box(p,y,s)
        if y<725:arrow(p,f'200,{y+76} 200,{y+130}')
    text(p,200,850,'아래 방향: 시간 진행 · DNS는 UDP만이 아님','label')
    save(p,'lesson05-tcp.svg')
