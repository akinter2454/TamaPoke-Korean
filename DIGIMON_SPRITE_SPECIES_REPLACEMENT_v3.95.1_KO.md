# TamaPoke v3.95.1 · DMUL 스프라이트 호환 종 교체

48×48 DMUL 스프라이트를 확보할 수 없는 종을 카탈로그 ID를 유지한 채 교체했습니다.

- ID 360: Belphemon: Sleep Mode → Lilithmon (리리스몬)
- ID 393: Shamamon → Gazimon (가지몬)
- ID 410: Luxmon → Patamon (파닥몬)

## 적용 원칙
- 기존 ID 0~457과 총 458종 구조 유지
- 저장 데이터 배열 크기와 SAVE_VERSION 유지
- 기존 진화 분기 위치는 그대로 두고 종 이름/타입/스프라이트 대상만 교체
- 돌봄 실수 진화 조건은 다시 추가하지 않음
- ID 393 Gazimon과 ID 410 Patamon은 기존 DMC 쪽 동명 종과 별도 DMUL 슬롯으로 유지하며, DMUL 진화 탐색은 버전 우선 조회를 사용

## 새 DMUL 분기
- Pokomon → Renamon / Impmon / Gazimon / Goblimon
- Gazimon → Fugamon / Musyamon / Sorcermon / BlackTailmon
- Koromon 균형 분기 → Patamon
- Patamon → Gladimon / Reppamon / Pidmon / Darcmon
- Dark 완전체 분기에서 기존 Belphemon: Sleep Mode 자리는 Lilithmon으로 대체

## 타입
- Lilithmon: DARK / FAIRY
- Gazimon: DARK / NORMAL
- Patamon: FLYING / FAIRY
