자체 가상 EML2개와외부수집문맥JSON입니다. 실제메일·서버로그·인증·원본워크북자료가아닙니다.
python inspect_email.py message-a.eml context.json
python inspect_email.py message-b.eml context.json
Python3표준라이브러리만사용/로컬파일읽기·출력만합니다. 링크열기·DNS조회·메일전송·서명검증·첨부실행없음.
두EML은서로다른자료이며SHA256으로각각문맥에연결합니다. 해시일치가수집경로의신뢰성을인증하지않습니다. receiver_provenance_claim은가상입력가정,실제수신자생성검증은false입니다.
A는상단보고를수신자가남겼다는가정에서엄격도메인일치한DKIM성공주장을사용합니다. B는같은authserv-id가있어도수집경로미확인가정이라결과null입니다. 둘다실제SPF/DKIM/DMARC검증결과가아닙니다.
단순고정형식:From한개메일함/ASCII도메인/Authentication-Results선택인덱스/단일SPF·DKIM주장/Received2개만지원. 일반AR문법·다중서명·DNS트리탐색·완화정렬·DKIM정규화/암호검증·모든MIME/SMTP상태기계는미구현.
Received4초는헤더의시각주장차이이며실제전송지연검증아닙니다. smtp_data_accepted_claim은별도JSON가정이며최종받은편지함·열람·클릭·실행·피싱성공을증명하지않습니다.
실제검증모두false/사건unresolved/외부0. 종료2는문맥해시·입력·지원범위오류이며실제인증실패아닙니다. EML은CRLF바이트그대로비교하세요.
