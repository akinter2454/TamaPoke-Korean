# TamaPoke v3.92.0 - Digimon Capacity Expansion

## 변경
- `DIGI_SPECIES_CAP`: 352 -> **2048**
- 현재 로스터: 333종
- 즉시 남는 여유: **1,715종**
- Creature ID 범위는 2000 + index를 유지하며 2048 CAP에서도 int16 범위 안입니다.

## 세이브 호환성
CAP이 커져도 저장할 때는 배열 전체 2048칸을 쓰지 않습니다.
현재 실제 로스터 길이(`DIGI_SPECIES_COUNT`)만 저장합니다.

현재 333종 기준:
- `digbest`: 333 bytes
- `digreg`: 42 bytes

기존 352 CAP 저장본은 prefix-safe 로딩으로 앞부분을 그대로 복원하고, 새로 생긴 뒤쪽 영역은 0으로 유지합니다.
`SAVE_VERSION`은 2를 유지합니다.

## 미래 확장
- 최대 2048종까지 CAP 재수정 없이 추가 가능
- 한 버전/스테이지에 255종을 넘겨도 starter counting이 넘치지 않도록 `countOf`/`pick`을 uint16_t로 확장
- DGI3 포맷, 현재 ID, 진화/세이브 인덱스는 변경하지 않음

## 버전
과거 폐기된 v3.91.0 DGI4 실험본과 혼동하지 않도록 다음 minor 번호인 **v3.92.0**을 사용합니다.
