"""Build the independent network security course; preserve reviewed prose."""
from pathlib import Path
from html import escape
import re, json
from network_security_diagrams import build_lesson02
from network_security_dns_diagrams import build_lesson03
from network_security_dns_analysis_diagrams import build_lesson04
from network_security_dns_lab_diagrams import build_lesson05

ROOT = Path(__file__).resolve().parents[1]
TITLE = '네트워크 보안 분석: 통신 원리부터 침해 조사까지'
OUT = ROOT/'courses/network-security'
ASSETS = ROOT/'assets/network-security'
OUT.mkdir(parents=True, exist_ok=True)
ASSETS.mkdir(parents=True, exist_ok=True)

def svg(title, height, nodes, edges, legend):
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="{height}" viewBox="0 0 400 {height}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(legend)}</desc>', '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto-start-reverse"><path d="M0 0L8 4L0 8" fill="none" stroke="#78e3c5"/></marker></defs><rect width="400" height="100%" rx="14" fill="#0e1927"/>', '<style>text{font-family:Pretendard,Arial,sans-serif;fill:#deeee9;font-size:17px} .label{font-size:14px;fill:#a8c9d5}</style>']
    for points, label, x, y, kind in edges:
        dash=' stroke-dasharray="6 5"' if kind=='copy' else ''
        start=' marker-start="url(#arrow)"' if kind=='both' else ''
        parts.append(f'<polyline points="{points}" fill="none" stroke="#78e3c5" stroke-width="2" marker-end="url(#arrow)"{dash}{start}/><text class="label" x="{x}" y="{y}" text-anchor="middle">{escape(label)}</text>')
    for x,y,w,h,lines in nodes:
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#152d3a" stroke="#426c7c"/>')
        for i,line in enumerate(lines):
            parts.append(f'<text x="{x+w/2}" y="{y+(h-len(lines)*23)/2+17+i*23}" text-anchor="middle">{escape(line)}</text>')
    parts.append(f'<text class="label" x="200" y="{height-18}" text-anchor="middle">{escape(legend)}</text></svg>')
    return ''.join(parts)

diagrams = [
svg('서로 다른 서브넷 사이의 통신',430,
[(85,20,230,65,['직원 컴퓨터','192.0.2.10']),(85,165,230,65,['라우터','목적지에 맞는 경로 선택']),(85,310,230,65,['서버','198.51.100.20'])],
[('170,85 170,165','요청 ↓',117,130,'one'),('230,165 230,85','응답 ↑',278,130,'one'),('170,230 170,310','요청 ↓',117,276,'one'),('230,310 230,230','응답 ↑',278,276,'one')],'화살표: 패킷 방향 · 주소: 문서용 예제'),
svg('보안 구역과 정책 적용 지점',670,
[(85,20,230,60,['라우터·방화벽 등','구역 사이 경로와 정책'])]+[(85,125+i*72,230,48,[s]) for i,s in enumerate(['직원 컴퓨터 구역','내부 서버 구역','공개 서비스 구역','IoT 구역','방문객 구역','클라우드 구역','제한 서버 구역'])],
[(f'85,50 45,50 45,{149+i*72} 85,{149+i*72}','',0,0,'both') for i in range(7)],'양방향 연결: 정책이 허용한 통신만 가능'),
svg('스위치 내부 통신과 복사 위치',610,
[(20,20,150,55,['직원 A']),(230,20,150,55,['직원 B']),(110,140,180,55,['같은 스위치']),(20,270,170,55,['상위 연결 TAP']),(20,415,170,55,['라우터']),(220,270,160,55,['미러링 센서']),(220,415,160,55,['TAP 센서'])],
[('95,75 95,115 160,115 160,140','',0,0,'both'),('305,75 305,115 240,115 240,140','',0,0,'both'),('150,195 105,270','원래 경로',80,235,'both'),('105,325 105,415','원래 경로',57,375,'both'),('290,168 330,168 330,270','포트·VLAN 복사',310,225,'copy'),('190,298 205,298 205,443 220,443','링크 복사',290,380,'copy')],'실선: 원래 통신 · 점선: 분석용 복사'),
svg('침해된 컴퓨터의 접근 시도와 정책',650,
[(75,20,250,55,['침해된 직원 컴퓨터']),(90,140,220,55,['다른 직원 컴퓨터']),(90,280,220,55,['구역 사이 접근 정책']),(90,420,220,55,['업무 서버']),(75,555,250,55,['중요 자료·백업 서버'])],
[('200,75 200,140','접근 시도',255,115,'one'),('75,48 35,48 35,307 90,307','접근 시도',70,245,'one'),('200,335 200,420','허용 조건 충족 시',280,382,'one'),('200,475 200,555','별도 접근 정책 필요',285,519,'one')],'화살표: 접근 시도 · 성공을 뜻하지 않음')]
for i,d in enumerate(diagrams,1): (ASSETS/f'figure-{i}.svg').write_text(d,encoding='utf-8')
build_lesson02(ASSETS)
build_lesson03(ASSETS)
build_lesson04(ASSETS)
build_lesson05(ASSETS)

def inline(s):
    s=escape(s)
    s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
    s=re.sub(r'\[([^\]]+)\]\((https://[^\s)]+|\.\./\.\./assets/network-security/lab05/[A-Za-z0-9_.-]+)\)',r'<a href="\2">\1</a>',s)
    return s

def render(md, expected_mermaid=0):
    lines=md.splitlines(); out=[]; toc=[]; i=0; fig=0; section=False
    while i<len(lines):
        line=lines[i]
        if not line.strip(): i+=1; continue
        if line.startswith('```mermaid'):
            i+=1
            while i<len(lines) and not lines[i].startswith('```'): i+=1
            fig+=1
            out.append(f'<figure class="diagram course-diagram"><img src="../../assets/network-security/figure-{fig}.svg" width="400" height="{[430,670,610,650][fig-1]}" alt="그림 {fig}: {["서로 다른 서브넷 사이의 통신 경로","보안 구역과 정책 적용 관계","스위치·TAP·미러링의 관측 위치","측면 이동 시도와 접근 정책"][fig-1]}" loading="lazy"><figcaption>그림 {fig} · 위 본문에 설명한 방향과 범례를 함께 읽어주세요.</figcaption></figure>'); i+=1;continue
        image_match=re.fullmatch(r'!\[([^\]]*)\]\(([^)]+)\)',line)
        if image_match:
            alt,src=image_match.groups()
            assert src.startswith('../../assets/network-security/')
            asset=OUT/src
            dimensions=re.search(r'width="(\d+)" height="(\d+)"',asset.read_text(encoding='utf-8'))
            assert dimensions,src
            width,height=dimensions.groups()
            out.append(f'<figure class="diagram course-diagram"><img src="{escape(src)}" width="{width}" height="{height}" alt="{escape(alt)}" loading="lazy"><figcaption>{escape(alt)}</figcaption></figure>')
            i+=1;continue
        if line.startswith('```'):
            language=line[3:].strip();code=[];i+=1
            assert re.fullmatch(r'[A-Za-z0-9_-]*',language)
            while i<len(lines) and not lines[i].startswith('```'):
                code.append(lines[i]);i+=1
            assert i<len(lines),'Unclosed code fence'
            out.append(f'<pre tabindex="0"><code class="language-{language}">'+escape('\n'.join(code))+'</code></pre>')
            i+=1;continue
        if line=='\\[':
            i+=1
            while i<len(lines) and lines[i]!='\\]': i+=1
            out.append('<p class="calculation" aria-label="초당 1기가비트 더하기 초당 1기가비트는 초당 2기가비트">1 Gbps + 1 Gbps = 2 Gbps</p>');i+=1;continue
        if line.startswith('## '):
            if section: out.append('</section>')
            heading=line[3:]; anchor='section-'+str(len(toc)+1); toc.append((anchor,heading));out.append(f'<section id="{anchor}"><h2>{inline(heading)}</h2>');section=True;i+=1;continue
        if line.startswith('### '): out.append('<h3>'+inline(line[4:])+'</h3>');i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                cells=[x.strip() for x in lines[i].strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?',x) for x in cells): rows.append(cells)
                i+=1
            out.append('<div class="table-wrap" tabindex="0" role="region" aria-label="가로로 스크롤할 수 있는 비교표"><table>')
            for n,row in enumerate(rows):
                tag='th' if n==0 else 'td';out.append('<tr>'+''.join(f'<{tag}'+(' scope="col"' if n==0 else '')+'>'+inline(c)+f'</{tag}>' for c in row)+'</tr>')
            out.append('</table></div>');continue
        if line.startswith('- '):
            out.append('<ul>')
            while i<len(lines) and lines[i].startswith('- '):out.append('<li>'+inline(lines[i][2:])+'</li>');i+=1
            out.append('</ul>');continue
        if line.startswith('> '):out.append('<blockquote>'+inline(line[2:])+'</blockquote>');i+=1;continue
        if line=='---':out.append('<hr>');i+=1;continue
        p=[]
        while i<len(lines) and lines[i].strip() and not lines[i].startswith(('## ','### ','|','- ','```','\\[','> ','![')) and lines[i]!='---':p.append(lines[i]);i+=1
        out.append('<p>'+inline(' '.join(p))+'</p>')
    if section:out.append('</section>')
    assert fig==expected_mermaid
    return '\n'.join(out),toc

course=json.loads((ROOT/'content/network-security/course.json').read_text(encoding='utf-8'))

def page(title,description,body,lesson=False):
    links=''.join(f'<li><a href="#{a}">{inline(t)}</a></li>' for a,t in toc) if lesson else ''
    rows=['<li><a href="index.html">과정 소개와 학습 순서</a></li>']
    for item in course['lessons']:
        label=f'<span class="num">{item["id"]:02d}</span>{escape(item["title"])}'
        if item['status']=='published':
            current=' aria-current="page"' if item['id']==lesson else ''
            rows.append(f'<li><a href="{item["slug"]}.html"{current}>{label}</a></li>')
        else:rows.append(f'<li><span class="upcoming">{label} · 준비 중</span></li>')
    sidebar='<aside class="course-sidebar"><details open><summary>네트워크 보안 분석 · 과정 목차</summary><ol>'+''.join(rows)+'</ol></details></aside>'
    pager='<nav class="pager"><a href="index.html">← 과정 전체 목차</a>'
    selected=next((item for item in course['lessons'] if item['id']==lesson),None)
    if selected:
        index=course['lessons'].index(selected)
        if index:
            previous=course['lessons'][index-1]
            pager+=f'<a href="{previous["slug"]}.html">← {previous["id"]}강 · {escape(previous.get("short_title",previous["title"]))}</a>'
        if index+1<len(course['lessons']):
            following=course['lessons'][index+1]
            if following['status']=='published':pager+=f'<a href="{following["slug"]}.html">{following["id"]}강 · {escape(following.get("short_title",following["title"]))} →</a>'
            else:pager+=f'<span class="pending">다음 강의 · {escape(following["title"])} · 준비 중</span>'
    else:pager+='<a href="01-network-architecture.html">1강부터 읽기 →</a>'
    pager+='</nav>'
    contents='<nav class="toc" aria-label="이 강의의 목차"><strong>이 강의에서 배우는 내용</strong><ol>'+links+'</ol></nav>' if lesson else ''
    filename=selected['slug']+'.html' if selected else 'index.html'
    return f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#090e18"><meta name="description" content="{escape(description)}"><title>{escape(title)} | DFIR Training</title><link rel="canonical" href="https://dfirwiz.github.io/dfir-training/courses/network-security/{filename}"><link rel="preconnect" href="https://cdn.jsdelivr.net"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;family=JetBrains+Mono:wght@400;500;600&amp;display=swap" rel="stylesheet"><link rel="stylesheet" href="../../assets/site.css"><link rel="stylesheet" href="../../assets/notes.css"><link rel="stylesheet" href="../../assets/network-security/course.css"></head><body><a class="skip" href="#content">본문으로 건너뛰기</a><header class="shell nav"><a class="brand" href="../../index.html"><span class="mark">D</span>DFIR TRAINING</a><nav class="navlinks" aria-label="주요 메뉴"><a href="../../index.html#courses">교육 과정</a><a href="index.html">이 과정 목차</a></nav><a class="navbtn" href="index.html">과정 안내 ↗</a></header><div class="note-layout">{sidebar}<main class="note" id="content"><p class="breadcrumb"><a href="../../index.html#courses">교육 과정</a> / <a href="index.html">네트워크 보안 분석</a></p><header class="note-header"><div class="eyebrow">NETWORK SECURITY / {f'LESSON {int(lesson):02d}' if lesson else 'COURSE 02'}</div><h1>{escape(title)}</h1><p class="description">{escape(description)}</p><div class="meta"><span>{str(int(lesson))+'강 · '+escape(selected.get('short_title',selected['title'])) if selected else '초보자를 위한 독립 과정'}</span><span>업데이트 2026-11-02</span></div></header>{contents}{body}{pager}</main></div><footer class="note-footer">© 2026 DFIR Training · 관찰한 사실과 추론을 구분하는 학습</footer></body></html>'''

for item in course['lessons']:
    if item['status']!='published':continue
    md=(ROOT/f'content/network-security/{item["slug"]}.md').read_text(encoding='utf-8')
    body,toc=render(md,4 if item['id']==1 else 0)
    (OUT/f'{item["slug"]}.html').write_text(page(item['title'],item['description'],body,item['id']),encoding='utf-8')

overview='''<section id="start"><h2>통신의 원리에서 조사 판단까지</h2><p>의심스러운 통신을 발견했을 때, 어느 기록을 확인하고 어디까지 결론을 내릴 수 있을까요? 이 과정에서는 상황과 문제에서 출발해 생활 속 비유, 실제 기술의 동작, 작은 예제, 조건을 바꾼 사례, 조사에서의 해석 순서로 배웁니다.</p><p>이전에 네트워크를 배웠다고 가정하지 않습니다. 용어를 처음 사용할 때 의미를 설명하고, 패킷에서 관측한 사실과 그 사실이 지지하는 가설, 추가 증거가 필요한 결론을 구분합니다.</p><div class="callout"><strong>현재 공개된 강의: 1~5강</strong><p>네트워크 구조부터 순서대로 연재합니다. 각 강의에는 본문 설명, 필요한 표와 그림, 최신 보충의 근거, 바로 읽을 수 있는 복습 해설을 포함합니다.</p></div></section><section id="lessons"><h2>강의 목차</h2><a class="note-card live" style="display:block" href="01-network-architecture.html"><span class="number">LESSON 01 / 공개</span><h3>네트워크 구조: 통신이 지나가는 길과 증거가 남는 위치</h3><p>라우터·보안 구역·스위치·TAP과 미러링·방화벽·제로 트러스트를 조사에 연결합니다. 그림 4개와 복습 질문·해설 10개를 함께 읽습니다.</p><span class="read">1강 읽기 ↗</span></a><a class="note-card live" style="display:block;margin-top:20px" href="02-traffic-capture-analysis.html"><span class="number">LESSON 02 / 공개</span><h3>트래픽 수집과 분석 — 요약 기록에서 패킷 증거까지</h3><p>세 종류의 수집 자료, 플로와 샘플링, 메타데이터, 저장 용량, 표시 필터와 요청·응답을 연결합니다. 그림 3개, 명령·필터 예제, 복습 12문항과 해설을 함께 읽습니다.</p><span class="read">2강 읽기 ↗</span></a><a class="note-card live" style="display:block;margin-top:20px" href="03-understanding-dns.html"><span class="number">LESSON 03 / 공개</span><h3>DNS의 동작 원리 — 이름에서 주소로, 응답에서 증거로</h3><p>조회 경로와 캐시, 주소·별칭·메일·서비스 레코드, 질문·응답 짝짓기와 관측 한계를 배웁니다. 그림 4개, 자체 패킷 연습, 복습 14문항과 해설을 포함합니다.</p><span class="read">3강 읽기 ↗</span></a><a class="note-card live" style="display:block;margin-top:20px" href="04-dns-analysis-attacks.html"><span class="number">LESSON 04 / 공개</span><h3>DNS 분석과 공격 징후 — 조회 기록에서 조사 판단까지</h3><p>로그 수집 위치, 도메인 보강, 비인가 DNS, 터널링, 유사 문자와 암호화 DNS를 조사 판단에 연결합니다. 그림 5개, 종합 가상 사례, 복습 18문항과 해설을 포함합니다.</p><span class="read">4강 읽기 ↗</span></a><a class="note-card live" style="display:block;margin-top:20px" href="05-dns-investigation-practice.html"><span class="number">LESSON 05 / 공개</span><h3>DNS 분석 실습 — 질문·응답에서 조사 기록까지</h3><p>자체 PCAP과 보조 로그를 내려받아 질문·응답, 재시도, 빈 답, 비인가 경로와 TCP 전환을 분석합니다. 그림 4개, 실습 해설, 복습 16문항을 포함합니다.</p><span class="read">5강 읽기 ↗</span></a><h3>이어서 배울 범위</h3><ol><li>HTTP의 동작 원리</li><li>HTTP·HTTPS 분석과 공격 징후</li><li>웹 통신 실습 연결</li><li>SMTP와 이메일 통신</li><li>추가 네트워크 프로토콜</li><li>이메일 실습과 종합 복습</li></ol><p>뒤의 범위는 준비 중입니다. 필요한 배경과 예외를 생략하지 않도록 학습 범위에 따라 회차를 더 나눌 수 있습니다.</p></section><section id="evidence"><h2>예제와 분석 결과의 구분</h2><p>1~4강의 주소·구성·조사 사례는 설명을 위해 만든 문서용 자체 예제입니다. 실제 네트워크 수집본의 분석 결과가 아닙니다. 5강은 자체 합성 PCAP과 가상 보조 기록을 제공하며, 파일 해석에서 확인한 결과와 가상 맥락·실행하지 않은 절차를 구분합니다.</p></section>'''
(OUT/'index.html').write_text(page(TITLE,'네트워크를 처음 배우는 독자를 위한 한국어 강의. 통신 구조와 프로토콜의 원리를 패킷 분석과 보안 조사에 연결합니다.',overview),encoding='utf-8')
(ASSETS/'course.css').write_text('.toc ol{list-style:none;padding-left:0}.course-diagram{max-width:440px;margin:30px auto;padding:12px}.course-diagram img{display:block;width:100%;height:auto;min-width:0}.calculation{font-family:Inter,sans-serif;padding:20px;border:1px solid #426c7c;border-radius:10px}.note .table-wrap{max-width:100%}.note .course-diagram figcaption{font-size:13px}.note hr{border:0;border-top:1px solid #32445b;margin:35px 0}@media(max-width:460px){.course-diagram{padding:4px}.note-layout{padding-left:15px;padding-right:15px}}',encoding='utf-8')

card='''<!-- NETWORK-SECURITY:START --><div class="course" style="margin-top:28px"><div><span class="pill">● 두 번째 코스 · 5강까지 공개</span><h3>네트워크 보안 분석:<br>통신 원리부터 침해 조사까지</h3><p>네트워크 구조와 관측 위치에서 시작해 DNS·웹·이메일의 동작을 이해하고, 패킷과 로그를 근거로 조사하는 방법을 배웁니다. 친근한 해설, 실제로 보이는 도식, 조건을 바꾼 사례와 복습 해설을 함께 제공합니다.</p><div class="tags"><span class="tag">네트워크 구조</span><span class="tag">패킷 분석</span><span class="tag">보안 조사</span><span class="tag">DNS · HTTP · SMTP</span></div><div class="actions"><a class="primary" href="courses/network-security/index.html">과정 살펴보기 ↗</a><a class="secondary" href="courses/network-security/01-network-architecture.html">1강 읽기</a></div></div><div class="outline"><div class="lesson"><b>01</b> 네트워크 구조와 증거의 위치 · 공개</div><a class="lesson" href="courses/network-security/02-traffic-capture-analysis.html"><b>02</b> 트래픽 수집과 분석 · 공개 ↗</a><a class="lesson" href="courses/network-security/03-understanding-dns.html"><b>03</b> DNS의 동작 원리 · 공개 ↗</a><a class="lesson" href="courses/network-security/04-dns-analysis-attacks.html"><b>04</b> DNS 분석과 공격 징후 · 공개 ↗</a><a class="lesson" href="courses/network-security/05-dns-investigation-practice.html"><b>05</b> DNS 분석 실습 · 자료 내려받기 ↗</a><div class="lesson"><b>→</b> 웹 통신 · 이메일</div></div></div><!-- NETWORK-SECURITY:END -->'''
home=ROOT/'index.html';text=home.read_text(encoding='utf-8')
if '<!-- NETWORK-SECURITY:START -->' in text:text=re.sub(r'<!-- NETWORK-SECURITY:START -->.*?<!-- NETWORK-SECURITY:END -->',card,text,flags=re.S)
else:
    m=re.search(r'<section class="section" id="courses">.*?</section>',text,re.S);assert m
    old=m.group();new=old[:-len('</div></section>')]+card+'</div></section>';assert old.endswith('</div></section>');text=text[:m.start()]+new+text[m.end():]
text=text.replace('<strong>01</strong><small>첫 번째 학습 트랙</small>','<strong>02</strong><small>독립적인 학습 과정</small>')
home.write_text(text,encoding='utf-8')
print('Built course catalog, five complete lessons, twenty SVG diagrams and home course card.')
