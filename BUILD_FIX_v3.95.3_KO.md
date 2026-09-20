# TamaPoke v3.95.3 GitHub Actions firmware-source hotfix

## 문제
GitHub Actions의 `Sync current PMDCollab Pokemon and canonical official forms` 단계가 저장소 루트의 `TamaPoke.ino`를 직접 참조하고 있어, 파일이 누락되거나 하위 폴더에 들어간 경우 `sed: can't read .../TamaPoke.ino`로 즉시 종료될 수 있었습니다.

## 수정
- checkout 직후 `Resolve canonical firmware sketch` 단계를 추가했습니다.
- 루트 `TamaPoke.ino`가 없으면 `firmware_source/TamaPoke.ino` 백업을 자동 복구합니다.
- 백업도 없으면 저장소 안의 다른 `TamaPoke.ino`를 탐색해 루트로 복사합니다.
- 그래도 찾지 못하면 어떤 파일이 필요한지 명확한 오류 메시지를 출력합니다.
- 루트 원본과 `firmware_source/TamaPoke.ino`가 byte-for-byte 동일한지 검증하는 테스트를 추가했습니다.
- workflow mirror (`.github/workflows/main.yml` / `GITHUB_WORKFLOW_COPY.txt`) 동기화를 유지합니다.

## 호환성
- Digimon ID 0~457 및 458종 카탈로그 유지
- v3.95.1의 Lilithmon / Gazimon / Patamon 교체 유지
- Imperialdramon OmegaX 유지
- 돌봄 실수 진화 미사용 정책 유지
- 세이브 포맷 변경 없음
