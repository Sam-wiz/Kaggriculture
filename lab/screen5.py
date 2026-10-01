# screen rivals5 new extractions vs pipe16 (2 seeds, both seats)
import inco, sys, os, json
from concurrent.futures import ProcessPoolExecutor

P16 = 'rivals/kaggriculture-pipe16-idle-workers/_entry.py'
CANDS = [(d, f'rivals5/{d}/main.py') for d in sys.argv[1:]]

def _load(path):
    d = os.path.dirname(os.path.abspath(path))
    if d not in sys.path: sys.path.insert(0, d)
    return inco.load_agent(path)

def game(job):
    path, seed = job
    try:
        fa = _load(path); fb = _load(P16)
        b0, b1 = inco.match(fa, fb, seed)   # cand seat 0
        c0, c1 = inco.match(fb, fa, seed)   # cand seat 1
        return {'s0': b0 - b1, 's1': c1 - c0}
    except Exception as e:
        return {'err': str(e)[:80]}

if __name__ == '__main__':
    seeds = [5001, 5002]
    jobs = [(p, s) for _, p in CANDS for s in seeds]
    res = {}
    with ProcessPoolExecutor(max_workers=12) as ex:
        for job, r in zip(jobs, ex.map(game, jobs)):
            res.setdefault(job[0], []).append(r)
    rows = []
    for d, p in CANDS:
        rs = res[p]
        if any('err' in r for r in rs):
            print(f'{d:55s} ERR {rs[0].get("err","")}'); continue
        diffs = [r['s0'] for r in rs] + [r['s1'] for r in rs]
        w = sum(1 for x in diffs if x > 0); l = len(diffs) - w
        rows.append((sum(diffs)/len(diffs), d, w, l))
    for m, d, w, l in sorted(rows, reverse=True):
        print(f'{d:55s} vs pipe16: W{w}-L{l} {m:+.0f}')
    json.dump({d: res[p] for d, p in CANDS}, open('screen5.json', 'w'))
