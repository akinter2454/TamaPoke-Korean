# TamaPoke v3.90.0 DMUL DB 호환 로스터 업데이트

DMC Sprite Database에서 이미지셋을 찾지 못하던 3개 슬롯을 DB 친화적인 대체 로스터로 교체했습니다.

| 기존 슬롯 | v3.90.0 대체 | ID | 단계 | 진행 구조 |
|---|---|---:|---|---|
| Chrysalimon | Kurisarimon | 289 | 성숙기 | Keramon → Kurisarimon → Infermon |
| Chibimon | Gigimon | 322 | 유년기 II | Dodomon → Dorimon/Gigimon, Gigimon → Guilmon |
| PetiMeramon | Pokomon | 330 | 유년기 II | Mokumon → Pokomon, 기존 ATK/DEF/SPE/HP 분기 결과 유지 |

## 저장 데이터 호환
세 슬롯의 인덱스(ID)는 289/322/330 그대로 유지합니다. 기존 세이브의 종 ID를 이동하지 않고 해당 슬롯의 종/스프라이트 키만 교체하므로 SAVE_VERSION은 2를 유지합니다.

## 스프라이트 도구
GitHub 프로젝트 안의 필수 SD 팩 생성기/검증기 카탈로그도 새 이름으로 동기화했습니다. 과거 이름과 일부 영문 더빙명은 입력 별칭으로 남겨 기존 스프라이트 파일을 변환할 때도 인식합니다.
