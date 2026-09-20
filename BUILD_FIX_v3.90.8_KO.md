# TamaPoke v3.90.8 - Generated Catalog Push Resilience

## 사용자 로그
`Commit generated catalog lock source`에서:

- `[rejected] HEAD -> main (non-fast-forward)`
- `failed to push some refs`

## 원인
Actions가 긴 빌드/카탈로그 생성 작업을 수행하는 동안 원격 `main`이 먼저 앞으로 이동했습니다.
생성 카탈로그 lock/source 커밋은 편의용 자동 커밋인데, 기존 workflow는 이 push 실패를
전체 배포 실패로 처리했습니다.

## v3.90.8 수정
- 자동 생성 카탈로그 커밋 단계를 `best effort`로 변경.
- push 전에 `origin/main`을 fetch하고, 실행 시작 SHA보다 원격이 앞서 있으면 자동 커밋을 건너뜀.
- fetch와 push 사이의 경쟁 조건으로 push가 다시 거부되어도 경고만 출력.
- 이 단계에 `continue-on-error: true` 적용.
- GitHub Pages 생성/업로드/배포는 계속 진행.
- `GITHUB_WORKFLOW_COPY.txt`를 `main.yml`과 바이트 단위로 동기화.
- `verify_catalog_push_resilience.py` 추가.

## 게임
v3.90.7과 동작 동일.
SAVE_VERSION 2, DGI1/DGI2/DGI3 유지.
