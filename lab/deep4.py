# deep validation: rivals4 leaders vs live pair, 8 seeds both seats, paired margins
import inco, json
from concurrent.futures import ProcessPoolExecutor

SL = {
 'v51':'rivals/kaggriculture-v51-lean-flock/main.py',
 'pipe16':'rivals/kaggriculture-pipe16-idle-workers/main.py',
 'metav4':'rivals/the-metav4-farm-submission-v13/main.py',
 'mev4':'rivals/kaggriculture-master-engine-v4/main.py',
 'v50':'rivals/kaggriculture-v50-early-yarn-commit/main.py',
 'mr':'rivals/kaggriculture-market-rhythm-sale-policy/main.py',
 'mw':'rivals/kaggriculture-more-wheat-smarter-sales/main.py',
 'god':'rivals/god-s-mode-hacked-stores/main.py',
 'v2945':'subJ_2945.py',
 'v48':'subH2_v48.py',
}

def _load(path):
    import sys, os
    d = os.path.dirname(os.path.abspath(path))
    if d not in sys.path:
        sys.path.insert(0, d)
    return inco.load_agent(path)

def game(job):
    a, b, seed = job
    fa = _load(SL[a]); fb = _load(SL[b])
    b0, b1 = inco.match(fa, fb, seed)   # a in seat 0
    c0, c1 = inco.match(fb, fa, seed)   # a in seat 1
    return {'seat0': (b0, b1), 'seat1': (c1, c0)}  # (a_bank, b_bank) per seat

pairs = [
 ('v51','v2945'), ('pipe16','v2945'), ('metav4','v2945'),
 ('v51','v48'), ('pipe16','v48'), ('metav4','v48'),
 ('v51','pipe16'), ('v51','metav4'), ('pipe16','metav4'),
 ('mw','v2945'), ('mw','v48'), ('god','v2945'),
 ('mev4','v2945'), ('v50','v2945'), ('mr','v48'),
]
SEEDS = [2001,2002,2003,2004,2005,2006,2007,2008]
jobs = [(a,b,s) for (a,b) in pairs for s in SEEDS]

if __name__ == '__main__':
    out = {}
    with ProcessPoolExecutor(max_workers=12) as ex:
        for job, res in zip(jobs, ex.map(game, jobs)):
            out.setdefault(job[:2], []).append((job[2], res))
    json.dump({f'{a}|{b}|{s}':r for (a,b),lst in out.items() for s,r in lst},
              open('deep4.json','w'))
    for (a,b),lst in out.items():
        diffs = []
        for s,r in lst:
            diffs.append(r['seat0'][0]-r['seat0'][1])
            diffs.append(r['seat1'][0]-r['seat1'][1])
        w = sum(1 for d in diffs if d>0); l = sum(1 for d in diffs if d<0)
        print(f'{a:8s} vs {b:8s} W{w}-L{l} mean {sum(diffs)/len(diffs):+.0f}  n={len(diffs)}', flush=True)
