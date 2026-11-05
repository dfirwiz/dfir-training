18강 자체 오프라인 워크플로 재생
네 파일:deliveries.json,workflow-contract.json,replay_workflow.py,README.txt
Python 표준 라이브러리만 사용합니다. 실제 SOAR/TheHive/Cortex/API 형식이나 실행이 아닙니다.
도메인과 이벤트·케이스·조회 결과는 전부 가상입니다.
python replay_workflow.py deliveries.json
python replay_workflow.py deliveries.json --max-attempts 1
기본:모의조회5회,중복계획1회생략,노트계획2개,미해결1개입니다.
프로그램은 미리 적힌 모의 결과를 읽습니다. 조회·대기·네트워크·케이스쓰기·차단을 실행하지 않습니다.
중복제거 상태는 같은 프로세스 실행 안의 계획에만 적용됩니다. 다시 실행하면 상태가 초기화됩니다.
종료0은재생계산성공이며미해결0을보장하지않습니다.잘못된입력은2입니다.
입력은수정하지않으며화면출력외의파일을만들지않습니다.자세한설명은18강본문에있습니다.
