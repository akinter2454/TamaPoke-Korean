# TamaPoke v3.99.1 — UI Geometry Compile-Order Fix

## 증상
GitHub Actions의 `Compile current TamaPoke firmware` 단계에서 다음 오류가 발생했습니다.

- `uiDrawCenteredFit`: `CX was not declared in this scope`
- 같은 원인으로 `uiRoundTextWidth`의 `CY`도 선언 순서상 위험한 상태였습니다.

## 원인
v3.98.1에서 추가된 원형 화면 텍스트 경계 helper가 파일 앞부분에 위치했지만, `#define CX 233` / `#define CY 233`은 약 980줄 뒤에서 정의되어 있었습니다. C/C++ 전처리 매크로는 정의 이후에만 유효하므로 실제 Arduino 컴파일에서 실패했습니다.

## 수정
- `CX`, `CY`를 `FW_VERSION` 바로 뒤의 공통 화면 geometry 영역으로 이동했습니다.
- 뒤쪽의 중복 정의는 제거했습니다.
- `TamaPoke.ino`와 `firmware_source/TamaPoke.ino`를 동일하게 유지했습니다.
- `verify_ui_geometry_declaration_order_v3991.py`를 추가하고 GitHub Actions pre-compile verifier 목록에 포함했습니다.
- `verify_digimon_shiny_v3990.py`의 버전 검사를 기능 기준(3.99.0 이상)으로 바꿔 patch 버전에서 거짓 실패하지 않도록 했습니다.

## 호환성
- SAVE_VERSION: 2 유지
- 키우기 슬롯: 5 유지
- 디지몬: 458종(ID 0..457) 유지
- v3.99.0 알고리즘 Shiny 기능 변화 없음
- 게임 밸런스/진화/배틀 데이터 변화 없음
