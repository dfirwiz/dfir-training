# 첫째 날 상세 개정 최종 누락 점검 — 2026-11-02

판정: **부분 검토 통과, 전체 완료 보류**. 1~22강의 상세 개정은 끝났으나 원본 전자 워크북 전체 학습 목표/문제 목록에 대한 재접근이 막혀 최종 무누락 판정을 내리지 않는다. editorial_revision.status는 in_progress, final_coverage_audit는 blocked_source_access로 유지한다. 회차 수나 과거 progress.status=completed를 완료 근거로 쓰지 않는다.

## 실제 수행한 대조

- 최신 course의 첫째 날 대상(day 생략 또는1)은 정확히1~22강이다. 1~21강 인쇄범위는4~167쪽164페이지에 한 번씩 대응하며 누락·중복 범위가 없다. 22강은 별도 실습 보충이다. 둘째 날23강과 다른 과정은 검토/수정 범위에 넣지 않았다.
- 각 개정 검토의 원문 학습 포인트 대응표와 현재 본문 절·예제·복습 연결을 읽고 확인했다. 과거 최종 점검표의 대표 앵커 중 실제 이름이 바뀐 것은 현재 본문을 기준으로 기록했다. 이 검사는 모든 원문 페이지164장의 이번 재열람이나 모든 실습 재실행이 아니다.
- 본 교재 원본을 다시 확보하고 인쇄50/70/90/110/143/167쪽의 실습 안내 이미지6개와 OCR을 이번에 직접 대조했다. 워크북을 참조하는 안내와 실제 문제 본문을 구별했다. 전용 음성·VM 정답을 복원하지 않았다.
- 이전 원문 범위별 직접 대조와 현재 개정 본문 연결에서, 기록된 학습 포인트의 누락은 발견하지 못했다. 단, 이는 접근 가능한 대응 기록에 대한 판정이며 원본 워크북의 모든 문제/힌트를 직접 재확인했다는 뜻이 아니다.

## 본 교재 기록과 현재 본문의 대응

|회차|인쇄범위|대응 기록의 핵심 학습 목표|현재 존재를 확인한 대표 절|
|---|---|---|---|
|1|4~11|자료와 실습 한계·학습 방법·기초가 필요한 이유·패킷의 가치·경고/규칙/관련 로그의 검증|goal / packet / roadmap / alert / workflow / modern-value|
|2|12~21|관찰→가설→검증→보고, Echo 필드·간격·도구 식별, SYN 탐색과 터널·우선순위|sweep / read-pcap / fingerprint / syn / tunnel / timeline|
|3|22~30|계층·캡슐화·식별자·길이·옵션·원시 바이트 경계·제한|layers / encapsulation / decapsulation / length / options / worked-example|
|4|31~45|비트/니블/바이트·진법·자리값·오프셋·덤프·길이와ID 계산|units / place-value / binary / hex / nibbles / conversion / offset / dump / id|
|5|46~50|정상 기준·명세·구현 차이·겹침·대상 구현과 종합 복습|rfc / current-specs / implementations / overlap / target / synthesis|
|6|51~56|도구 조합·파일 열기·세 패널·필터·바이트 위치|features / workflow / launch / panes / details / offset / filters|
|7|57~61|캡처 속성·시간·크기·계층 통계·대화·방향과 후보 선택|properties / sizes / hierarchy / conversations / sorting / decision|
|8|62~70|Follow·양방향 SMTP·필터·검색 영역·HTTP 헤더·선언 길이와 실제 자료|follow / direction / scope / search / http / length / objects|
|9|71~76|링크 형식·주소·Type/Length·길이·충돌·FCS·VLAN과 관측|family / frame / type / length / collision / fcs / tools / vlan / visibility|
|10|77~83|경로·다음 홉·ARP 요청/응답·전체 필드·캐시와 전달 표·IPv6 차이|routing / request / reply / fields / bytes / cache / tables / ipv6|
|11|84~90|캐시 오염·양방향 전달·경쟁 응답·CAM·방어별 역할과 한계|learning / scenario / forwarding / competing / cam / controls / dai / verification|
|12|91~100|IPv4 전체 지도·Version/IHL·옵션·ToS/DSCP/ECN·Total Length·ID|map / version / ihl / options / tos / dscp / ecn / total-length / identification / idle|
|13|101~110|Flags·TTL·ICMP 인용·Protocol·체크섬·주소·옵션/소스 경로|fragment-bits / ttl / icmp / protocol / checksum-math / addresses / subnets / options / source-route|
|14|111~121|MTU·DF/MF·ID/묶음·Offset×8·길이 단위·비트와 분류|mtu / payload / identity / df / mf / offset / units / bitfield / classification|
|15|122~126|전체/헤더/데이터 길이·덤프·원시 오프셋·끝 위치·계산 문제|commands / first-length / last-length / offset / join / assumptions / exercise|
|16|127~139|중첩·중복·재조립 정책·세 조각 계산·도구 표시·필터·체크섬|overlap / duplicate / standards / sensor-policy / first / remaining / overhead / wireshark / filters / checksums|
|17|140~143|VPN 안팎·오버헤드·DF·PMTU·DHCP MTU·MSS·손실/시간 초과|budget / df / pmtu / dhcp / mss / loss / timeout / workflow|
|18|144~154|셸 입출력·파이프·페이저·cut/awk/sort/uniq/head/wc의 옵션·단위와 집계|pipes / pagers / cut-position / cut-fields / stack-cut / awk / sort / uniq / pipeline / wc|
|19|155~158|전용 회수 도구·바이너리/텍스트·stdin·기록 수·grep/sed|retrieval / binary / stdin / count / capinfos / grep-current / grep-example / sed / sed-example|
|20|159~163|정규식의 기초·메타문자·반복·집합·앵커·탐욕성과 첫 두 예제|context / atoms / repetition / sets / anchors / greedy / engine / example-one / example-two|
|21|164~167|세 결합식의 부분 일치/실패/전체 일치·부정 집합·연습 안내·종합|read-pattern / partial / plus / negated / counterexamples / outputs / synthesis / review|
|22|별도 보충|워크북 기록의 여섯 실습 주제·IPv6 확장·자료 역할과 실행 한계|tcpdump / wireshark / link / ipv4 / fragments / ipv6-basics / ipv6-practice / review / pcap-validation|

