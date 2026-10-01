import inco, json, sys, os
from concurrent.futures import ProcessPoolExecutor

SL = {
 'p16': 'rivals/kaggriculture-pipe16-idle-workers/_entry.py',
 'a2802': 'rivals5/2802-two-identical-agents-90-points-apart/_entry.py',
 'melon': 'rivals5/kaggriculture-melon-threshold-squeeze-2749/_entry.py',
 'v2945': 'subJ_2945.py',
}

def _load(path):
    d = os.path.dirname(os.path.abspath(path))
    if d not in sys.path: sys.path.insert(0, d)
    return inco.load_agent(path)

def game(job):
    a, b, seed = job
    fa = _load(SL[a]); fb = _load(SL[b])
    b0, b1 = inco.match(fa, fb, seed)
    c0, c1 = inco.match(fb, fa, seed)
    return {'seat0': (b0, b1), 'seat1': (c1, c0)}

pairs = [
 ('a2802','p16'), ('melon','p16'),
 ('melon','v2945'), ('a2802','v2945'),   # do the anomalies also beat 2945?
 ('melon','a2802'),
]
SEEDS = [6001,6002,6003,6004,6005,6006,6007,6008]
jobs = [(a,b,s) for (a,b) in pairs for s in SEEDS]

if __name__ == '__main__':
    out = {}
    with ProcessPoolExecutor(max_workers=10) as ex:
        for job, res in zip(jobs, ex.map(game, jobs)):
            out.setdefault(job[:2], []).append((job[2], res))
    json.dump({f'{a}|{b}|{s}':r for (a,b),lst in out.items() for s,r in lst},
              open('deep6.json','w'))
    for (a,b),lst in out.items():
        diffs=[]
        for s,r in lst:
            diffs.append(r['seat0'][0]-r['seat0'][1]); diffs.append(r['seat1'][0]-r['seat1'][1])
        w=sum(1 for d in diffs if d>0)
        print(f'{a:8s} vs {b:8s} W{w}-L{len(diffs)-w} mean {sum(diffs)/len(diffs):+.0f}  n={len(diffs)}', flush=True)
