이번 강의는 **두 번째 단원 ‘법과 준수 원칙’의 핵심 요약**입니다. 보안 검증을 시작하기 전에 무엇을 허락받고, 자료를 어떻게 다뤄야 하는지 짧게 정리하겠습니다.

영국 법률과 EU 제도를 중심으로 설명합니다. 호주·한국 등 다른 국가의 업무에 그대로 적용되는 법률 안내는 아니며, 실제 프로젝트에서는 해당 관할의 법률과 계약을 확인해야 합니다. 아래 사례는 독립적으로 작성한 가상 상황입니다.

## 1. 문이 열린다고 들어가도 될까요?

회사 웹 서버를 점검하던 중 같은 계정으로 협력사 서버에도 접속할 수 있다는 사실을 발견했다고 해봅시다. “취약점을 찾아주려는 목적이니까 괜찮겠지”라고 생각하기 쉽습니다. 하지만 **접속 가능성은 접근 허가를 뜻하지 않습니다.**

건물 점검 허가를 받았다고 옆 건물까지 들어갈 수 없는 것과 같습니다. 다만 디지털 환경에서는 한 로그인으로 여러 조직의 시스템에 접근할 수 있어 경계가 더 잘 보이지 않습니다. 대상뿐 아니라 허용 행동·기간·데이터·제3자 서비스까지 문서로 확인해야 합니다. **ROE(Rules of Engagement, 활동 수행 규칙)**는 이 경계를 실무적으로 정리한 약속이며, 필요한 법적 권한을 대신하지는 않습니다.