범위별 세부 대응은 각 lesson-01~22-rewrite 검토(1강은2026-11-01, 나머지는2026-11-02)를 따른다. 옛 coverage 파일의 당시 다음 회차나 자료 미제공 표현은 현재 진행 정보로 사용하지 않는다.

## 워크북 기록의 목표 대응

|기존 검토가 확인한 범주|현재 강의 연결|이번 확인|원본 전체 목록 판정|
|---|---|---|---|
|계층·tcpdump|3~5,18,22#tcpdump|옵션·이름 변환·식별값·기준점·길이 유지|보류|
|Wireshark|6~8,22#wireshark|통계·대화·헤더 끝·검색/스트림·TCP옵션 유지|보류|
|링크 계층|9~11,22#link|ARP·충돌·자발적공지·학습자원·검증 유지|보류|
|IPv4|12~13,22#ipv4|Version/IHL·주소·길이·체크섬·수집조건 유지|보류|
|단편화|14~17,22#fragments|첫/끝·복사옵션·구간/누락·필터·중첩 유지|보류|
|IPv6|22#ipv6-basics,22#ipv6-practice|RS/RA/NS/NA·확장 헤더·조각·주소대응 보강|보류|

첫째 날 PCAP6개/621기록 및 워크북 문제·힌트·기재 해설의 기존 오프라인 검증 기록은 보존한다. 이번에 그 원본을 다시 열거나 재실행하지 않았다. Library 검색과 연결된 이전 작업의 자료 위치 조회에서는 현재 재접근할 전자 워크북 파일/URL을 확보하지 못했다. 이전에 자료가 제공되지 않았다고 결론 내린 것이 아니라, **현재 원본 전체 목록과 대조할 접근 경로가 없다는 미해결 상태**다. 개인 경로나 원본 식별자는 공개하지 않는다.

## 검증과 한계

24HTML 구조·중복ID·로컬 경로/앵커, 22강 기존158텍스트항목 보존, 그림XML·범례/단위, 독립바이트·길이·구간·164페이지 연속성과22강 존재를 포함한42조건을 검사했다. 다른 회차를 구버전으로 덮어쓰지 않았다. 실제 GUI/모바일 화면은 브라우저 초기화의 파일시스템 오류로 미검증이며 임의 서버/브라우저로 우회하지 않았다. 원본PCAP·전용VM·실제 스위치/라우터·피해 호스트 반응·음성 답안·운영 공격/탐지 성능은 이번에 검증하지 않았다.

## 미해결 항목과 재개 조건

1. 원본 첫째 날 전자 워크북의 전체 학습 목표·문제·힌트 목록에 접근한다.
2. 그 목록을 위 여섯 범주뿐 아니라 실제 세부 항목별로 현재1~22강에 대응한다. 누락이 있으면 상세 설명을 보강하고 다시 검증한다.
3. 미해결 항목이 없어야 editorial_revision.status=completed와최종감사통과를기록한다. 현재는completed로처리하지않는다.

현재 강의 개정 목록은1~22이며 새 강의는없다. next_lesson_id=null은강의추가가아닌최종감사가남았다는뜻이고status=in_progress/blocked_source_access가판정기준이다. 원본접근 없이는최종감사를더진행할수없으므로 이번변경배포를확인한뒤현재개정자동화만일시중지한다. 과거비활성연재를재활성화하지않는다. 재개에필요한자료는원본전자워크북파일또는접근가능한원본위치이다.
