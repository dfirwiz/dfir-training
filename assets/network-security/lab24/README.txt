24강 독립 메타데이터 비교
metadata.json/check_metadata.py/field-notes.txt/README.txt를 같은 폴더에 둡니다.
Python 표준 라이브러리만 사용합니다. 실제 SAML 토큰·서명·제품 API가 아닙니다.
python check_metadata.py metadata.json
python check_metadata.py metadata.json --now 2026-11-01T11:05:00Z
기본 R1/R4: 교육 조건 일치. R2: 대상 불일치. R3: 기간 밖. 일치가 실제 인증 허용을 뜻하지 않습니다.
fixture_signature_ok는 미리 적은 가상 값이며 프로그램이 서명을 검증하지 않습니다. R4의 키 신뢰 침해도 판정하지 않습니다.
종료0: 비교 계산 완료(불일치 포함). 종료2: 입력 오류. 입력 변경·토큰 생성·외부 요청·로그인·조치가 없습니다.
