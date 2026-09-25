# TamaPoke KO v3.98.0 — 개발 기준선

현재 개발 기준은 **v3.98.0**입니다. 세이브 포맷은 **SAVE_VERSION 2**를 유지합니다.

## v3.98.0 변경
- 체육관 및 일반/미션·탐험·타워 계열 전투에서 한국어 종 이름이 `Combatant.name[12]`에 잘려 표시되던 문제 수정
- `Combatant.name`은 실제 별명 전용으로 사용하고, 기본 종 이름은 전투 표시 시 `dex`에서 다시 조회
- 동시 키우기 슬롯 **3개 → 5개**
- 기존 `care0~care2` 보존, 신규 `care3`, `care4` 추가
- 슬롯별 CRC A/B 복구 키도 `c0a/c0b ~ c4a/c4b`로 확장
- 중요 성장치 복구 가드 3슬롯 → 5슬롯 확장, v3.97.x의 3슬롯 가드(v2)를 새 가드(v3)로 읽어 마이그레이션
- 백업/복원은 기존 SAVE_VERSION 2와 호환. 구버전 백업에는 care3/4가 없으므로 새 슬롯은 빈 상태로 생성됨

## 유지 불변 조건
- Digimon 458종 / ID 0..457 / 예약 용량 2048
- 기존 Digimon ID 이동 금지, 신규는 append-only
- Digimon 진화에서 careMistakes 미사용
- 일반 진화와 Jogress 분리
- 체육관/타입보스 파티 선택의 현재·파티·박스 후보 구조 유지
- `TamaPoke.ino == firmware_source/TamaPoke.ino` 유지
- `.github/workflows/main.yml == GITHUB_WORKFLOW_COPY.txt` 유지
