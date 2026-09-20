#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
main = root / 'TamaPoke.ino'
fallback = root / 'firmware_source' / 'TamaPoke.ino'
workflow = (root / '.github/workflows/main.yml').read_text(encoding='utf-8')
mirror = (root / 'GITHUB_WORKFLOW_COPY.txt')

assert main.is_file() and main.stat().st_size > 0, 'root TamaPoke.ino missing'
assert fallback.is_file() and fallback.stat().st_size > 0, 'firmware fallback missing'
assert main.read_bytes() == fallback.read_bytes(), 'firmware fallback drift'
assert 'Resolve canonical firmware sketch' in workflow, 'firmware resolver step missing'
assert 'firmware_source/TamaPoke.ino' in workflow, 'fallback path missing from workflow'
assert '#define FW_VERSION "3.96.1"' in main.read_text(encoding='utf-8'), 'FW_VERSION mismatch'
assert mirror.is_file(), 'workflow mirror missing'
assert (root/'.github/workflows/main.yml').read_bytes() == mirror.read_bytes(), 'workflow mirror drift'
print('firmware source fallback v3.96.1 OK')
