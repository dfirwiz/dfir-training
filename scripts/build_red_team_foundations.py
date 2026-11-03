"""Build the independent red-team foundations course.

Standard library only. Existing courses are not regenerated or modified.
"""
from pathlib import Path
from html import escape
import json
import re
from red_team_windows_diagrams import build_windows_diagrams
from red_team_c2_diagrams import build_c2_diagrams

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'content/red-team-foundations'
OUT = ROOT / 'courses/red-team-foundations'
ASSETS = ROOT / 'assets/red-team-foundations'
TITLE = '레드팀 기초: 공격 이해와 보안 검증'
ORIGIN = 'https://dfirwiz.github.io/dfir-training/'


def inline(text):
    pattern = r'(`[^`]+`|\*\*[^*]+\*\*|\[[^\]]+\]\((?:https://[^\s)]+|\.\./\.\./assets/red-team-foundations/[A-Za-z0-9_.-]+)\))'
    parts = []
    for token in re.split(pattern, text):
        if token.startswith('`') and token.endswith('`'):
            parts.append('<code>' + escape(token[1:-1]) + '</code>')
        elif token.startswith('**') and token.endswith('**'):
            parts.append('<strong>' + inline(token[2:-2]) + '</strong>')
        elif re.fullmatch(r'\[[^\]]+\]\((?:https://[^\s)]+|\.\./\.\./assets/red-team-foundations/[A-Za-z0-9_.-]+)\)', token):
            label, url = re.fullmatch(r'\[([^\]]+)\]\(((?:https://[^\s)]+|\.\./\.\./assets/red-team-foundations/[A-Za-z0-9_.-]+))\)', token).groups()
            parts.append(f'<a href="{escape(url, quote=True)}">{inline(label)}</a>')
        else:
            parts.append(escape(token))
    return ''.join(parts)


def diagram(title, width, height, nodes, edges, description):
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
           f'<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>',
           '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8" fill="none" stroke="#78e3c5" stroke-width="1.5"/></marker></defs>',
           '<style>text{font-family:Pretendard,Arial,sans-serif;fill:#deeee9;font-size:18px}.label{font-size:16px;fill:#a8c9d5}</style>',
           f'<rect width="{width}" height="{height}" rx="14" fill="#0e1927"/>']
    for points, labels, x, y in edges:
        out.append(f'<polyline points="{points}" fill="none" stroke="#78e3c5" stroke-width="2.2" marker-end="url(#arrow)"/>')
        if labels:
            label_width = max(len(label) for label in labels) * 16 + 14
            out.append(f'<rect x="{x-label_width/2}" y="{y-17}" width="{label_width}" height="{len(labels)*22+4}" rx="4" fill="#0e1927"/>')
        for i, label in enumerate(labels):
            out.append(f'<text class="label" x="{x}" y="{y + i * 22}" text-anchor="middle">{escape(label)}</text>')
    for x, y, w, h, labels, kind in nodes:
        fill, stroke = ('#193345', '#80a7ff') if kind == 'decision' else ('#152d3a', '#426c7c')
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}"/>')
        top = y + (h - len(labels) * 26) / 2 + 20
        for i, label in enumerate(labels):
            out.append(f'<text x="{x+w/2}" y="{top + i * 26}" text-anchor="middle">{escape(label)}</text>')
    out.append('</svg>')
    return ''.join(out)


