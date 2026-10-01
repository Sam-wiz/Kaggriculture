# Scan full Kaggle replays for per-seat overage consumption (remainingOverageTime trajectory).
# Evidence for whether top agents compute >1 s on any step (runtime planning) on Kaggle hardware.
import json, glob, sys, os
rows = []
for f in sorted(glob.glob(sys.argv[1] + '/*.json'))[:int(sys.argv[2]) if len(sys.argv) > 2 else 10**9]:
    try:
        d = json.load(open(f))
    except Exception as e:
        continue
    steps = d.get('steps') or []
    names = [a.get('Name') if isinstance(a, dict) else a for a in (d.get('info', {}).get('TeamNames') or [])]
    for seat in range(2):
        tr = []
        for t, s in enumerate(steps):
            o = s[seat].get('observation', {})
            if 'remainingOverageTime' in o:
                tr.append((t, o['remainingOverageTime']))
        if not tr:
            continue
        start = tr[0][1]
        drops = [(t, round(prev - v, 3)) for (tp, prev), (t, v) in zip(tr, tr[1:]) if prev - v > 1e-6]
        rows.append(dict(f=os.path.basename(f), seat=seat, team=names[seat] if seat < len(names) else None,
                         start=start, end=tr[-1][1], used=round(start - tr[-1][1], 3), ndrop=len(drops),
                         top_drops=sorted(drops, key=lambda x: -x[1])[:5],
                         status=steps[-1][seat].get('status')))
for r in rows:
    print(json.dumps(r))
