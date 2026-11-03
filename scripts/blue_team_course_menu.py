"""Render the public blue-team course navigation from day metadata."""
from html import escape

def sidebar_menu(course, selected):
    current=next((x for x in course['lessons'] if x['id']==selected),None)
    rows=['<a class="course-overview" href="index.html">과정 소개와 날짜별 학습 순서</a>']
    for day in course['days']:
        opened=' open' if (current and current['day']==day['id']) or (not current and day['id']==1) else ''
        rows.append(f'<details class="course-day"{opened}><summary><span>{escape(day["label"])}<br>{escape(day["title"])}</span></summary><ol>')
        for item in day['lessons']:
            label=f'<span class="num">{item["number"]:02d}</span><span>{escape(item["title"])}'
            if item['status']=='published':
                active=' aria-current="page"' if selected==item['id'] else ''
                rows.append(f'<li><a href="{item["slug"]}.html"{active}>{label}</span></a></li>')
            else:
                rows.append(f'<li><span class="upcoming">{label}<small class="lesson-state">준비 중</small></span></span></li>')
        rows.append('</ol></details>')
    return '<aside class="course-sidebar" aria-label="블루팀 필수 지식 과정 목차"><details class="course-menu" open><summary>블루팀 필수 지식 · 날짜별 목차</summary><div class="course-days">'+''.join(rows)+'</div></details></aside>'

def overview_body(course):
    next_item=next((x for x in course['lessons'] if x['id']==course.get('next_lesson')),None)
    next_day=next((d for d in course['days'] if next_item and d['id']==next_item['day']),None)
    total=sum(x['status']=='published' for x in course['lessons'])
    day_one=sum(x['status']=='published' for x in course['days'][0]['lessons'])
    pieces=['''<section id="start"><h2>블루팀이 갖춰야 할 지식을 처음부터</h2><p>경보가 울렸을 때 무엇부터 확인하고, 어떤 근거로 판단하며, 누구와 협업해야 할까요? 블루팀은 조직의 시스템을 지키는 사람들입니다. 이 과정은 보안 운영의 역할과 흐름부터 네트워크·단말·로그·파일의 원리, 조사와 탐지 개선까지 차근차근 연결합니다.</p><p>처음부터 용어를 알고 있다고 가정하지 않습니다. 구체적인 상황과 필요성에서 출발해 비유, 실제 동작, 작은 예제, 조건을 바꾼 사례, 조사 결과의 해석 순서로 배웁니다. 관측한 사실과 가설, 추가 증거가 필요한 결론을 구분합니다.</p><div class="callout"><strong>다음 업데이트: 첫째 날 1강부터</strong><p>과정을 날짜별로 다시 정리했습니다. 앞으로 첫째 날부터 순서대로 분량을 나눠 업데이트합니다. 기존 공개 강의 6편은 둘째 날 아래에서 계속 읽을 수 있으며, 첫째 날 강의는 준비 중입니다.</p></div><p>각 ‘날’은 학습 주제를 묶는 단위입니다. 하루에 전부 읽어야 하는 분량을 뜻하지 않습니다. 강의마다 필요한 배경·예제·예외·복습 해설을 충분히 담고, 내용이 길면 회차를 더 나눕니다.</p></section><nav class="day-jump" aria-label="날짜별 목차 바로가기">''']
    announcement=f'<div class="callout"><strong>현재 공개: {total}개 강의 · 첫째 날 {day_one}개</strong><p>첫째 날부터 날짜별로 순서대로 상세 강의를 업데이트합니다. 각 날짜 아래에서 공개된 강의를 읽을 수 있습니다.'
    if next_item:announcement+=f' 다음 업데이트는 {escape(next_day["label"])} {next_item["number"]}강, ‘{escape(next_item["title"])}’부터입니다.'
    announcement+='</p></div>'
    import re
    pieces[0]=re.sub(r'<div class="callout">.*?</div>',announcement,pieces[0])
    pieces.extend(f'<a href="#day-{d["id"]}">{escape(d["label"])}</a>' for d in course['days'])
    pieces.append('</nav>')
    for day in course['days']:
        published=sum(x['status']=='published' for x in day['lessons'])
        status=f'{published}개 강의 공개' if published else '준비 중'
        pieces.append(f'<section class="day-section" id="day-{day["id"]}"><div class="day-heading"><span class="day-kicker">DAY {day["id"]:02d} · {status}</span><h2>{escape(day["label"])} · {escape(day["title"])}</h2><p>{escape(day["description"])}</p></div><ol class="day-lessons">')
        for item in day['lessons']:
            label=f'<span class="day-lesson-number">{item["number"]:02d}</span>'
            state='공개 · 읽기 ↗' if item['status']=='published' else '준비 중'
            content=label+f'<span class="day-lesson-title">{escape(item["title"])}</span><span class="day-lesson-state">{state}</span>'
            if item['status']=='published':
                pieces.append(f'<li><a class="day-lesson live" href="{item["slug"]}.html">{content}</a></li>')
            else:
                pieces.append(f'<li><div class="day-lesson planned">{content}</div></li>')
        pieces.append('</ol></section>')
    pieces.append(f'<section id="learning"><h2>학습 자료와 업데이트 안내</h2><p>{escape(course["planning_note"])}</p><p>강의는 독립적인 설명·예제·도식으로 작성합니다. 본문에서 가상 사례, 자체 실습 자료, 실제로 확인한 결과와 실행하지 않은 절차를 구분합니다. 기존 둘째 날 1~4강의 사례는 문서용 자체 예제입니다. 5강은 자체 합성 PCAP과 가상 보조 기록을 제공하며, 6강의 HTTP 메시지는 자체 가상 예제입니다.</p><p>각 회차에는 복습 질문과 바로 읽을 수 있는 해설을 포함합니다. 최신 기술 보충에는 적용 조건·확인 날짜·근거 링크를 붙입니다.</p></section>')
    return ''.join(pieces)

