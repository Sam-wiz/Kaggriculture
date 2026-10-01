"""Summarize TOP-SUB cells: per arm, shop-aligned only (and all).
shortfall = candidate bank - recorded bank of the top team it replaced (same seed, same opponent tape)
breakage  = opponent tape's replayed bank - its recorded bank (how much the frozen tape moved)
usage: subsum.py SUB.jsonl[,SUB2.jsonl] [LB.json]
"""
import json, sys, statistics as S, collections, math
rows = []
for fn in sys.argv[1].split(","):
    rows += [json.loads(l) for l in open(fn)]
lb = json.load(open(sys.argv[2] if len(sys.argv) > 2 else "moe/r3/lb_0926_0500.json"))
arms = collections.defaultdict(list)
for r in rows:
    if "err" in r: continue
    arms[r["name"]].append(r)


def mle_rating(cells):
    """Elo MLE of the candidate from W/L vs opponents of known LB rating (ties = half)."""
    obs = [(lb.get(c["opp_team"]), 1.0 if c["me"] > c["opp"] else (0.5 if c["me"] == c["opp"] else 0.0)) for c in cells]
    obs = [(R, y) for R, y in obs if R]
    if not obs: return None
    best = None
    for R in range(1000, 3600, 5):
        ll = 0
        for Ro, y in obs:
            p = 1 / (1 + 10 ** ((Ro - R) / 400)); p = min(max(p, 1e-9), 1 - 1e-9)
            ll += y * math.log(p) + (1 - y) * math.log(1 - p)
        if best is None or ll > best[0]: best = (ll, R)
    return best[1]


print(f"{'arm':8} {'n':>4} {'aln':>4} {'WR':>5} {'margin':>8} {'shortfall':>10} {'brk':>7} {'|brk|':>7} {'R_mle':>6}   (shop-aligned cells)")
for a, cs in sorted(arms.items()):
    al = [c for c in cs if c["shops_ok"]]
    if not al: print(a, len(cs), 0); continue
    wr = sum(1 for c in al if c["me"] > c["opp"]) / len(al)
    mg = S.mean(c["me"] - c["opp"] for c in al)
    sf = S.mean(c["me"] - c["rec_me"] for c in al)
    br = S.mean(c["opp"] - c["rec_opp"] for c in al)
    abr = S.median(abs(c["opp"] - c["rec_opp"]) for c in al)
    print(f"{a:8} {len(cs):4d} {len(al):4d} {wr:5.2f} {mg:+8.0f} {sf:+10.0f} {br:+7.0f} {abr:7.0f} {mle_rating(al) or 0:6d}")
# recorded baseline: the replaced top team's own result in the same aligned cells
al = [c for c in arms[next(iter(arms))] if c["shops_ok"]] if arms else []
if al:
    wr = sum(1 for c in al if c["rec_me"] > c["rec_opp"]) / len(al)
    print(f"{'recorded':8} {len(al):4d}      {wr:5.2f} {S.mean(c['rec_me']-c['rec_opp'] for c in al):+8.0f}   (replaced top team, same cells as first arm)")
