# TamaPoke KO v3.99.1 — 개발 기준선

현재 개발 기준은 **v3.99.1**이며 세이브 포맷은 **SAVE_VERSION 2**입니다.

## v3.99.1 핵심
- v3.99.0 GitHub Actions Arduino 컴파일에서 발생한 `CX was not declared in this scope` 오류 수정
- `CX`/`CY`를 원형 텍스트 helper보다 먼저 선언
- UI geometry 선언 순서 회귀검증 추가

## 유지 기능
- 5개 동시 육성 슬롯
- 체육관/미션/보스 배틀 이름 UTF-8 안전 표시
- 원형 466x466 화면 텍스트 Fit/말줄임 보호
- 디지몬 알고리즘 Shiny 및 Shiny 도감 기록
- 일반 진화/Jogress 분리 및 DMUL 지배 스탯 분기

## 불변 조건
- Digimon ID 0..457은 이동/재사용 금지, 신규는 append-only
- Digimon 진화에 careMistakes를 조건으로 사용하지 않음
- `TamaPoke.ino`와 `firmware_source/TamaPoke.ino`는 byte-identical 유지
- `.github/workflows/main.yml`와 `GITHUB_WORKFLOW_COPY.txt`는 byte-identical 유지

## 다음 작업 전 검증
최소한 다음을 실행합니다.
- `tools/verify_ui_geometry_declaration_order_v3991.py`
- `tools/verify_text_bounds_v3981.py`
- `tools/verify_digimon_shiny_v3990.py`
- `tools/verify_save_compatibility.py`
- `tools/verify_care_slots_v3980.py`
- `tools/verify_battle_name_v3980.py`
그리고 GitHub Actions의 실제 `arduino-cli compile` 성공 여부를 최종 확인합니다.
