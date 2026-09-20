# TamaPoke v3.90.4 build fix

기준: v3.90.3 Sick/Hurt 동작 패치

## 수정
- `TamaPoke.ino`: FW_VERSION 3.90.4
- `TamaPoke-KO-OneClick-Installer.html`: `3.90.4-ko-dgi3-sick-hurt-motion`
- 버전 고정 검증 스크립트: 3.90.4로 동기화

## 원인
v3.90.3 패키지의 설치기 버전 마커가 `3.90.1-ko-dgi3-pokemon-motion`에 남아 있어 `verify_sd_serial_protocol.py`의 소스/설치기 버전 일치 검사가 실패했습니다.

게임 동작, DGI 포맷, SAVE_VERSION에는 추가 변경이 없습니다.
