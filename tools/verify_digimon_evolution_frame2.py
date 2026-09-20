from pathlib import Path
root=Path(__file__).resolve().parents[1]
s=(root/'TamaPoke.ino').read_text(encoding='utf-8')
assert '#define FW_VERSION "3.96.0"' in s
assert 'return drawDigiFrameCentered(spriteId,2,CX,PET_GROUND,0,false,silhouette);' in s
assert 'digiWasEvolving=true;' in s
assert 'digiEvolveCelebrateUntil=now+1800;' in s
assert 'digiMotionFrame(DIGI_MOTION_POSE,now)' in s
assert '#define SAVE_VERSION 2' in (root/'save.h').read_text(encoding='utf-8')
assert '"DGI4"' not in s
print('Digimon evolution frame-2 transform + Pose completion OK')