범위가 불명확하면 해당 행동을 멈추고, 연락 담당자에게 확인한 뒤 서면으로 범위를 갱신하세요. [영국 Computer Misuse Act](https://www.legislation.gov.uk/ukpga/1990/18/contents)는 무단 접근 등을 범죄로 규정합니다. 좋은 의도만으로 허가가 생기는 것은 아닙니다.

## 2. 영국 컴퓨터 오용법에서 기억할 것

법 조문 전체를 암기하기보다 어떤 행동을 통제하는지 구분하면 됩니다. 다음은 [현행 법률](https://www.legislation.gov.uk/ukpga/1990/18/contents)을 학습용으로 단순화한 표입니다.

| 조항 | 핵심 내용 | 보안 검증에서의 판단 |
| --- | --- | --- |
| Section 1 | 무단 컴퓨터 자료 접근 | 계정이 작동해도 승인 범위를 확인합니다. |
| Section 2 | 추가 범죄를 저지르거나 돕기 위한 무단 접근 | 접근 목적과 후속 행동도 판단 대상입니다. |
| Section 3 | 기능 방해 의도 또는 방해에 대한 무모함을 수반한 무단 행위 | 서비스 영향과 금지 행동을 사전에 정합니다. |
| Section 3A | 범죄에 사용할 도구·자료의 제작·공급·취득 등에 관한 요건 | 도구의 목적과 공급·사용 맥락을 봅니다. |
| Section 3ZA | 심각한 피해 또는 그 위험을 만드는 무단 행위 | 의료·에너지 등에서 피해의 규모와 안전을 고려합니다. |

Police and Justice Act 2006과 Serious Crime Act 2015는 이 법을 개정하며 관련 조항을 추가했습니다. 특히 **단순 사고만으로 Section 3 위반이 자동 성립하는 것은 아닙니다.** 무단성, 인식, 의도 또는 무모함 등 법정 요건을 따져야 합니다. 또한 [검찰 지침](https://www.cps.gov.uk/prosecution-guidance/computer-misuse-act)은 Section 3A에서 도구의 단순 보유만으로 범죄가 되지는 않는다고 설명합니다. 반대로 점검용 도구라는 이름만으로 모든 사용이 허용되는 것도 아닙니다.

## 3. 개인 영역과 증거의 신뢰성을 지키세요

[Human Rights Act 1998의 권리 조항](https://www.legislation.gov.uk/ukpga/1998/42/schedule/1)은 공정한 재판(Article 6), 사생활·통신 보호(Article 8), 재산 보호(제1의정서 Article 1)를 다룹니다. 직접적인 법적 의무가 누구에게 적용되는지는 공권력 행사 여부 등 맥락에 따라 달라집니다. 이를 실무에 연결하면 **개인 영역을 보호하고, 시스템·자료의 훼손을 피하며, 증거 취급을 설명할 수 있게 하라**는 원칙이 됩니다.

예를 들어 회사 노트북 점검 허가는 직원의 개인 클라우드나 집 공유기 조사 허가까지 뜻하지 않습니다. **BYOD(Bring Your Own Device, 개인 기기의 업무 사용)**와 재택근무에서는 업무 데이터와 개인 데이터의 경계를 별도로 합의해야 합니다.

조사 자료는 원본과 분석본을 구분하고, 수집 시각·출처·담당자·전달 이력을 남기세요. **해시(hash)**는 파일의 변경 여부를 비교하는 데 쓰는 값입니다. 해시가 일치해도 수집의 적법성이나 법정 증거능력이 자동 보장되지는 않습니다. 패킷에서 접속이 관측됐다는 사실과 “승인된 접속이었다”는 판단도 다릅니다. 승인 문서·시간대·대상 목록·작업 기록을 함께 봐야 합니다.

## 4. 개인정보는 필요한 만큼만 취급하세요

보안 점검 중에도 이름·이메일·세션 정보 등 개인정보가 수집될 수 있습니다. 영국의 Data Protection Act 2018과 UK GDPR을 고려해야 하는 이유입니다. 처리 목적과 방법을 정하는 주체가 **컨트롤러(controller)**, 그 주체의 지시에 따라 처리하는 주체가 **프로세서(processor)**입니다. 실제 역할을 확인하고, 필요한 처리 계약과 지침을 마련합니다.

[ICO의 7대 원칙](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/)을 점검 업무에 연결해 보겠습니다. 오른쪽은 이해를 돕기 위한 실무 예시입니다.

| 원칙 | 실무 예시 |
| --- | --- |
| 적법성·공정성·투명성 | 적절한 법적 근거와 고지·처리 조건을 확인합니다. |
| 목적 제한 | 점검 자료를 관계없는 목적으로 재사용하지 않습니다. |
| 최소 수집 | 취약점 입증에 필요한 최소 자료만 수집합니다. |
| 정확성 | 계정·시각·사람을 잘못 연결한 기록을 바로잡습니다. |
| 보관 제한 | 정당한 보관 필요와 합의된 기간을 검토하고 삭제합니다. |
| 무결성·기밀성 | 암호화, 접근 통제, 안전한 전달로 보호합니다. |
| 책임성 | 누가 무엇을 왜 처리했는지 설명할 기록을 남깁니다. |

예컨대 고객 정보가 노출된다는 사실을 입증하려고 전체 고객 목록을 내려받을 필요는 없습니다. 허용된 시험 데이터나 최소한의 마스킹 증거로 입증할 방법을 먼저 정하세요.

**최신 보충:** [Data (Use and Access) Act 2025](https://www.gov.uk/guidance/data-use-and-access-act-2025-data-protection-and-privacy-changes)는 기존 영국 개인정보 법체계를 대체하지 않고 일부를 개정합니다. ICO 지침도 갱신 중이므로 실제 처리 시점의 규정을 확인해야 합니다. 또한 EU GDPR과 UK GDPR은 구분해야 하며, 해외 조직에 적용되는지 여부를 단순히 “EU 거주자 데이터 보유”만으로 단정하지 않습니다. [역외 적용 조건](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/receiving-personal-information-from-the-eea/)에는 현지 사업장, 상품·서비스 제공, 행동 모니터링 등이 관련됩니다.

## 5. 업종별 규정과 시험 프레임워크도 확인하세요

금융·결제·의료 분야에서는 일반적인 접근 허가에 더해 해당 서비스의 규제와 운영 안전을 확인해야 합니다. 영국의 Financial Services and Markets Act, Payment Services Regulations, Health and Social Care Act 등 업종별 법령이 관련될 수 있습니다. 어떤 조항이 해당하는지는 조직과 업무에 따라 판단합니다.

여기서 **법률·규정**과 **시험 프레임워크**를 구분하세요. DORA는 EU 금융 분야의 디지털 운영 복원력 규정이며 2025년 1월 17일부터 적용됩니다. [CBEST](https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide)는 영국 금융 분야의 위협 정보 기반 평가 체계입니다. [TIBER-EU](https://www.ecb.europa.eu/press/intro/news/html/ecb.mipnews250211.en.html)는 위협 정보 기반 레드팀 시험 프레임워크이며, 2025년 DORA의 TLPT(Threat-Led Penetration Testing, 위협 기반 침투시험) 요건에 맞춰 갱신됐습니다. 프레임워크를 따른다는 사실이 개별 대상의 접근 허가를 대신하지는 않습니다.

## 6. 실행 전 확인과 짧은 복습

실행 전에는 **승인 권한자와 서면 범위, 제3자·개인 영역, 중단 조건과 연락처, 최소 수집·보호·삭제 방법, 증거·작업 이력**을 확인하세요. 허용 여부를 설명할 수 없다면 먼저 확인하는 것이 출발점입니다.

### 복습 1. 승인된 서버에서 협력사 계정을 발견했습니다. 접속해도 될까요?

**해설:** 그 사실만으로는 허용되지 않습니다. 협력사 대상과 행동을 승인할 권한이 있는 주체의 허가, 제3자 서비스 조건, ROE 범위를 확인해야 합니다. 불명확한 접속은 보류합니다.

### 복습 2. 고객 정보 노출을 찾았습니다. 전체 목록을 증거로 가져와야 할까요?

**해설:** 먼저 허용된 최소 증거로 입증할 방법을 선택합니다. 목적에 필요한 범위를 넘는 수집을 피하고, 마스킹·접근 통제·보관 기간을 적용합니다.

### 복습 3. 패킷에 접속 기록이 있고 파일 해시도 일치합니다. 적법한 활동임이 증명됐나요?

**해설:** 아직 아닙니다. 패킷은 관측된 통신을, 해시는 비교 대상 파일의 동일성을 뒷받침합니다. 활동의 적법성은 승인 권한·범위·시각·행동 등 별도 근거와 함께 판단해야 합니다.

## 7. 공식 근거와 확인일

확인일: **2026년 11월 2일**. 이 강의는 법적 개념을 익히는 교육용 요약입니다. 구체적인 사건 판단과 실제 프로젝트의 법적 요건은 해당 관할의 전문가 및 조직 담당자와 확인하세요.

- [Computer Misuse Act — 현행 조항](https://www.legislation.gov.uk/ukpga/1990/18/contents)
- [CPS — Computer Misuse Act 해설](https://www.cps.gov.uk/prosecution-guidance/computer-misuse-act)
- [Human Rights Act — 권리 조항](https://www.legislation.gov.uk/ukpga/1998/42/schedule/1)
- [ICO — 개인정보 보호 7대 원칙](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/)
- [영국 정부 — 2025년 개인정보 법률 개정](https://www.gov.uk/guidance/data-use-and-access-act-2025-data-protection-and-privacy-changes)
- [ICO — 영국·EU 개인정보법 적용 범위 안내](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/receiving-personal-information-from-the-eea/)
- [ESMA — DORA 개요와 적용일](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/digital-operational-resilience-act-dora)
- [Bank of England — CBEST](https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide)
- [ECB — DORA에 맞춘 TIBER-EU 개정](https://www.ecb.europa.eu/press/intro/news/html/ecb.mipnews250211.en.html)