def build_diagrams():
    ASSETS.mkdir(parents=True, exist_ok=True)
    items = {
        '01-ttp.svg': diagram('전술·기법·절차의 관계', 560, 460, [
            (70, 25, 420, 80, ['전술', '실행 기회를 유지하려는 목적'], ''),
            (70, 180, 420, 70, ['기법: Windows 예약 작업 이용'], ''),
            (15, 330, 255, 100, ['절차 예시 A', '화면에서', '실습 작업 등록'], ''),
            (290, 330, 255, 100, ['절차 예시 B', '명령줄 도구로', '실습 작업 등록'], ''),
        ], [
            ('280,105 280,180', [], 0, 0),
            ('280,250 280,285 142,285 142,330', [], 0, 0),
            ('280,250 280,285 417,285 417,330', [], 0, 0),
        ], '화살표는 시간 순서가 아니라 설명의 구체화 관계입니다. 전술에서 기법으로 이어지며 화면과 명령줄의 두 절차로 분기합니다.'),
        '02-lifecycle.svg': diagram('내부 탐색과 이동이 반복되는 가상 흐름', 720, 850, [
            (190, 25, 240, 60, ['최초 접근'], ''),
            (190, 155, 240, 70, ['내부 구조와 자원 조사'], ''),
            (190, 305, 240, 60, ['추가 시스템 접근'], ''),
            (190, 455, 240, 60, ['필요한 권한 확보'], ''),
            (190, 605, 240, 60, ['목표 자료 접근'], ''),
            (190, 755, 240, 60, ['목표 달성 여부 검증'], ''),
        ], [
            ('310,85 310,155', [], 0, 0),
            ('310,225 310,305', [], 0, 0),
            ('310,365 310,455', [], 0, 0),
            ('190,485 70,485 70,190 190,190', ['권한 확보 후', '다시 조사'], 92, 340),
            ('430,190 610,190 610,650 430,650', ['현재 권한으로', '접근 가능'], 620, 265),
            ('430,335 510,335 510,620 430,620', ['목표가 있는', '시스템'], 555, 430),
            ('310,665 310,755', [], 0, 0),
        ], '화살표는 가능한 진행 방향입니다. 권한 확보 후 내부 조사로 돌아가는 경로와 기존 권한으로 목표 자료에 접근하는 경로를 모두 보존합니다.'),
        '03-engagement.svg': diagram('실행·중단·재개의 판단 흐름', 700, 880, [
            (35, 25, 280, 65, ['수행할 행동 선택'], ''),
            (35, 165, 280, 100, ['판단 1', '대상과 행동이', '합의 범위 안인가?'], 'decision'),
            (35, 350, 280, 65, ['실행하고 기록'], ''),
            (35, 490, 280, 100, ['판단 2', '예상한 상태와 영향인가?'], 'decision'),
            (35, 760, 280, 80, ['결과 검증과', '변경 사항 정리'], ''),
            (405, 350, 250, 100, ['관련 활동 중단', '상태 기록·연락'], ''),
            (405, 560, 250, 100, ['조율 결과와', '재개 조건 확인'], ''),
        ], [
            ('175,90 175,165', [], 0, 0),
            ('175,265 175,350', ['예'], 200, 311),
            ('315,235 530,235 530,350', ['아니오 또는 불명확'], 505, 285),
            ('175,415 175,490', [], 0, 0),
            ('175,590 175,760', ['예'], 200, 680),
            ('315,540 365,540 365,400 405,400', ['아니오'], 365, 470),
            ('530,450 530,560', [], 0, 0),
            ('655,610 680,610 680,125 345,125 345,190 315,190', ['재개 조건 확인 후', '범위 재검토'], 505, 90),
        ], '화살표는 활동 결정 순서입니다. 범위 또는 영향이 불명확하면 중단·기록·연락하고, 조율 후 다시 범위를 확인합니다.'),
    }
    for name, text in items.items():
        (ASSETS / name).write_text(text, encoding='utf-8')
    build_windows_diagrams(ASSETS, diagram)
    build_c2_diagrams(ASSETS, diagram)


