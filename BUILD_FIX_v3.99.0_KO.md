# TamaPoke v3.99.0 — Digimon Algorithmic Shiny

## 변경 사항
- 통합 `Pet` 디지몬의 Shiny 강제 비활성화를 제거했습니다.
- 디지타마 생성 시 포켓몬과 동일한 Shiny 확률/좋은 이별/반짝부적 보정을 사용합니다.
- 디지몬 버전 선택을 바꿔도 이미 굴린 `eggShiny` 값은 유지되어 재굴림 악용을 막습니다.
- `Pet::makeCurrentShiny()`가 디지몬 ID도 허용하여 샤이니열매를 사용할 수 있습니다.
- DGI1/DGI2/DGI3 RGB565 픽셀을 런타임에서 변환하는 `digiShinyColor565()`를 추가했습니다.
- 검은 외곽선과 밝은 흰색 하이라이트는 유지하고, 유채색은 채널 회전, 회색 중간톤은 종별 warm/cool tint를 사용합니다.
- 홈, 상태 프로필, 진화 완료, 이별/도주, 배틀 렌더링에 동일한 Shiny 팔레트를 적용합니다.
- `digiShinyReg` 도감 비트셋과 NVS `digshy` 키를 추가했습니다.
- 백업/복원 `SAVE_FIELDS`에 `digshy`를 추가했습니다. SAVE_VERSION은 2 유지입니다.
- 디지몬 도감 목록/상세에서 과거 Shiny 육성 기록을 `*`로 표시합니다.
- 레거시 `DigiPet`에도 Shiny 필드/저장을 추가해 잔존 UI가 사용되더라도 색상 상태가 일관되게 동작합니다.

## 호환성
- 기존 v3.98.1 세이브에는 `digshy`가 없으므로 0으로 시작하며 다른 진행 데이터는 그대로 유지됩니다.
- 기존 DGI 파일은 수정할 필요가 없습니다.
- 별도 Shiny 이미지/SD 용량 추가가 필요하지 않습니다.
- Digimon ID 0..457 및 SAVE_VERSION 2는 변경하지 않았습니다.
