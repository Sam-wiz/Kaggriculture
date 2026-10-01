import inco, json, sys, os
from concurrent.futures import ProcessPoolExecutor
from deep4 import SL, _load

def game(job):
    a, b, seed = job
    fa = _load(SL[a]); fb = _load(SL[b])
    b0, b1 = inco.match(fa, fb, seed)
    c0, c1 = inco.match(fb, fa, seed)
    return {'seat0': (b0, b1), 'seat1': (c1, c0)}

pairs = [
 ('pipe16','god'), ('pipe16','mw'), ('pipe16','mr'),
 ('god','v48'), ('god','metav4'), ('mr','v2945'),
 ('mw','metav4'), ('god','mw'), ('mr','mw'),
 ('metav4','v51'),
]
SEEDS = [3001,3002,3003,3004,3005,3006,3007,3008]
jobs = [(a,b,s) for (a,b) in pairs for s in SEEDS]

if __name__ == '__main__':
    out = {}
    with ProcessPoolExecutor(max_workers=12) as ex:
        for job, res in zip(jobs, ex.map(game, jobs)):
            out.setdefault(job[:2], []).append((job[2], res))
    json.dump({f'{a}|{b}|{s}':r for (a,b),lst in out.items() for s,r in lst},
              open('deep5.json','w'))
    for (a,b),lst in out.items():
        diffs = []
        for s,r in lst:
            diffs.append(r['seat0'][0]-r['seat0'][1])
            diffs.append(r['seat1'][0]-r['seat1'][1])
        w = sum(1 for d in diffs if d>0); l = sum(1 for d in diffs if d<0)
        print(f'{a:8s} vs {b:8s} W{w}-L{l} mean {sum(diffs)/len(diffs):+.0f}  n={len(diffs)}', flush=True)
