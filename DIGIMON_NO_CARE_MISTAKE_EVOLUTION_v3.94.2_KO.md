# TamaPoke v3.94.2 — 디지몬 돌봄 실수 진화 조건 제거

## 변경 내용
- 디지몬 진화 함수에서 `careMistakes` 입력 자체를 제거했습니다.
- DMUL 일반 분기는 ATK/DEF/SPE/HP 훈련치만으로 결정됩니다.
- 다음 특수진화에서 돌봄 실수 조건을 제거했습니다.
  - Dukemon → Dukemon Crimson Mode: Lv.60+, ATK+SPE 80+
  - MirageGaogamon → MirageGaogamon Burst Mode: Lv.60+, ATK+SPE 90+
  - Lucemon → Lucemon Falldown Mode: Lv.45+, 총 훈련 70+
  - Lucemon Falldown Mode → Lucemon Satan Mode: Lv.60+, ATK+HP 90+
- 조그레스 및 기존 육성 기록 조건은 그대로 유지합니다.

## 호환성
- `careMistakes` 저장값 자체는 삭제하지 않았습니다. 기존 세이브/돌봄 기록 호환성을 유지하기 위해 보존합니다.
- 포켓몬 쪽 기존 돌봄 실수 기반 진화 지연 로직은 이번 패치 범위에서 변경하지 않았습니다.
- SAVE_VERSION은 2를 유지합니다.
