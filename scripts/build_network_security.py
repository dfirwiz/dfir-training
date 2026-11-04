"""Build the day-based blue-team course; preserve published lecture prose."""
from pathlib import Path
from html import escape
import re, json
from network_security_diagrams import build_lesson02
from network_security_dns_diagrams import build_lesson03
from network_security_dns_analysis_diagrams import build_lesson04
from network_security_dns_lab_diagrams import build_lesson05
from network_security_http_diagrams import build_lesson06

ROOT = Path(__file__).resolve().parents[1]
from blue_team_day01_diagrams import build_day01
from blue_team_soc_diagrams import build_soc
from blue_team_visibility_diagrams import build_visibility
from blue_team_alert_diagrams import build_alerts
from blue_team_course_menu import sidebar_menu, overview_body, home_card, MENU_CSS
TITLE = '블루팀 필수 지식: 보안 운영과 분석'
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
build_lesson06(ASSETS)
build_day01(ASSETS)
build_soc(ASSETS)
build_visibility(ASSETS)
build_alerts(ASSETS)

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
lessons_by_id={item['id']:item for item in course['lessons']}
for day in course['days']:
    day['lessons']=[lessons_by_id[key] for key in day['lesson_ids']]

def page(title,description,body,lesson=False):
    links=''.join(f'<li><a href="#{a}">{inline(t)}</a></li>' for a,t in toc) if lesson else ''
    sidebar=sidebar_menu(course,lesson)
    selected=next((item for item in course['lessons'] if item['id']==lesson),None)
    pager='<nav class="pager" aria-label="강의 이동"><a href="index.html">← 날짜별 전체 목차</a>'
    if selected:
        day=next(d for d in course['days'] if d['id']==selected['day'])
        items=day['lessons']; index=items.index(selected)
        if index and items[index-1]['status']=='published':
            previous=items[index-1]
            pager+=f'<a href="{previous["slug"]}.html">← {day["label"]} {previous["number"]}강 · {escape(previous.get("short_title",previous["title"]))}</a>'
        if index+1<len(items):
            following=items[index+1]
            if following['status']=='published':
                pager+=f'<a href="{following["slug"]}.html">{day["label"]} {following["number"]}강 · {escape(following.get("short_title",following["title"]))} →</a>'
            else:
                pager+=f'<span class="pending">다음 강의 · {escape(following['title'])} · 준비 중</span>'
    else:
        pager+='<a href="#day-1">첫째 날 학습 계획 보기 →</a>'
    pager+='</nav>'
    contents='<nav class="toc" aria-label="이 강의의 목차"><strong>이 강의에서 배우는 내용</strong><ul class="toc-list" role="list">'+links+'</ul></nav>' if lesson else ''
    filename=selected['slug']+'.html' if selected else 'index.html'
    return f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#090e18"><meta name="description" content="{escape(description)}"><title>{escape(title)} | DFIR Training</title><link rel="canonical" href="https://dfirwiz.github.io/dfir-training/courses/network-security/{filename}"><link rel="preconnect" href="https://cdn.jsdelivr.net"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;family=JetBrains+Mono:wght@400;500;600&amp;display=swap" rel="stylesheet"><link rel="stylesheet" href="../../assets/site.css"><link rel="stylesheet" href="../../assets/notes.css?v=20261103-toc-all"><link rel="stylesheet" href="../../assets/network-security/course.css?v=20261104-day01-batch04"></head><body><a class="skip" href="#content">본문으로 건너뛰기</a><header class="shell nav"><a class="brand" href="../../index.html"><span class="mark">D</span>DFIR TRAINING</a><nav class="navlinks" aria-label="주요 메뉴"><a href="../../index.html#courses">교육 과정</a><a href="index.html">이 과정 목차</a></nav><a class="navbtn" href="index.html">과정 안내 ↗</a></header><div class="note-layout">{sidebar}<main class="note" id="content"><p class="breadcrumb"><a href="../../index.html#courses">교육 과정</a> / <a href="index.html">블루팀 필수 지식</a></p><header class="note-header"><div class="eyebrow">BLUE TEAM / {f'DAY {selected["day"]:02d} · LESSON {selected["number"]:02d}' if selected else 'COURSE 02'}</div><h1>{escape(title)}</h1><p class="description">{escape(description)}</p><div class="meta"><span>{escape(day['label'])+' '+str(selected['number'])+'강 · '+escape(selected.get('short_title',selected['title'])) if selected else '보안 운영·분석을 시작하는 독자를 위한 과정'}</span><span>업데이트 {course["updated"]}</span></div></header>{contents}{body}{pager}</main></div><footer class="note-footer">© 2026 DFIR Training · 관찰한 사실과 추론을 구분하는 학습</footer></body></html>'''

for item in course['lessons']:
    if item['status']!='published':continue
    md=(ROOT/f'content/network-security/{item["slug"]}.md').read_text(encoding='utf-8')
    body,toc=render(md,4 if item['id']==1 else 0)
    (OUT/f'{item["slug"]}.html').write_text(page(item['title'],item['description'],body,item['id']),encoding='utf-8')

overview=overview_body(course)
(OUT/'index.html').write_text(page(TITLE,'블루팀이 갖춰야 할 보안 운영과 분석의 필수 지식. 첫째 날부터 네트워크, 단말·로그·파일, 조사, 탐지 개선과 자동화까지 날짜별로 배웁니다.',overview),encoding='utf-8')
(ASSETS/'course.css').write_text('.toc ol,.toc ul{list-style:none;padding-left:0}.course-diagram{max-width:440px;margin:30px auto;padding:12px}.course-diagram img{display:block;width:100%;height:auto;min-width:0}.calculation{font-family:Inter,sans-serif;padding:20px;border:1px solid #426c7c;border-radius:10px}.note .table-wrap{max-width:100%}.note .course-diagram figcaption{font-size:13px}.note hr{border:0;border-top:1px solid #32445b;margin:35px 0}@media(max-width:460px){.course-diagram{padding:4px}.note-layout{padding-left:15px;padding-right:15px}}'+MENU_CSS,encoding='utf-8')

card=home_card(course)
home=ROOT/'index.html';text=home.read_text(encoding='utf-8')
if '<!-- NETWORK-SECURITY:START -->' in text:text=re.sub(r'<!-- NETWORK-SECURITY:START -->.*?<!-- NETWORK-SECURITY:END -->',card,text,flags=re.S)
else:
    m=re.search(r'<section class="section" id="courses">.*?</section>',text,re.S);assert m
    old=m.group();new=old[:-len('</div></section>')]+card+'</div></section>';assert old.endswith('</div></section>');text=text[:m.start()]+new+text[m.end():]
text=text.replace('<strong>01</strong><small>첫 번째 학습 트랙</small>','<strong>02</strong><small>독립적인 학습 과정</small>')
home.write_text(text,encoding='utf-8')
print('Built blue team catalog and',sum(item['status']=='published' for item in course['lessons']),'published lessons.')
