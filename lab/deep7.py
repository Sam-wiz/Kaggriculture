import inco, json, sys, os
from concurrent.futures import ProcessPoolExecutor
from deep4 import SL, _load

SL2 = dict(SL)
SL2['melon'] = 'rivals5/kaggriculture-melon-threshold-squeeze-2749/_entry.py'
SL2['a2802'] = 'rivals5/2802-two-identical-agents-90-points-apart/_entry.py'
SL2['p16'] = SL.pop('p16', None) or 'rivals/kaggriculture-pipe16-idle-workers/_entry.py'

def game(job):
    a, b, seed = job
    fa = _load(SL2[a]); fb = _load(SL2[b])
    b0, b1 = inco.match(fa, fb, seed)
    c0, c1 = inco.match(fb, fa, seed)
    return {'seat0': (b0, b1), 'seat1': (c1, c0)}

pairs = [
 ('melon','metav4'), ('a2802','metav4'),
 ('melon','god'), ('a2802','god'),
 ('melon','v48'), ('a2802','v48'),
 ('melon','v51'),
]
SEEDS = [7001,7002,7003,7004,7005,7006,7007,7008]
jobs = [(a,b,s) for (a,b) in pairs for s in SEEDS]

if __name__ == '__main__':
    out = {}
    with ProcessPoolExecutor(max_workers=10) as ex:
        for job, res in zip(jobs, ex.map(game, jobs)):
            out.setdefault(job[:2], []).append((job[2], res))
    json.dump({f'{a}|{b}|{s}':r for (a,b),lst in out.items() for s,r in lst},
              open('deep7.json','w'))
    for (a,b),lst in out.items():
        diffs=[]
        for s,r in lst:
            diffs.append(r['seat0'][0]-r['seat0'][1]); diffs.append(r['seat1'][0]-r['seat1'][1])
        w=sum(1 for d in diffs if d>0)
        print(f'{a:8s} vs {b:8s} W{w}-L{len(diffs)-w} mean {sum(diffs)/len(diffs):+.0f}  n={len(diffs)}', flush=True)
