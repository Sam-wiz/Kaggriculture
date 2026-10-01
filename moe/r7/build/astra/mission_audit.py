import json
from collections import defaultdict, Counter
from pathlib import Path
src = Path('moe/r7/build/opus/bc2s_DSM.jsonl')
units = defaultdict(list)
with src.open() as f:
    for line in f:
        r = json.loads(line)
        units[r['ep'], r['ui']].append((r['t'], r['G']['day'], r['y'], r['y2']))
moves = {'NORTH', 'SOUTH', 'EAST', 'WEST'}
def eligible(r):
    return r[2] in moves and r[3] not in {None, 'PASS', 'ABSENT'} | moves
eps = sorted({ep for (ep, ui), rs in units.items() if any(map(eligible, rs))})
te = set(eps[-10:])
counts = {'all': Counter(), 'last10': Counter()}
for (ep, ui), rs in units.items():
    rs.sort()
    prev = None
    for r in rs:
        if eligible(r):
            for name in (['all', 'last10'] if ep in te else ['all']):
                c = counts[name]
                c['travel_rows'] += 1
                c['copy_previous_y2_correct'] += bool(prev and prev[3] == r[3])
                c['MOVE_IDLE_target'] += r[3] == 'MOVE_IDLE'
                c['prior_row_other_day'] += bool(prev and prev[1] != r[1])
                if prev and prev[0] == r[0]-1 and prev[1] == r[1] and prev[2] in moves:
                    c['adjacent_same_day_move_prefix'] += 1
                    c['prefix_same_y2'] += prev[3] == r[3]
        prev = r
out = {'source':str(src), 'episode_count':len(eps), 'evaluation_episodes':sorted(te), 'counts':counts,
       'note':'Descriptive audit, reused F-test split, not fresh validation; no model fit or simulations.'}
Path('moe/r7/build/astra/mission_audit.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
