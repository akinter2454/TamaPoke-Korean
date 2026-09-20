TamaPoke v3.90.7 Deploy/Installer Embed Fix

이번 패치는 v3.90.6의 게임 동작을 변경하지 않습니다.

원인:
- v3.90.4에서 OneClick Installer의 EMBEDDED_FIRMWARE placeholder를
  여러 줄 객체에서 한 줄 JSON 객체로 바꿨습니다.
- 기존 embed_tamapoke_firmware.py 정규식은 여러 줄 형태의 마지막 `\n};`를
  전제로 했기 때문에, 한 줄 EMBEDDED_FIRMWARE에서 시작해 뒤의
  EMBEDDED_SPRITE_PAKS와 OFFSETS까지 잘못 삼켜 버렸습니다.
- 그 결과 다음 치환 단계에서 `EMBEDDED_SPRITE_PAKS block not found`로 실패했습니다.

v3.90.7 수정:
1. OneClick Installer의 EMBEDDED_FIRMWARE를 v3.90.0 정상 deploy 템플릿의
   여러 줄 구조로 정확히 복원.
2. embed_tamapoke_firmware.py 정규식을 한 줄/여러 줄 양쪽 모두 지원하도록 보강.
3. verify_sd_serial_protocol.py에서 두 임베드 블록의 존재를 사전 검증.
4. 실제 더미 bootloader/partitions/boot_app0/app.bin으로 embed 스크립트를 실행해
   index.html 생성 성공까지 검증.

게임 동작:
- v3.90.6과 동일
- SAVE_VERSION 2 유지
- DGI1/DGI2/DGI3 유지
- DGI4 사용 안 함