def home_card(course):
    def state(day):
        count=sum(x['status']=='published' for x in day['lessons'])
        return f' · {count}강 공개' if count else ' · 준비 중'
    rows=''.join(f'<a class="lesson" href="courses/network-security/index.html#day-{d["id"]}"><b>{d["id"]:02d}</b><span>{escape(d["label"])} · {escape(d["title"])}'+state(d)+'</span></a>' for d in course['days'])
    return '''<!-- NETWORK-SECURITY:START --><div class="course" style="margin-top:28px"><div><span class="pill">● 블루팀 기초 과정 · 날짜별 학습</span><h3>블루팀 필수 지식:<br>보안 운영과 분석</h3><p>보안 운영의 역할과 흐름에서 시작해 네트워크, 단말·로그·파일, 경보 조사, 탐지 개선과 자동화까지 배웁니다. 첫째 날부터 순서대로 강의를 업데이트합니다. 기존 네트워크 강의 6편은 둘째 날에서 읽을 수 있습니다.</p><div class="tags"><span class="tag">보안 운영</span><span class="tag">네트워크 · 단말</span><span class="tag">로그 · 조사</span><span class="tag">탐지 개선 · 자동화</span></div><div class="actions"><a class="primary" href="courses/network-security/index.html">날짜별 과정 살펴보기 ↗</a><a class="secondary" href="courses/network-security/index.html#day-1">첫째 날 강의 보기</a></div></div><div class="outline">'''+rows+'</div></div><!-- NETWORK-SECURITY:END -->'

MENU_CSS='''
/* Blue-team course menu: scoped to its own stylesheet. */
.course-sidebar .course-overview{margin-bottom:12px}
.course-sidebar .lesson-state{display:block;font-size:11px;color:#9baec5;margin-top:3px}
.course-sidebar .course-days{overflow-wrap:anywhere}
.course-sidebar .course-day .num{min-width:1.5em}
.day-jump{display:flex;flex-wrap:wrap;gap:10px;margin:28px 0}
.day-jump a{border:1px solid #426c7c;border-radius:8px;padding:10px 15px;color:#9cf0d9}
.day-jump a:hover{background:#153a36}
.day-kicker{font:500 12px Inter,sans-serif;color:#9cf0d9}
.note .day-heading h2{margin-top:12px;margin-bottom:12px}
.note .day-lessons{list-style:none;padding:0;display:grid;gap:10px}
.note .day-lessons li{margin:0}
.note .day-lesson{display:grid;grid-template-columns:28px minmax(0,1fr) auto;gap:12px;align-items:start;padding:17px 18px;border:1px solid #32445b;border-radius:10px;background:#101d2c;text-decoration:none!important}
.note .day-lesson-number{font:500 13px/1.9 'JetBrains Mono',monospace;color:#9cf0d9}
.note .day-lesson-title{font-size:15px;color:#dbe7f6;line-height:1.8;overflow-wrap:anywhere}
.note .day-lesson-state{font-size:12px;line-height:2.2;white-space:nowrap;color:#9cf0d9}
.note .day-lesson.live:hover{border-color:#78e3c5;background:#15302e}
.note .day-lesson.planned .day-lesson-state{color:#9baec5}
@media(max-width:600px){.note .day-lesson{grid-template-columns:25px minmax(0,1fr);gap:5px 10px;padding:14px}.note .day-lesson-state{grid-column:2;white-space:normal}.day-jump a{padding:9px 12px}.course-sidebar .course-days{max-height:360px;overflow-y:auto}}
'''
