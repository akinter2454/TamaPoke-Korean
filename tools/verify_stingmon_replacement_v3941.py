from pathlib import Path
import re, json
R=Path(__file__).resolve().parents[1]
cpp=(R/'digimon.cpp').read_text(encoding='utf-8')
ino=(R/'TamaPoke.ino').read_text(encoding='utf-8')
types=json.loads((R/'data/digimon/types.json').read_text(encoding='utf-8'))
assert '#define FW_VERSION "3.96.1"' in ino
rows=[m.groups() for m in re.finditer(r'D\("([^"]+)",(\d+),(\d+),(\d+),(\d+)\)',cpp)]
assert len(rows)==458
assert rows[442][0]=='Snimon' and rows[442][1]=='22' and rows[442][2]=='3'
assert all(name!='Stingmon' for name, *_ in rows)
assert 'if(!strcmp(n,"Wormmon"))return set4("Snimon"' in cpp
assert 'if(!strcmp(n,"Snimon"))return set4("JewelBeemon"' in cpp
assert 'if(!strcmp(n,"ExVeemon")&&q("Snimon",25))return target("Paildramon")' in cpp
assert 'if(!strcmp(n,"Snimon")&&q("ExVeemon",25))return target("Dinobeemon")' in cpp
assert types['entries'][442]['name']=='Snimon'
assert types['entries'][442]['type1']=='BUG' and types['entries'][442]['type2']=='FIGHTING'
assert '스나이몬' in cpp and '스팅몬' not in cpp
print('v3.96.1 Stingmon replacement invariant OK: ID442 Snimon, routes/jogress/types aligned')
