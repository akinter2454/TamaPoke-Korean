# TamaPoke v3.97.0 — 디지몬 이름/진화 조건 가독성 개선

## 목표
작은 원형 화면에서 긴 디지몬 이름과 복잡한 진화 조건을 외부 PDF 없이 빠르게 읽을 수 있도록 표시 계층을 단순화했습니다.

## 긴 이름 축약
전체 한국어 이름 표와 내부 species key/ID는 그대로 유지하고, 화면에 표시할 때만 `digimonNameKoShort()`를 사용합니다.

주요 예시:
- Omegamon Alter-S → `오메가몬S`
- Dukemon Crimson Mode → `듀크몬 CM`
- MirageGaogamon Burst Mode → `미라쥬가오가몬 BM`
- Beelzebumon Blast Mode → `베르제브몬 BM`
- Lucemon Falldown Mode → `루체몬 FD`
- Lucemon Satan Mode → `루체몬 SM`
- Imperialdramon Dragon/Fighter/Paladin Mode → `황제드라몬 DM/FM/PM`
- Imperialdramon OmegaX → `황제드라몬 OX`
- Coredramon Blue/Green → `코어드라몬 청/녹`
- MetalGreymon Virus → `메탈그레이몬V`

## 한국어 이름 교정
한국어로 이름이 크게 달라지는 종은 디지몬 공식 종합 사이트의 한국어 도감 표기를 우선 기준으로 확인해 교정했습니다.

대표 교정:
- Gabumon → 파피몬
- Numemon → 워매몬
- Mamemon / MetalMamemon / BigMamemon → 콩알몬 / 메탈콩알몬 / 빅콩알몬
- Monzaemon / WaruMonzaemon → 퍼펫몬 / 배드퍼펫몬
- Yukidarumon → 프리지몬
- Centalmon → 켄터스몬
- Whamon → 고래몬
- Bakemon → 고스몬
- Drimogemon → 두리몬
- Giromon → 째리몬
- Coelamon → 실리컨몬
- Nanimon → 모야몬
- Devidramon → 데블드라몬
- Tuskmon → 태스크몬
- Mugendramon → 파워드라몬
- Nanomon → 데이터몬
- Hangyomon → 다이버몬
- Dagomon → 드라고몬
- Gladimon → 그라디몬
- Reppamon → 레파몬
- Duftmon → 두프트몬
- Wormmon → 추추몬
- Aquilamon → 아큐라몬
- Ankylomon → 황금아르마몬
- JewelBeemon → 주엘비몬
- Dinobeemon → 다이노몬
- Silphymon → 실피드몬
- Shakkoumon → 토우몬

※ 공식 한국어 도감 자체도 비일본어 페이지 일부에 기계 번역을 사용하며, 각 언어의 명칭이 확정되면 표기가 바뀔 수 있다고 안내합니다. 따라서 이번 버전은 현재 확인 가능한 공식 한국어 표기를 우선 기준으로 사용합니다.

## 진화 조건 바로보기
디지몬 상태 카드에 `다음 진화 조건` 상자를 추가했습니다.

표시 정보:
- 일반 진화 필요 레벨
- 단계별 필요 훈련합
- ATK/DEF/SPE/HP 우세별 다음 진화 대상
- 특수 진화 조건
- 조그레스 상대 및 필요 레벨/육성 기록
- 추가 진화가 없는 경우 `최종 형태 · 추가 진화 없음`

일반 진화와 조그레스는 v3.96.x의 선택형 구조를 그대로 유지하며, 이 업데이트는 해당 규칙을 바꾸지 않고 조건을 화면에 보여 주는 기능입니다.

## 호환성
- `SAVE_VERSION = 2` 유지
- 디지몬 458종, ID 0~457 유지
- 기존 세이브 구조 변경 없음
- DGI1/DGI2/DGI3 포맷 변경 없음
- 진화 수치/분기 규칙 변경 없음
