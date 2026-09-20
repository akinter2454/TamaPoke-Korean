# TamaPoke v3.90.6 workflow-copy sync fix

## 원인
`verify_training_rewards.py`는 `.github/workflows/main.yml`과 `GITHUB_WORKFLOW_COPY.txt`가 완전히 동일한지 확인합니다.
v3.90.5에서 `verify_digimon_behavior_declaration_order.py`를 main.yml에 추가했지만 workflow copy를 함께 갱신하지 않아 Actions가 중단되었습니다.

## 수정
- `GITHUB_WORKFLOW_COPY.txt`를 현재 `.github/workflows/main.yml`과 바이트 단위로 동기화
- FW_VERSION 3.90.6
- Installer marker 3.90.6-ko-dgi3-sick-hurt-motion
- 버전 고정 회귀검사 3.90.6으로 동기화

## 동작 변경
없음. v3.90.5의 DGI3 동작 규칙과 Sick/Hurt/Attack/Pose 설정을 그대로 유지합니다.
