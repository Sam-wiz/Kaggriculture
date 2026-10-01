"""Tree-router feasibility: exact-replay each team game (both recorded tapes, kagsim), record the team seat's farm
signature at dawns 6/9/12/15 (steps 144/216/288/360, obs before the reply). For games sharing shops[:k], measure
tile-signature distance between their dawn states: a splice at dawn d onto a tape whose recorded state is within a
few tiles of ours is (nearly) state-safe.
usage: statecompat.py INDEX.json OUT.json"""
import json, gzip, os, sys, collections, itertools, statistics as S
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r4/build/opusb"); sys.path.insert(0, ROOT + "/kaggriculture-cppsim")
from t1 import tape, farmsig
import kagsim
recs = json.load(open(sys.argv[1])); out = sys.argv[2]
DAWNS = (144, 216, 288, 360)
dec = {}
for fn in ('moe/r4/build/opus/dec_top.jsonl', 'moe/r4/build/opus/dec_top10.jsonl'):
    for l in open(fn):
        r = json.loads(l)
        if r.get('ep') in {x['ep'] for x in recs}: dec[r['ep']] = r
res = []
for x in recs:
    d = json.load(gzip.open(x['p'], 'rt')); A = d['actions']; k = x['s']
    g = kagsim.Game(seed=int(d['seed'])); sig = {}
    T0, T1 = tape(A, 0), tape(A, 1)
    for t in range(max(DAWNS) + 1):
        o0, o1 = g.observe(0), g.observe(1)
        if t in DAWNS: sig[t] = farmsig((o0 if k == 0 else o1)['farms'][k])
        g.step(T0(o0), T1(o1))
    res.append(dict(ep=x['ep'], s=k, shops=dec[x['ep']]['shops'], bank=x['bank'], sig=sig))
json.dump(res, open(out, 'w'))
def dist(a, b): return sum(p != q for p, q in zip(a, b))
for t, kk in ((144, 0), (216, 2), (288, 3), (360, 4)):
    grp = collections.defaultdict(list)
    for r in res: grp[tuple(r['shops'][:kk])].append(r)
    ds = [dist(a['sig'][str(t)] if str(t) in a['sig'] else a['sig'][t], b['sig'][str(t)] if str(t) in b['sig'] else b['sig'][t]) for v in grp.values() for a, b in itertools.combinations(v, 2)]
    if ds:
        print(f"dawn step {t} (games sharing first {kk} shops): pairs {len(ds)} dist median {S.median(ds)} | <=2: {sum(d<=2 for d in ds)/len(ds):.2f} <=5: {sum(d<=5 for d in ds)/len(ds):.2f} | groups {len(grp)} mean size {len(res)/len(grp):.1f}")
