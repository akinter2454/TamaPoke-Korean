# TamaPoke v3.90.5 compile-order fix

## 실제 컴파일 오류
`digiBehNext()`가 전역 `beh` 객체 선언보다 먼저 정의되어 Arduino C++ 컴파일에서
`beh was not declared in this scope`가 발생했습니다.

## 수정
- `digiBehNext()` 원형 선언만 앞쪽에 유지
- `beh` 전역 객체를 먼저 정의
- `digiBehNext()` 함수 본문을 `beh` 선언 뒤로 이동
- 동작 매핑/속도/Sick-Hurt 로직은 v3.90.4와 동일
- `verify_digimon_behavior_declaration_order.py` 추가
- Actions 사전검증에서 선언 순서를 확인하도록 추가
- FW_VERSION/Installer marker를 v3.90.5로 동기화

SAVE_VERSION 2 / DGI1-3 호환 유지.
