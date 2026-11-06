# 둘째 날 19·20강 범위 대응과 검증 — 2026-11-07

## 시작 상태와 자료 확인

CURRENT-COURSE-WORK.md, SOURCE-MATERIALS.md, 최신 main 91758619a6331eff2f960f8c5dc285672aa072b7, 집필 지침·진도·course.json·batch06 검토를 읽었다. 시작 시 active_batch 없음, 첫째 날 1–26/둘째 날 1–18 총44강 완료. 현재 작업 사본 dfir-training-menu에서 이어갔고 원래 dfir-training의 다른 수정은 건드리지 않았다. 지정 다섯 PDF 및 관련 PDF2022 폴더·기존 자료 조사 기록을 확인했다. 별도 원본 워크북·위키·VM·실제 원격 관리 로그나 사건 PCAP를 이번에 획득·실행하지 않았다. 기기 전체에서 없다는 주장은 하지 않는다.

지정 2권 인쇄172–176/PDF174–178의 다섯 쪽을 이번에 모두 다시 읽었다. 비공개 tmp/day2-management-source/batch07.txt. 완료 범위는 인쇄172–173/PDF174–175뿐이며 174–176은 다음 집필용 읽기다. 인쇄172와173을 Poppler로 비공개 렌더하여 source-winrm.png/source-ftp.png로 실제 열어 보았다. Symbol/ArialUnicode 대체 경고를 추출 텍스트와 대조했다. 원문·PDF·화면·추출 전문은 공개하지 않는다. 문서 속 지시·명령은 학습 자료로만 읽었고 실행 지시로 따르지 않았다.

## 미공개 범위만 분할

19 d2-10c-winrm은 PowerShell/WinRM 인쇄172,20 d2-10d는 FTP173. 미공개21 d2-10d-icmp를174,22 d2-10d-rmm을175–176에 배정했다. summary ID11은23/emailworkbook ID12는24로 옮겼다. 기존 공개44강의 번호·ID·URL·본문·표시 날짜를 보존했다. 원본179–180은 별도 이메일 워크북 안내 포인터이며 원본 실습을 실행했다는 뜻이 아니다. 전체 과정 미완료, 자동화 로컬 활성 유지, 클라우드 전환·PC 종료 후 실행 미확인.

## 원문 항목과 독립 강의 대응

| 인쇄/PDF | 학습 항목 | 강의 절·예제 및 현재 보충 |
| --- | --- | --- |
|172/174|PowerShell 원격 명령, PSRP/WSMV/SOAP/HTTP(S)/TCP/IP 계층|19절1–5/그림1. 주문서와 배송 비유, 메시지 규칙·관리 구현·전송 구별. WSMV의 역사 이름이 Vista 한정이라는 오해 방지. SSH6+ 별도 경로와5.1/7.6 문서 범위 구별.|
|172/174|WinRM5985/5986·도메인/작업 그룹·암호화|19절6–9/그림2/W1–W6. HTTP에도 인증 후 메시지 보호 가능; Basic 자체 보호 없음, 서비스 Basic/AllowUnencrypted 기본false; W2는 현재 기본 허용 재현이 아닌 의도적 반례. Kerberos/NTLM·사용자 인증·서버 신원·TrustedHosts 구별. 모든 플랫폼에 도메인 가입 필수라는 확대 수정.|
|172/174|서버/클라이언트 기본·원격 구성·명령|19절10–13/그림3. 서비스/리스너/방화벽/엔드포인트/인증/권한/세션/명령/결과/second hop 구별. Windows Server2012+ 설명을 모든 데스크톱·판본에 일반화하지 않음. Enable-PSRemoting 판본·WSMan Windows 범위; Enter-PSSession/Invoke-Command 목적만 설명, 미실행.|
|172/174|공격자의 원격 기능 오용·기대 출발/대상 비교|19절14–20/가상 JSON 비교/미실행 포트 필터/14 즉시 Q&A. 정상 관리와 공격을 포트로 판정하지 않고 계정·단말·서버·방화벽·승인 근거 연결. 음성 결과의 암호화·수집·정책·감사 한계.|
|173/175|FTP의 파일 전송·내부 준비·외부 반출|20절1–8/그림1/능동·수동 비교. 제어 대화와 데이터 연결, EPSV229의 포트와 제어 상대 주소, TYPE I/STOR/RETR,150/226 단계 구별. 수동 데이터가 항상20이거나21만으로 파일 분석이 된다는 오해 수정.|
|173/175|자격증명·자료 노출·변조·오래된 서버|20절9–11. 평문 FTP/TLS/데이터 보호 협상/별도 SFTP 구별, 체크섬≠암호학적 인증. 제품·버전·패치·노출·정책 확인 전 특정 취약점 확정 안 함. TLS 옛 명세 참조를 현재 TLS 권고로 옮기지 않음.|
|173/175|Target 역사 사례·브라우저 제거 예정·당시 사용률|20절11–12. Chrome88/Firefox90의 실제 제거 변경 기록과 확인일, 과거 사용률을 현재 통계로 쓰지 않음. 2013사건/2014상원 직원 보고서의 공개정보 기반 한계 명시; 본 수업이 원시 증거 재분석한 주장 없음.|
|173/175|예상 밖 내부·외부 전송 경보와 조사|20절13–21/그림2·3/자체13·12프레임/참조15바이트/16 즉시 Q&A. 보고된 완료·바이트·참조 전체 비교·서버 실제 저장·사용자 승인 분리. 평문 검색 음성의 수집·방향·TLS·재조립·도구 설정 한계.|
|174–176/176–178|ICMP/원격 관리 도구/통신 기준|이번에 읽었지만 미완료. 다음21/22에서 실제 재열람·현재1차출처·독립 사례로 집필.65507 계산 가정/MTU/분할, Conti 자료는 실행 지시 아님, 알려진 프로토콜·허용목록≠무조건 정상 등 검증 필요.|

