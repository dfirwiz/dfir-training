#!/usr/bin/env python3
"""Render the static learning catalog and notes using only Python's standard library."""
from pathlib import Path
import json, re
from html import escape

ROOT = Path(__file__).resolve().parents[1]
course = json.loads((ROOT / 'content/course.json').read_text(encoding='utf-8'))
lessons = course['lessons']
published = [item for item in lessons if item['status'] == 'published']

def day_title(day):
    return {1: '첫째 날 · 기초 네트워크 분석', 2: '둘째 날 · 필터와 전송 프로토콜'}.get(day, f'{day}일차')

def lesson_label(item):
    if 'day_lesson' in item:
        return f'{day_title(item["day"]).split(" · ")[0]} {item["day_lesson"]}강'
    return f'{item["id"]}강'

def nav(current):
    days = {}
    for item in lessons:
        days.setdefault(item.get('day', 1), []).append(item)
    groups = []
    for day, items in days.items():
        rows = []
        for item in items:
            number = f'<span class="num">{item["id"]:02d}</span>'
            title = escape(item['title'])
            if item['status'] == 'published':
                active = ' aria-current="page"' if item['id'] == current else ''
                rows.append(f'<li><a href="{item["slug"]}.html"{active}>{number}<span>{title}</span></a></li>')
            else:
                rows.append(f'<li><span class="upcoming">{number}<span>{title} · 예정</span></span></li>')
        groups.append(f'<details class="course-day"><summary>{escape(day_title(day))}</summary><ol>{"".join(rows)}</ol></details>')
    return '<aside class="course-sidebar"><details class="course-menu" open><summary>기초 네트워크 분석 · 전체 목차</summary><div class="course-days">' + ''.join(groups) + '</div></details></aside>'

for item in published:
    body_path = ROOT / f'content/notes/{item["slug"]}.html'
    body = body_path.read_text(encoding='utf-8')
    headings = re.findall(r'<section id="([^"]+)"[^>]*><h2>(.*?)</h2>', body)
    toc = '<nav class="toc" aria-label="이 노트의 목차"><strong>이 노트에서 배우는 내용</strong><ol>' + ''.join(f'<li><a href="#{anchor}">{title}</a></li>' for anchor,title in headings) + '</ol></nav>'
    idx = lessons.index(item)
    previous = lessons[idx-1] if idx else None
    following = lessons[idx+1] if idx+1 < len(lessons) else None
    pager = '<nav class="pager" aria-label="이전 및 다음 노트">'
    pager += f'<a href="{previous["slug"]}.html">← {lesson_label(previous)} {escape(previous["title"])}</a>' if previous else '<a href="../index.html#lesson">← 전체 학습 노트</a>'
    if following:
        pager += f'<a href="{following["slug"]}.html">{lesson_label(following)} {escape(following["title"])} →</a>' if following['status']=='published' else f'<span class="pending">다음 · {escape(following["title"])} · 준비 중</span>'
    pager += '</nav>'
    title = escape(item['title']); description = escape(item['description'])
    day_badge = f'<span>{escape(lesson_label(item))}</span>' if 'day_lesson' in item else ''
    page = f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#090e18"><meta name="description" content="{description}"><title>{item['id']:02d} {title} | DFIR Training</title><link rel="canonical" href="https://dfirwiz.github.io/dfir-training/notes/{item['slug']}.html"><link rel="preconnect" href="https://cdn.jsdelivr.net"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;family=JetBrains+Mono:wght@400;500;600&amp;display=swap" rel="stylesheet"><link rel="stylesheet" href="../assets/site.css"><link rel="stylesheet" href="../assets/notes.css"></head><body><a class="skip" href="#content">본문으로 건너뛰기</a><header class="shell nav"><a class="brand" href="../index.html"><span class="mark">D</span>DFIR TRAINING</a><nav class="navlinks" aria-label="주요 메뉴"><a href="../index.html#courses">교육 과정</a><a href="../index.html#lesson">학습 노트</a></nav><a class="navbtn" href="../index.html#lesson">전체 목차 ↗</a></header><div class="note-layout">{nav(item['id'])}<main class="note" id="content"><p class="breadcrumb"><a href="../index.html#courses">네트워크 트래픽 분석과 위협 탐지</a> / 기초</p><header class="note-header"><div class="eyebrow">FOUNDATIONS / NOTE {item['id']:02d}</div><h1>{title}</h1><p class="description">{description}</p><div class="meta"><span>학습 노트 {item['id']:02d}</span><span>약 {item['minutes']}분</span><span>업데이트 {item['updated']}</span></div></header>{toc}{body}{pager}</main></div><footer class="note-footer">© 2026 DFIR Training · 관찰한 사실과 추론을 구분하는 학습</footer></body></html>'''
    if day_badge:
        page = page.replace('<div class="meta">', '<div class="meta">' + day_badge, 1)
    (ROOT / f'notes/{item["slug"]}.html').write_text(page, encoding='utf-8')

cards = []
last_day = None
for item in lessons:
    day = item.get('day', 1)
    if day != last_day:
        cards.append(f'<h3 class="catalog-group">{escape(day_title(day))}</h3>')
        last_day = day
    title=escape(item['title']); desc=escape(item['description'])
    if item['status']=='published':
        day_label = f' / {lesson_label(item)}' if 'day_lesson' in item else ''
        cards.append(f'<a class="note-card live" href="notes/{item["slug"]}.html"><span class="number">NOTE {item["id"]:02d}{day_label} / 공개</span><h3>{title}</h3><p>{desc}</p><span class="read">약 {item["minutes"]}분 · 노트 읽기 ↗</span></a>')
    else:
        cards.append(f'<div class="note-card planned"><span class="number">NOTE {item["id"]:02d} / 예정</span><h3>{title}</h3><p>{desc}</p></div>')
catalog = f'''<section class="section" id="lesson"><div class="shell"><div class="eyebrow">03 / FIELD NOTES</div><h2>순서대로 읽는 학습 노트</h2><p class="intro">기초 네트워크 분석부터 차근차근. 쉬운 해설, 최신 보충, 표와 구조도를 함께 읽고 조사에 적용합니다.</p><div class="catalog-progress"><span>기초 과정 {len(published)} / {len(lessons)}강 공개</span><progress value="{len(published)}" max="{len(lessons)}" aria-label="기초 과정 공개 진행률">{len(published)} / {len(lessons)}</progress><span>최근 업데이트 {course['updated']}</span></div><div class="catalog-grid">{''.join(cards)}</div></div></section>'''
p=ROOT/'index.html'; text=p.read_text(encoding='utf-8')
text=re.sub(r'<!-- NOTES:START -->.*?<!-- NOTES:END -->','<!-- NOTES:START -->\n'+catalog+'\n<!-- NOTES:END -->',text,flags=re.S)
p.write_text(text, encoding='utf-8')
print(f'Rendered {len(published)} notes and {len(lessons)} catalog entries')
