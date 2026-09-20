# TamaPoke v3.95.2 · GitHub Actions workflow mirror hotfix

## 원인
`tools/verify_catalog_push_resilience.py`는 `.github/workflows/main.yml`과 루트의 `GITHUB_WORKFLOW_COPY.txt`가 완전히 동일한지 검사합니다.
v3.95.1에서 새 검증 단계 `verify_dmul_sprite_species_replacements_v3951.py`를 실제 workflow에 추가했지만 mirror 파일에는 같은 한 줄이 반영되지 않아 `AssertionError: workflow mirror drift`가 발생했습니다.

## 수정
- `.github/workflows/main.yml`과 `GITHUB_WORKFLOW_COPY.txt`를 byte-for-byte 동일하게 동기화
- 펌웨어 패치 버전 `3.95.2`로 증가
- 기존 DMUL 종 교체, OmegaX, 돌봄실수 제거, ID 0~457 구조는 변경하지 않음
- 기존 v3.95.1 스프라이트 도구/카탈로그 파일명은 호환성을 위해 유지

## 기대 결과
`python3 tools/verify_catalog_push_resilience.py`가 정상 통과하고 이후 GitHub Actions 검증 단계가 계속 진행됩니다.