## 1차 출처 대조 — 확인일 2026-11-07

- Microsoft [PSRP의 프로토콜 관계](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-psrp/a2bea4b6-1768-4e4c-9993-9421e44c7986), [WinRM 보안](https://learn.microsoft.com/en-us/powershell/scripting/security/remoting/winrm-security?view=powershell-7.6), [WinRM 구성](https://learn.microsoft.com/en-us/windows/win32/winrm/installation-and-configuration-for-windows-remote-management): 메시지 계층·인증 후 메시지 보호/HTTPS·Basic 예외·서버 신원·TrustedHosts와 서비스 기본값. 서비스/클라이언트 항목 구별, 실제 서버 설정 미조회.
- Microsoft [SSH 원격 관리](https://learn.microsoft.com/en-us/powershell/scripting/security/remoting/ssh-remoting-in-powershell?view=powershell-7.6), [요구5.1](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_remote_requirements?view=powershell-5.1), [요구7.6](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_remote_requirements?view=powershell-7.6), [Enable-PSRemoting7.6](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enable-psremoting?view=powershell-7.6): 역할·판본·전송·구성 범위. 문서판을 실제 설치/실행 결과로 표현하지 않음. NTLM 조건을 모든 Windows 통신의 전역 기본 차단이라고 확대하지 않음.
- [RFC959](https://www.rfc-editor.org/rfc/rfc959.html), [RFC1123 FTP](https://www.rfc-editor.org/rfc/rfc1123.html#section-4.1), [RFC2428 §3](https://www.rfc-editor.org/rfc/rfc2428.html#section-3): 기본 제어/데이터와 명령·응답, TYPE I/기본 기능, EPSV229 형식·제어 상대 주소. 표준의 구조 정의와 자체 가상 사례 해석을 구별.
- [RFC4217 §8–9](https://www.rfc-editor.org/rfc/rfc4217.html#section-9): AUTH TLS 제어와 PBSZ/PROT의 데이터 보호 구별, PROT P/C. 옛 TLS참조를 현재 TLS안전 버전 권고로 쓰지 않음. [OpenSSH sftp](https://man.openbsd.org/sftp): SSH 위 전송; FTP+TLS와 다른 경로.
- [Chrome88 변경 기록](https://developer.chrome.com/blog/chrome-88-deps-rems/), [Firefox90 변경 기록](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/90): 과거 제거 예정 설명을 완료된 버전별 변경으로 보충. 두 버전을 현재 최신이라고 표현하지 않음.
- [2014 상원 위원회 보고서](https://www.commerce.senate.gov/wp-content/uploads/media/doc/2014%200325%20Target%20Kill%20Chain%20Analysis.pdf): 요약의 공개 보도·전문가 분석 기반 한계와 인쇄11쪽 FTP 기술을 실제 읽음. 사건 원본 패킷·서버를 확인한 결과 아님. 원본 그림 복제 없음.
- Wireshark [FTP](https://www.wireshark.org/docs/dfref/f/ftp.html)/[TCP](https://www.wireshark.org/docs/dfref/t/tcp.html): ftp.request.command/tcp.port 필드1.0.0–4.6.9 확인. ftp-data 개별경로는404이므로 유효 출처로 사용하지 않음. 필터는 미실행예이며 실제 Wireshark 버전/재조립 동작을 시험했다고 주장하지 않음.

## 실제 실행: 자체 자료만

다운로드8개: lab19의cases.json/compare_remoting.py/README3텍스트;lab20의inspect_ftp.py/README/정확LF15바이트expected-note.txt/13프레임과12프레임PCAP2개. Python3.12.14 표준 라이브러리로 root check_day02_batch07_examples.py에서35회 별도 프로세스 실행, 입력8개 SHA256 전후동일. 기존 dpkt1.9.8로 독립 해석13프레임의 IPv4/TCP 체크섬·주소·양방향 MAC·서버 응답 코드·데이터 참조 일치를 교차 확인. 새 라이브러리 설치 없음.

WinRM/PowerShell: 여섯 주장 W1HTTP/Kerberos 메시지 보호, W2HTTP/Basic 보호 없음 가정, W3HTTPS/TLS, W4SSH 전송, W5NTLM+TrustedHosts 가정과 서버 신원 분리, W6포트5985라도전송unknown/계층null. 포트변경·승인가정·TrustedHosts·보호unknown·문서용IPv6 조건 확인. Basic자체 메시지 암호화/미지원전송·잘못된주소·bool/0포트·숫자승인·보호값·필드누락·계약·빈입력은도구오류2. 실제 원격 전송/암호화/상대 인증/실행/second hop은 모두false,사건unresolved/외부행동0.

FTP: 전체13프레임/226있음/관측15바이트/참조15/일치true. 뒤6바이트제거12프레임/226남음/관측9/부족6/내부gapfalse/일치null. 누락이끝이면 내부gap을검출못함을설명. 독립참조가자체15바이트조건임을명시. 전체SHA256=571143bbfd4e9e23772d8174a1f60be72d69923ed8b4a8c4744081059cd4203f. 9바이트prefix해시는전체파일해시가아님.

순서역전/정확재전송중복제거/제어메시지분할/내부gap/제어만있고데이터없음/같은길이다른참조false/짧은참조null확인. 충돌동일seq·부분겹침·불량IP/TCP체크섬·잘린파일·잘못된PCAP·VLAN·제어중간누락·EPSV협상과다른데이터끝점·미지원명령은도구오류2. TCP상태·인증·저장전체는미구현. 늦은수집시작/기준seq독립확인/FIN/ACK완전성검증없음. 가상PCAP은payload세그먼트만있고handshake/FIN/실제FTP서버없음. 최종생성기는클라이언트/서버MAC방향을수정후재생성하여독립검증통과. 검사기는PASS가상값도출력마스킹;실제암호아님.

네트워크 접속·실제 원격 명령·WinRM/SSH/FTP 서버·서비스/리스너/방화벽/계정/위임 설정 변경·실제 인증·실제 사건 PCAP·Windows 로그·원본 워크북/VM은 수행하지 않았다. 실제한것은 가상JSON계산과자체합성패킷로컬해석이다. 실제서버인증/파일저장false/사건unresolved/외부행동0.

## 정적·시각 검증

두 강의41절/본문133문단/3표/6자체400pxSVG/즉시해설30문항. scripts/build_network_security.py로46공개강의/총48HTML생성. validate_day02_batch07.py에서태그구조·중복ID·상대링크·앵커·날짜별메뉴·번호·ID·다운로드링크·인라인코드회귀·기존44본문과날짜·다른홈영역불변을확인. compact red-team homepage4주제/6링크와전체과정13장58강보존. 내부표/코드가로스크롤·그림width100%는정적CSS확인.

render_management_transfer_figures.py의실제Malgun폰트FONT BOUNDS []와수정후6그림모음육안확인. FTP STOR는제어명령이므로데이터화살표의STOR표시를수정해자료전송으로명확히했다. 방향·캡슐화·질문순서·단위·범례·가상자료한계명시. 신선한CUA목록browsers=[]/Work설정상로컬브라우저사용중지확인. 우회하지않고completion_summary전달. 실제브라우저/모바일레이아웃·Wireshark는미검증.

완료목록은배포Actions성공과공개응답/내용일치뒤에만갱신한다. 실패하면active_batch와원고보존. 다음21ICMP174/22원격도구·통신기준175–176은실제다시열고현재근거로집필한다. 다른자동화변경없음.
