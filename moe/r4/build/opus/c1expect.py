"""(1) Elo-expected record of C1's 8 >=2000 live games if C1 = RR-predicted live rating; SPRT-style log-LR of the
RR prediction vs sonnet's p1=0.80. (2) Seed-bootstrap CI of C1's RR-mapped rating (anchors frozen at PREREG fit)."""
import json, math, random
R = 2085
G = [("Clement Lau", 2558, 0), ("Fanch", 2485, 0), ("kazuhiro3381", 2403, 0), ("tamref", 2393, 0),
     ("Juste Me", 2341, 1), ("豆包", 2273, 1), ("hinemos", 2187, 1), ("SatoGo", 2028, 0)]
e = lambda r: 1 / (1 + 10 ** ((r - R) / 400))
for lo, hi in [(2400, 9999), (2200, 2400), (2000, 2200), (2000, 9999)]:
    s = [(e(r), w) for _, r, w in G if lo <= r < hi]
    ll_rr = sum(math.log(p if w else 1 - p) for p, w in s); ll_80 = sum(math.log(.8 if w else .2) for p, w in s)
    print(f"{lo}-{hi}: n={len(s)} obs W={sum(w for _, w in s)} exp W(R={R})={sum(p for p, _ in s):.2f}  "
          f"logLR(RR vs p1=.80)={ll_rr - ll_80:+.2f}")
rows = [json.loads(l) for l in open("moe/r4/build/opus/rr_retro.jsonl")]
anc = dict(shep=113, sirV1=88, hyb=80, f55V2=-92, pipe16=-189); LIVE = dict(shep=2100, hyb=1974, f55V2=1930, sirV1=1897, pipe16=1800)
xs = [anc[k] for k in LIVE]; ys = [LIVE[k] for k in LIVE]; mx, my = sum(xs) / 5, sum(ys) / 5
b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs); a = my - b * mx
bys = {}
for r in rows:
    if "C1" in (r["a"], r["b"]):
        c = r["a"] == "C1"; o = r["b"] if c else r["a"]; d = (r["ra"] - r["rb"]) * (1 if c else -1)
        bys.setdefault(r["seed"], []).append((o, 1. if d > 0 else 0. if d < 0 else .5))
def mle(g): return max(range(-400, 1200, 4), key=lambda E: sum(w * math.log(1 / (1 + 10 ** ((anc[o] - E) / 400))) +
                        (1 - w) * math.log(1 - 1 / (1 + 10 ** ((anc[o] - E) / 400)) + 1e-12) for o, w in g))
random.seed(0); seeds = list(bys); out = []
for _ in range(300):
    g = [x for s in random.choices(seeds, k=len(seeds)) for x in bys[s]]; out.append(a + b * mle(g))
out.sort(); print(f"C1 mapped live: point {a + b * mle([x for s in seeds for x in bys[s]]):.0f}, "
                  f"seed-bootstrap 90% CI [{out[15]:.0f}, {out[284]:.0f}] ({len(seeds)} seeds x 5 anchors x 2 seats)")
