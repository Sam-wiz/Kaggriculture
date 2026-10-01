"""Summarise subst.py output: paired WR / margin per arm, sign test, implied Elo vs opponent R."""
import json, math, sys, statistics as st

rows = [json.loads(l) for l in open(sys.argv[1])]
arms = [a for a in sys.argv[2].split(",")]
w = lambda m: 1.0 if m > 0 else 0.5 if m == 0 else 0.0


def elo(scores, R):
    lo, hi = 0.0, 4000.0
    for _ in range(60):
        r = (lo + hi) / 2
        g = sum(s - 1 / (1 + 10 ** ((q - r) / 400)) for s, q in zip(scores, R))
        lo, hi = (r, hi) if g > 0 else (lo, r)
    return r


def boot(scores, R, n=400):
    import random
    rnd = random.Random(7); out = []
    for _ in range(n):
        ix = [rnd.randrange(len(scores)) for _ in scores]
        out.append(elo([scores[i] for i in ix], [R[i] for i in ix]))
    out.sort(); return out[int(.05 * n)], out[int(.95 * n)]


ok = [r for r in rows if all(r.get(a + "_shopok", True) for a in arms if a != "recorded")]
print(f"episodes {len(rows)}  shop-aligned {len(ok)}")
R = [r["R"] for r in ok]
for a in arms:
    s = [w(r[a]) for r in ok]
    lo, hi = boot(s, R)
    print(f"{a:10s} WR {st.mean(s):.3f}  mean margin {st.mean(r[a] for r in ok):+7.0f}  "
          f"median {st.median(r[a] for r in ok):+6.0f}  implied Elo {elo(s, R):6.0f} (90% {lo:.0f}-{hi:.0f})"
          + (f"  opp bank drift {st.mean(r[a + '_opp'] for r in ok):+6.0f}" if a != "recorded" else ""))
for i, a in enumerate(arms):
    for b in arms[i + 1:]:
        d = [r[a] - r[b] for r in ok]
        up = sum(1 for r in ok if w(r[a]) > w(r[b])); dn = sum(1 for r in ok if w(r[a]) < w(r[b]))
        n = up + dn
        z = (up - dn) / math.sqrt(n) if n else 0
        print(f"{a} - {b}: mean d {st.mean(d):+6.0f}  sd {st.pstdev(d):5.0f}  outcome flips +{up}/-{dn}  z {z:+.2f}")
