# TamaPoke 디지몬 진화·SD 도트 정책

## 공용 육성과 독립 도감
포켓몬과 디지몬은 Pet/파티/박스/배틀 육성 자리를 공유하지만 도감과 진화 데이터는 분리합니다. 디지몬 내부 ID는 2000+ 영역을 사용합니다.

## DMC/Pendulum
DMC Ver.1~5와 Pendulum P0~P5의 기존 진화/조그레스 구조를 유지합니다.

## DMUL DigiTama
DMUL Source 도트는 한 알로 무작위 합치지 않고 기존 기기 선택 방식처럼 6개 DigiTama로 분리합니다.
- DMUL Dragon: Dodomon → Dorimon/Gigimon → DORUmon·Ryudamon·Guilmon 계열
- DMUL Dark: Kuramon → Tsumemon → Keramon 계열
- DMUL Deep: Pitchmon → Moonmon → Lunamon 계열
- DMUL Nature: Bubbmon → Mochimon → Gaomon 계열
- DMUL Nightmare: Mokumon → Pokomon → Renamon 계열
- DMUL Secret: Botamon → Koromon → Hackmon(훈련 조건) / 기존 Agumon

DMUL Route 조건은 TamaPoke의 현재 육성 구조에 맞춰 **훈련치 중심**으로 결정합니다.
- 일반 분기: ATK / DEF / SPE / HP 중 가장 높은 훈련치가 A-D 분기를 결정합니다.
- 동률이면 해당 종의 기본 style을 우선하고, 이후 ATK→DEF→SPE→HP 순서로 결정합니다.
- 일부 성장기 확보용 특수 분기는 균형 훈련 또는 특정 훈련 조합으로 해금합니다.
- **돌봄 실수는 디지몬의 진화 분기, 특수진화, 조그레스 조건에 사용하지 않습니다.**
- 돌봄 실수 수치는 기존 세이브 호환과 다른 게임 시스템을 위해 저장되지만 DMUL/DMC/Pendulum 디지몬 진화 판정에는 영향을 주지 않습니다.

알파몬 + 오류우몬은 알파몬 왕룡검 조그레스를 유지하고, 듀크몬은 조건을 충족하면 크림슨 모드로 추가 진화합니다.

## GitHub와 SD카드 분리
GitHub에는 펌웨어, 도감/진화 데이터, 변환기만 둡니다. 원본 DMUL/DMC/Pendulum PNG와 생성된 .dgi는 저장소에 포함하지 않습니다.

1. tools/Digimon-SD-Pack-Maker.html을 브라우저에서 엽니다.
2. 캐릭터별 ZIP 또는 바깥 묶음 ZIP을 선택합니다.
3. 결과 ZIP의 digimon 폴더를 SD 카드 최상위에 복사합니다.
4. 포켓몬 /mons 폴더는 수정하지 않습니다.