def render(md):
    lines, out, toc, i, opened = md.splitlines(), [], [], 0, False
    counts = dict(sections=0, tables=0, figures=0, code_blocks=0, review_questions=0)
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith('## '):
            if opened:
                out.append('</section>')
            title = line[3:]
            anchor = 'section-' + str(len(toc) + 1)
            toc.append((anchor, title))
            out.append(f'<section id="{anchor}"><h2>{inline(title)}</h2>')
            counts['sections'] += 1
            opened = True
            i += 1
        elif line.startswith('### '):
            heading = line[4:]
            if heading.startswith('복습 '):
                counts['review_questions'] += 1
            out.append('<h3>' + inline(heading) + '</h3>')
            i += 1
        elif line.startswith('```'):
            language, code = line[3:].strip(), []
            assert re.fullmatch(r'[A-Za-z0-9_-]*', language)
            i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                code.append(lines[i])
                i += 1
            assert i < len(lines), 'Unclosed code fence'
            out.append(f'<pre tabindex="0" aria-label="{escape(language)} 예제"><code class="language-{language}">{escape(chr(10).join(code))}</code></pre>')
            counts['code_blocks'] += 1
            i += 1
        elif re.fullmatch(r'!\[[^\]]*\]\([^)]+\)', line):
            alt, src = re.fullmatch(r'!\[([^\]]*)\]\(([^)]+)\)', line).groups()
            assert src.startswith('../../assets/red-team-foundations/')
            asset = (OUT / src).resolve()
            assert asset.is_file()
            dimensions = re.search(r'width="(\d+)" height="(\d+)"', asset.read_text(encoding='utf-8'))
            width, height = dimensions.groups()
            out.append(f'<figure id="figure-{counts['figures']+1}" class="diagram course-diagram"><div class="diagram-scroll" tabindex="0" role="region" aria-label="가로로 스크롤할 수 있는 다이어그램"><img src="{escape(src)}" width="{width}" height="{height}" alt="{escape(alt)}" loading="lazy"></div><figcaption>{escape(alt)} 좁은 화면에서는 그림 안을 가로로 스크롤하세요.</figcaption></figure>')
            counts['figures'] += 1
            i += 1
        elif line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                cells = [cell.strip() for cell in lines[i].strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', cell) for cell in cells):
                    rows.append(cells)
                i += 1
            assert rows and all(len(row) == len(rows[0]) for row in rows)
            out.append('<div class="table-wrap" tabindex="0" role="region" aria-label="가로로 스크롤할 수 있는 비교표"><table><thead><tr>')
            out.extend(f'<th scope="col">{inline(cell)}</th>' for cell in rows[0])
            out.append('</tr></thead><tbody>')
            for row in rows[1:]:
                out.append('<tr>' + ''.join(f'<td>{inline(cell)}</td>' for cell in row) + '</tr>')
            out.append('</tbody></table></div>')
            counts['tables'] += 1
        elif line.startswith('- ') or re.match(r'^\d+\. ', line):
            ordered = bool(re.match(r'^\d+\. ', line))
            tag = 'ol' if ordered else 'ul'
            pattern = r'^\d+\. (.*)' if ordered else r'^- (.*)'
            out.append(f'<{tag}>')
            while i < len(lines) and re.match(pattern, lines[i]):
                out.append('<li>' + inline(re.match(pattern, lines[i]).group(1)) + '</li>')
                i += 1
            out.append(f'</{tag}>')
        elif line.startswith('> '):
            parts = []
            while i < len(lines) and lines[i].startswith('> '):
                parts.append(inline(lines[i][2:]))
                i += 1
            out.append('<blockquote><p>' + '<br>'.join(parts) + '</p></blockquote>')
        elif line == '---':
            out.append('<hr>')
            i += 1
        else:
            paragraph = []
            while i < len(lines) and lines[i].strip() and lines[i] != '---' and not lines[i].startswith(('## ', '### ', '```', '|', '- ', '> ', '![')) and not re.match(r'^\d+\. ', lines[i]):
                paragraph.append(lines[i])
                i += 1
            assert paragraph, f'Unsupported Markdown: {lines[i]}'
            out.append('<p>' + inline(' '.join(paragraph)) + '</p>')
    if opened:
        out.append('</section>')
    return '\n'.join(out), toc, counts


def chapter_groups(course):
    groups = []
    for chapter in course['chapters']:
        lessons = [item for item in course['lessons'] if item['unit'] == chapter['id']]
        assert [item['lesson_number'] for item in lessons] == list(range(1, len(lessons) + 1))
        groups.append(dict(chapter, lessons=lessons))
    assert [item['id'] for group in groups for item in group['lessons']] == [item['id'] for item in course['lessons']]
    return groups


def lesson_label(lesson):
    return f'{lesson["unit"]}장 {lesson["lesson_number"]}강'


def chapter_label(chapter):
    return f'{chapter["id"]}장 · {chapter["title"]}'


def page(course, title, description, body, toc, selected=None):
    groups = chapter_groups(course)
    rows = []
    for chapter in groups:
        current = selected and selected['unit'] == chapter['id']
        opened = ' open' if current or (not selected and chapter['id'] == groups[0]['id']) else ''
        items = []
        for lesson in chapter['lessons']:
            active = ' aria-current="page"' if selected and selected['id'] == lesson['id'] else ''
            items.append(f'<li><a href="{lesson["slug"]}.html"{active}><span class="num">{lesson["lesson_number"]}강</span><span>{escape(lesson["short_title"])}</span></a></li>')
        rows.append(f'<details class="course-day course-chapter"{opened}><summary><span><span class="chapter-number">{chapter["id"]}장</span> <span lang="en">{escape(chapter["title"])}</span></span></summary><ol class="chapter-lessons">' + ''.join(items) + '</ol></details>')
    sidebar = '<aside class="course-sidebar"><details class="course-menu" open><summary>레드팀 기초 · 과정 목차</summary><a class="course-overview" href="index.html">과정 소개와 학습 순서</a><nav class="course-chapters" aria-label="장별 강의 목차">' + ''.join(rows) + '</nav></details></aside>'
    contents = '<nav class="toc" aria-label="이 강의의 목차"><strong>이 강의에서 배우는 내용</strong><ul class="toc-list" role="list">' + ''.join(f'<li><a href="#{a}">{inline(t)}</a></li>' for a, t in toc) + '</ul></nav>' if toc else ''
    pager = '<nav class="pager" aria-label="강의 이동"><a href="index.html">← 과정 전체 목차</a>'
    if selected:
        index = course['lessons'].index(selected)
        if index > 0:
            prev = course['lessons'][index - 1]
            pager += f'<a href="{prev["slug"]}.html">← {lesson_label(prev)} · {escape(prev["short_title"])}</a>'
        if index + 1 < len(course['lessons']):
            nxt = course['lessons'][index + 1]
            pager += f'<a href="{nxt["slug"]}.html">{lesson_label(nxt)} · {escape(nxt["short_title"])} →</a>'
        else:
            pager += '<span class="pending">다음 강의는 게시 후 안내합니다</span>'
    else:
        pager += f'<a href="{course["lessons"][0]["slug"]}.html">1장 1강부터 읽기 →</a>'
    pager += '</nav>'
    filename = selected['slug'] + '.html' if selected else 'index.html'
    label = f'CHAPTER {selected["unit"]:02d} / LESSON {selected["lesson_number"]:02d}' if selected else 'COURSE 03'
    meta = f'{lesson_label(selected)} · {selected["review_questions"]}개의 복습과 해설' if selected else f'{len(groups)}개 장 · 총 {len(course["lessons"])}개 강의 공개 · {sum(item["review_questions"] for item in course["lessons"])}개의 복습과 해설'
    chapter_crumb = ''
    if selected:
        chapter = next(item for item in groups if item['id'] == selected['unit'])
        chapter_crumb = f' / <a href="index.html#chapter-{chapter["id"]}">{escape(chapter_label(chapter))}</a>'
    updated = (selected or course).get('updated', '2026-11-02')
    return f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#090e18"><meta name="description" content="{escape(description)}"><title>{escape(title)} | DFIR Training</title><link rel="canonical" href="{ORIGIN}courses/red-team-foundations/{filename}"><link rel="preconnect" href="https://cdn.jsdelivr.net"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;family=JetBrains+Mono:wght@400;500;600&amp;display=swap" rel="stylesheet"><link rel="stylesheet" href="../../assets/site.css"><link rel="stylesheet" href="../../assets/notes.css?v=20261103-toc-all"><link rel="stylesheet" href="../../assets/red-team-foundations/course.css?v=20261103-chapters"></head>
<body><a class="skip" href="#content">본문으로 건너뛰기</a><header class="shell nav"><a class="brand" href="../../index.html"><span class="mark">D</span>DFIR TRAINING</a><nav class="navlinks" aria-label="주요 메뉴"><a href="../../index.html#courses">교육 과정</a><a href="index.html">이 과정 목차</a></nav><a class="navbtn" href="index.html">과정 안내 ↗</a></header><div class="note-layout">{sidebar}<main class="note" id="content"><p class="breadcrumb"><a href="../../index.html#courses">교육 과정</a> / <a href="index.html">레드팀 기초</a>{chapter_crumb}</p><header class="note-header"><div class="eyebrow">RED TEAM FOUNDATIONS / {label}</div><h1>{escape(title)}</h1><p class="description">{escape(description)}</p><div class="meta"><span>{meta}</span><span>업데이트 {updated}</span></div></header>{contents}{body}{pager}</main></div><footer class="note-footer">© 2026 DFIR Training · 관찰한 사실과 추론을 구분하는 학습</footer></body></html>'''


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    build_diagrams()
    course = json.loads((SOURCE / 'course.json').read_text(encoding='utf-8'))
    audit = []
    for item in course['lessons']:
        md = (SOURCE / f'{item["slug"]}.md').read_text(encoding='utf-8')
        body, toc, counts = render(md)
        assert counts['sections'] == item['sections']
        assert counts['review_questions'] == item['review_questions']
        assert counts['figures'] == item.get('figures', 1)
        assert md.count('**해설:**') == item['review_questions']
        html = page(course, item['title'], item['description'], body, toc, item)
        assert not re.search(r'libfile_|file_000||Getting Started\.html', html, re.I)
        (OUT / f'{item["slug"]}.html').write_text(html, encoding='utf-8')
        audit.append(dict(id=item['id'], source_bytes=len(md.encode()), **counts))
    cards = []
    for chapter in chapter_groups(course):
        lesson_cards = ''.join(f'<a class="note-card live" href="{item["slug"]}.html"><span class="number">{item["lesson_number"]}강 / 공개</span><h4>{escape(item["title"])}</h4><p>{escape(item["description"])}</p><span class="read">{item["review_questions"]}개의 복습과 해설 · {lesson_label(item)} 읽기 ↗</span></a>' for item in chapter['lessons'])
        cards.append(f'<section class="course-unit" id="chapter-{chapter["id"]}"><h3>{escape(chapter_label(chapter))}</h3><p class="chapter-description">{escape(chapter["title_ko"])} · {len(chapter["lessons"])}개 강의</p><div class="course-cards">' + lesson_cards + '</div></section>')
    cards = ''.join(cards)
    intro = '<section id="start"><h2>공격자의 행동을 이해하고 방어를 검증합니다</h2><p>보안 장비가 있다는 사실과 실제 공격을 발견하고 대응할 수 있다는 사실은 다릅니다. 이 과정은 그 차이에서 시작해 공격 행동을 설명하는 언어, 위협 정보와 조사 증거, 활동 계획과 기록을 차근차근 연결합니다.</p><p>소방 훈련·여행 지도·시설 점검의 비유에서 출발해 실제 기술과 판단 기준을 설명합니다. 용어를 처음 사용할 때 뜻을 풀고, 작은 예제에서 조건을 바꾼 사례로 발전시킵니다.</p><div class="callout"><strong>현재 공개: 1~4장 · 총 13개 강의</strong><p>1장·3장·4장은 상세 강의로 제공합니다. 2장은 법과 준수 원칙의 핵심 요약입니다. 각 장의 강의 번호는 1강부터 시작합니다. 3장에서는 PE 파일 구조, 프로세스·메모리·권한, 코드 주입의 증거, C# P/Invoke를 배웁니다. 4장에서는 Cobalt Strike의 구성 요소, HTTP·DNS와 SMB·TCP 경로, 페이로드·로더, 세션과 작업 기록을 배웁니다. 비교표, SVG 다이어그램 21개, 바로 읽는 복습 질문과 해설 93개, 읽기 전용 PE 검사기와 가상 이벤트 실습을 제공합니다.</p></div></section><section id="lessons"><h2>강의 목차</h2>' + cards + '</section><section id="evidence"><h2>예제와 증거를 구분합니다</h2><p>이 과정의 시나리오·주소·시간표는 독립적으로 작성한 가상 예제입니다. 3장 1강의 Python 합성 헤더 읽기와 4장 5강의 가상 이벤트 상태 계산은 실제 실행하여 검증했습니다. Windows API·C#·필터·PowerShell·Cobalt Strike 예제는 실제 대상 환경에서 실행한 결과로 제시하지 않습니다. 별도 패킷 캡처나 온라인 실습 환경은 이 과정에 포함되지 않습니다.</p><p>관측 사실, 그 사실이 지지하는 가설, 추가 증거가 필요한 결론을 구분합니다. 공식 자료는 각 강의에 표시한 확인일을 기준으로 하며 최신 추가 장은 2026년 11월 3일에 대조했습니다. 적용 버전과 관측 한계를 각 강의에서 설명합니다.</p></section>'
    (OUT / 'index.html').write_text(page(course, TITLE, course['description'], intro, []), encoding='utf-8')
    home = ROOT / 'index.html'
    text = home.read_text(encoding='utf-8')
    home_groups = []
    for chapter in chapter_groups(course):
        links = ''.join(f'<a class="lesson" href="courses/red-team-foundations/{item["slug"]}.html"><b>{item["lesson_number"]}강</b><span>{escape(item["short_title"])}</span></a>' for item in chapter['lessons'])
        home_groups.append(f'<div class="home-course-chapter"><h4>{escape(chapter_label(chapter))}</h4>' + links + '</div>')
    card = '<!-- RED-TEAM-FOUNDATIONS:START --><div class="course" style="margin-top:28px"><div><span class="pill">● 세 번째 코스 · 4개 장 · 13개 강의</span><h3>레드팀 기초:<br>공격 이해와 보안 검증</h3><p>레드팀의 목적과 TTP에서 출발해 위협 인텔리전스, 공격 생명주기, ROE·OPSEC과 작업 기록을 배웁니다. 법과 준수 원칙, PE 파일과 Windows 실행 기초를 배우고 Cobalt Strike의 구성 요소·통신 경로·페이로드·세션과 작업 기록까지 연결합니다. 가상 조사 사례, 비교표·다이어그램·복습 해설과 읽기 전용 예제를 연결합니다.</p><div class="tags"><span class="tag">TTP · ATT&amp;CK</span><span class="tag">위협 인텔리전스</span><span class="tag">ROE · OPSEC</span><span class="tag">증거 기반 검증</span></div><div class="actions"><a class="primary" href="courses/red-team-foundations/index.html">과정 살펴보기 ↗</a><a class="secondary" href="courses/red-team-foundations/01-purpose-ttp-evidence.html">1장 1강 읽기</a></div></div><div class="outline chapter-outline">' + ''.join(home_groups) + '</div></div><!-- RED-TEAM-FOUNDATIONS:END -->'
    if '<!-- RED-TEAM-FOUNDATIONS:START -->' in text:
        text = re.sub(r'<!-- RED-TEAM-FOUNDATIONS:START -->.*?<!-- RED-TEAM-FOUNDATIONS:END -->', card, text, flags=re.S)
    else:
        marker = '<!-- NETWORK-SECURITY:END -->'
        assert text.count(marker) == 1
        text = text.replace(marker, marker + card)
    text = text.replace('<strong>02</strong><small>독립적인 학습 과정</small>', '<strong>03</strong><small>독립적인 학습 과정</small>')
    chapter_css = '<link rel="stylesheet" href="assets/red-team-foundations/course.css?v=20261103-chapters">'
    if chapter_css not in text:
        text = text.replace('</head>', chapter_css + '</head>', 1)
    home.write_text(text, encoding='utf-8')
    print(json.dumps(audit, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
