# TamaPoke v3.97.1 DMUL 16~22 진화 구조

- 일반 분기: ATK / DEF / SPE / HP 중 가장 높은 훈련치가 분기를 결정합니다.
- 동률이면 해당 종의 기본 style을 먼저 사용하고, 이후 ATK→DEF→SPE→HP 순으로 결정합니다.
- Moonmon, Pokomon, Koromon에는 4방향 외 추가 성장기 확보를 위한 제어 가능한 특수 분기가 있습니다.
  - Moonmon: 네 훈련치가 모두 같고 총합 4 이상 → Penmon
  - Pokomon: 네 훈련치가 모두 같고 총합 4 이상 → Phascomon
  - Koromon: 네 훈련치가 모두 같고 총합 4 이상 → Patamon
  - Koromon: ATK=SPE>=3이고 둘 다 DEF/HP보다 높음 → Coronamon

## 특수진화 / 조그레스

> v3.94.2부터 디지몬 진화 판정에서 돌봄 실수 조건을 완전히 제거했습니다. v3.97.1에서도 동일하게 유지됩니다. 돌봄 실수 수치가 많거나 적어도 진화 루트에는 영향을 주지 않습니다.

- 듀크몬 → 듀크몬 CM: Lv.60+, ATK+SPE 80+
- Alphamon + Ouryumon → Alphamon Ouryuken: 각 Lv.55 기록
- Slayerdramon + Breakdramon → Examon: 각 Lv.55 기록
- Diablomon → Armagemon: Lv.60+, ATK 80+, Kuramon Lv.5+ 육성 기록
- Dianamon + Apollomon → GraceNovamon: 각 Lv.55 기록
- 미라쥬가오가몬 → 미라쥬가오가몬 BM: Lv.60+, ATK+SPE 90+
- 베르제브몬 → 베르제브몬 BM: Lv.60+, ATK+SPE 90+, Baalmon Lv.45+ 기록
- Jesmon + Gankoomon → JESmon GX: Jesmon Lv.60+, Gankoomon Lv.55+ 기록
- 루체몬 → 루체몬 FD: Lv.45+, 총 훈련 70+
- 루체몬 FD → 루체몬 SM: Lv.60+, ATK+HP 90+
- 엑스브이몬 + 스나이몬 → 파일드라몬 / 스나이몬 + 엑스브이몬 → 다이노몬: 각 Lv.25 기록
- 아큐라몬 + 가트몬 → 실피드몬: 각 Lv.25 기록
- 황금아르마몬 + 엔젤몬 → 토우몬: 각 Lv.25 기록
- Paildramon/Dinobeemon → 황제드라몬 DM: Lv.45+
- 황제드라몬 DM → 황제드라몬 FM: Lv.55+, ATK+SPE 60+
- 황제드라몬 FM + 오메가몬 육성 기록 → 황제드라몬 PM: Fighter Lv.60+, Omegamon Lv.55+
- 황제드라몬 PM → 황제드라몬 OX: Lv.70+, ATK+SPE 100+

기존 Omnimon Alter-S, Chaosmon, Millenniummon, Chaosdramon 및 Pendulum 조그레스는 유지됩니다.


## v3.97.1 조그레스 선택 방식
- 조그레스/융합은 일반 진화와 분리했습니다.
- 조그레스 조건을 충족해도 ATK/DEF/SPE/HP 기반 일반 진화가 자동으로 막히지 않습니다.
- 일반 진화와 조그레스가 동시에 가능하면 상태 카드에 `일반 진화`와 `조그레스` 버튼이 함께 표시됩니다.
- 조그레스는 사용자가 `조그레스`를 직접 선택한 경우에만 실행됩니다.
- 대상: 기존 융합체, Pendulum 조그레스, Alphamon Ouryuken, Examon, GraceNovamon, JESmon GX, Paildramon/Dinobeemon/Silphymon/Shakkoumon.
