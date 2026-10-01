# screen donor-pool agents vs pipe16 (2 seeds, both seats)
import inco, sys, os, json
from concurrent.futures import ProcessPoolExecutor

P16 = 'rivals/kaggriculture-pipe16-idle-workers/_entry.py'

def _load(path):
    d = os.path.dirname(os.path.abspath(path))
    if d not in sys.path: sys.path.insert(0, d)
    return inco.load_agent(path)

def game(job):
    path, seed = job
    try:
        fa = _load(path); fb = _load(P16)
        b0, b1 = inco.match(fa, fb, seed)
        c0, c1 = inco.match(fb, fa, seed)
        return {'s0': b0 - b1, 's1': c1 - c0}
    except Exception as e:
        return {'err': str(e)[:100]}

if __name__ == '__main__':
    cands = sys.argv[1:]
    seeds = [5001, 5002]
    jobs = [(p, s) for p in cands for s in seeds]
    res = {}
    with ProcessPoolExecutor(max_workers=12) as ex:
        for job, r in zip(jobs, ex.map(game, jobs)):
            res.setdefault(job[0], []).append(r)
    rows = []
    for p in cands:
        rs = res[p]
        if any('err' in r for r in rs):
            print(f'{os.path.basename(p):55s} ERR {next(r["err"] for r in rs if "err" in r)}'); continue
        diffs = [r['s0'] for r in rs] + [r['s1'] for r in rs]
        w = sum(1 for x in diffs if x > 0)
        rows.append((sum(diffs)/len(diffs), p, w, len(diffs)-w))
    for m, p, w, l in sorted(rows, reverse=True):
        print(f'{os.path.basename(p):55s} vs pipe16: W{w}-L{l} {m:+.0f}')
    json.dump(res, open('screen_donors.json','w'))
