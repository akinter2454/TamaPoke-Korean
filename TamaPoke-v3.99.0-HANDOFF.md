# TamaPoke KO v3.99.0 — 개발 기준선

현재 개발 기준은 **v3.99.0**이며 세이브 포맷은 **SAVE_VERSION 2**입니다.

## 현재 핵심 상태
- 키우기 슬롯 5개
- Digimon 458종 / ID 0..457 / 예약 용량 2048
- 체육관·미션·탐험·타워 배틀 이름은 dex 기반 표시
- UTF-8 말줄임 + 원형 AMOLED chord 기반 텍스트 경계 보호
- Digimon 일반 진화와 Jogress 분리, careMistakes 미사용
- DMC 후기 고정 가족 구조 및 DMUL 4종 훈련치 분기 유지

## v3.99.0 Digimon Shiny
- Digimon egg도 포켓몬과 같은 rare-variant roll을 사용합니다.
- good farewell / Shiny Charm next-egg boost가 Digimon에도 적용됩니다.
- Shiny Berry가 현재 Digimon에도 적용됩니다.
- 별도 Shiny sprite는 없습니다. `digiShinyColor565()`가 DGI RGB565 픽셀을 런타임 변환합니다.
- outline/highlight는 보존하며 색상은 species ID에 따라 결정적으로 변환됩니다.
- shiny 상태는 진화/Jogress/party/box/battle/care slot에 유지됩니다.
- `digiShinyReg` / NVS `digshy`로 Shiny 도감 기록을 저장합니다.

## 유지 불변 조건
- 기존 Digimon ID 이동 금지, 신규는 append-only
- `TamaPoke.ino == firmware_source/TamaPoke.ino`
- `.github/workflows/main.yml == GITHUB_WORKFLOW_COPY.txt`
- `tools/verify_digimon_shiny_v3990.py`를 CI에서 실행
- `tools/verify_text_bounds_v3981.py`도 계속 CI에서 실행
