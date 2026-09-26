TamaPoke 한국어판 v3.99.1

이번 버전은 v3.99.0의 GitHub Actions 실제 ESP32-S3 컴파일 오류를 수정한 안정성 패치입니다.

핵심 변경
- 원형 화면 텍스트 경계 보정에서 사용하는 CX/CY를 UI helper보다 먼저 선언하도록 수정했습니다.
- v3.99.0에서는 uiRoundTextWidth()/uiDrawCenteredFit()가 CX/CY보다 먼저 컴파일되어 Actions에서 'CX was not declared in this scope' 오류가 발생할 수 있었습니다.
- CX뿐 아니라 uiRoundTextWidth()가 사용하는 CY도 함께 선언 순서를 바로잡았습니다.
- tools/verify_ui_geometry_declaration_order_v3991.py를 추가해 같은 전처리/선언 순서 오류가 재발하지 않도록 했습니다.
- 디지몬 Shiny, 5개 키우기 슬롯, 배틀 이름 수정, UTF-8 말줄임/원형 화면 경계 기능은 그대로 유지됩니다.
- SAVE_VERSION은 2로 유지됩니다.

대상 하드웨어:
- Waveshare ESP32-S3-Touch-AMOLED-1.75
- 466x466 CO5300 QSPI AMOLED
- CST9217 Touch

개발을 이어갈 때는 `TamaPoke-v3.99.1-HANDOFF.md`를 기준으로 사용하세요.
