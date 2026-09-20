#!/usr/bin/env python3
"""Static guard for the standalone DMUL required-sprite downloader."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
p=root/'tools/DMC-DMUL-Required-Sprite-Downloader.html'
s=p.read_text(encoding='utf-8')
rows=re.findall(r"\[(\d+),'([^']+)',(\d+),(\d+),'(dragon|dark|deep|nature|nightmare|secret)'",s)
assert len(rows)==50, len(rows)
ids=[int(x[0]) for x in rows]
assert len(set(ids))==50
assert set(range(283,333))==set(ids)
assert "Source=DMUL" in s
assert 'raw.githubusercontent.com/tero0x/dmc-sprites/main/sprites.json' in s
assert 'cdn.jsdelivr.net/gh/tero0x/dmc-sprites@main/sprites.json' in s
assert "TamaPoke-DMUL-required-sprites.zip" in s
assert 'function makeZip' in s and 'function assetUrls' in s and 'function matchReq' in s
for name in ['Dodomon','Guilmon','Dukemon Crimson Mode','Diablomon','Dianamon','MirageGaogamon','Sakuyamon','Jesmon','DORUgoramon','Alphamon Ouryuken']:
    assert name in s, name
print('DMUL sprite downloader OK: 50 required IDs, Source=DMUL filter, online/local data fallback, ZIP output')
