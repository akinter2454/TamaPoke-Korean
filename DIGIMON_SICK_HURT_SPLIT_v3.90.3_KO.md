# TamaPoke v3.90.3 - Sick / Hurt 분리

## 같은 스프라이트, 다른 역할

- Hurt
  - DGI 13 <-> 14
  - 320 ms
  - 배틀 피격 전용
  - 기존 좌우 흔들림(jitter) 효과 유지

- Sick
  - DGI 13 <-> 14
  - 450 ms
  - 홈 화면 생활 상태 부족 표현
  - 흔들림 없음

## Sick 표시 조건

기존 `Pet::mood()` 판정을 그대로 사용합니다.

`lowestStat() < 25`

`lowestStat()`은 아래 네 상태 중 가장 낮은 값을 반환합니다.

- fullness (배고픔/포만도)
- joy (기쁨)
- energy (기력)
- hygiene (청결)

따라서 네 상태 중 하나라도 25 미만이면 홈 화면의 디지몬은 Sick 애니메이션을 사용합니다.

DGI 포맷과 SAVE_VERSION은 변경하지 않습니다.
