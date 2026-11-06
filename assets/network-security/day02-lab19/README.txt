둘째날19강 자체 가상 주장 비교입니다.실제WinRM/PowerShell/SSH로그·설정·패킷·원본워크북이아닙니다.
이폴더에서 python compare_remoting.py cases.json (Python3표준라이브러리)
프로그램은JSON만읽고출력합니다.서비스실행·원격접속·인증·리스너·TrustedHosts·방화벽·계정설정을바꾸지않습니다.
transport의wsman-http/wsman-https/ssh/unknown은작성자가가정한전송이며포트에서추론하지않습니다.보호값도미리주어진가정입니다.
W2의HTTP/Basic/보호없음은의도적인반례가정이며현재Windows기본설정이이를허용하거나실제로서버가받았다는뜻이아닙니다.Basic자체를메시지암호화라고입력하면도구오류2로거부합니다.
TrustedHosts나peer_identity_checked_in_fixture값은실제서버신원인증이아닙니다.모든actual_*와실제원격실행·두번째홉검증은false로남깁니다.
인증프로토콜전체·정책·버전·모든전송·실제암호협상·이벤트파서를구현하지않습니다.unknown은모르는것으로남깁니다.
종료0은로컬조건계산완료,2는입력/지원범위오류입니다.모든사건결론unresolved/외부행동0입니다.
