"""Original mobile-readable privilege and credential evidence diagrams."""
from blue_team_day01_diagrams import drawing

def build_privilege_credentials(assets):
 rows={
 'day03-03-consumer':('높은 권한의 소비 경계 조사',[
 ['입력을 누가 바꿀 수 있나','파일 · 폴더 · 실행 설정'],['누가 그 입력을 소비하나','실제 계정 · 토큰 · 요청 동작'],['어떤 조건으로 소비됐나','시작 · 로그온 · 서비스 · 작업'],['무엇이 실제로 성공했나','변경 · 문맥 · 결과 · 승인']],['입력 통제 확인','높은 문맥인지 확인','가능성과 수행 구별'],'아래: 조사 질문 순서\n구성 후보 ≠ 실제 권한 상승 성공'),
 'day03-03-kernel':('구성 문제와 커널 문제 구별',[
 ['높은 권한 결과의 원인은','정상 승인 · 구성 · 인증 · 취약점'],['커널 후보라면 적용 조건','정확한 빌드 · 코드 · 수정 상태'],['사건 당시 실행 조건','접근 · 실행 · 보호 · 관측 범위'],['성공 근거와 남는 한계','현재 설정 ≠ 과거 사건의 증명']],['다른 원인도 비교','버전 숫자만 보지 않기','사건 시점의 근거 대조'],'아래: 검증 순서 · 고정 공격 절차 아님\n근본 수정과 도구 제한 정책은 구별'),
 'day03-04-chain':('인증 자료에서 대상의 동작까지',[
 ['어떤 자료가 있다는 주장인가','암호 · 해시 · 티켓 · 캐시 검증값'],['실제로 얻고 사용했는가','형태 · 출처 · 보호 · 수집 범위'],['대상이 인증을 수락했는가','계정 · 대상 · 시각 · 인증 방식'],['권한과 실제 동작은 무엇인가','세션 · 인가 · 결과 · 승인']],['자료 종류부터 구별','추출과 재사용 분리','인증과 동작 분리'],'아래: 조사 질문 · 자동 성공 경로 아님\n자료 이름 ≠ 실제 비밀·유효성·재사용'),
 'day03-04-protection':('인증 비밀의 보호 범위 질문',[
 ['어떤 비밀·저장 구조인가','세션 메모리 · 로컬 저장 · 앱'],['어떤 보호가 적용되나','LSA 보호 · Credential Guard 등'],['이 장치에서 실제 동작하나','버전 · 역할 · 요구 조건 · 정책'],['보호 밖의 위험도 확인','입력 · 앱 비밀 · 현재 권한 오용']],['보관 위치를 합치지 않기','기본값과 실제 상태 구별','한 기능을 전체 보증으로 안 함'],'아래: 보호 범위 검토 순서\n모든 비밀이 같은 곳에 있다는 그림 아님'),
 'day03-04-evidence':('접근 기록과 성공 결론 나누기',[
 ['직접 관측한 기록의 종류','접근 · 자료 보고 · 인증 · 동작'],['같은 사건이라는 연결 가설','계정 · 대상 · 시각 · 식별자'],['추가 입증할 실제 결과','추출 · 자료 재사용 · 권한 · 승인'],['수집 공백과 판단을 기록','가상 후보 ≠ 실제 탈취·침해 성공']],['종류 존재 ≠ 내용 검증','시간 인접 ≠ 원인 증명','정상 작업 가설도 대조'],'아래: 조사 강도를 나누는 순서\n실습은 가상 분류·주장만 비교')}
 for name,(title,boxes,labels,foot) in rows.items():
  svg=drawing(title,[(40,60+i*125,320,68,b) for i,b in enumerate(boxes)],[(f'185,{128+i*125} 185,{185+i*125}',label,268,160+i*125) for i,label in enumerate(labels)],foot,565)
  (assets/(name+'.svg')).write_text(svg,encoding='utf-8')
 # Two excerpts of a fictional 16-byte page boundary; no exploit/OS diagram.
 s=['<svg xmlns="http://www.w3.org/2000/svg" width="400" height="565" viewBox="0 0 400 565" role="img" aria-labelledby="title desc"><title id="title">가상 페이지 끝의 범위 비교</title><desc id="desc">왼쪽에서 오른쪽 바이트 위치13부터17. R4는14와15만 포함하고 R3는16까지 포함해 경계를 넘는다. 페이지16바이트는 자체 가정이다.</desc><rect width="400" height="100%" rx="14" fill="#0e1927"/><style>text{font-family:Pretendard,Arial,sans-serif;fill:#deeee9;font-size:16px}.heading{font-size:18px;font-weight:700}.label{font-size:14px;fill:#a8c9d5}</style><defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8" fill="none" stroke="#78e3c5"/></marker></defs><text class="heading" x="200" y="32" text-anchor="middle">가상 페이지 끝의 범위 비교</text><text class="label" x="200" y="60" text-anchor="middle">P=16바이트 · 위치 13–17만 발췌</text>']
 for y,label,active,over in [(110,'R4 · 시작14 / 길이2 / 끝16',2,False),(300,'R3 · 시작14 / 길이3 / 끝17',3,True)]:
  s.append(f'<text x="200" y="{y}" text-anchor="middle">{label}</text>')
  for j,n in enumerate(range(13,18)):
   color='#9b4d2a' if over and n==16 else '#205a4d' if n in (14,15) else '#152d3a'
   s.append(f'<rect x="{40+j*64}" y="{y+30}" width="56" height="50" rx="5" fill="{color}" stroke="#426c7c"/><text x="{68+j*64}" y="{y+61}" text-anchor="middle">{n}</text>')
  s.append(f'<polyline points="228,{y+20} 228,{y+92}" fill="none" stroke="#ffbd70" stroke-width="2" stroke-dasharray="5 4"/><text class="label" x="228" y="{y+116}" text-anchor="middle">페이지 경계16</text>')
  s.append(f'<text class="label" x="200" y="{y+143}" text-anchor="middle">'+('14·15·16 포함 → 다음 페이지까지' if over else '14·15 포함 → 끝16은 포함 안 함')+'</text>')
 s.append('<polyline points="50,480 350,480" fill="none" stroke="#78e3c5" stroke-width="2" marker-end="url(#a)"/><text class="label" x="200" y="505" text-anchor="middle">오른쪽: 바이트 위치 증가 · 초록: 범위</text><text class="label" x="200" y="528" text-anchor="middle">주황: 넘은 부분 · 선: 페이지 경계</text><text class="label" x="200" y="550" text-anchor="middle">자체 정수 예제 · 실제 OS 페이지 측정 아님</text></svg>')
 (assets/'day03-03-range.svg').write_text(''.join(s),encoding='utf-8')
