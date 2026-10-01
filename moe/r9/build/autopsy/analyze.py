"""Autopsy analysis: per-episode margin, opponent LB rating, clone-identity,
market-order stats. Reads replays/*.json.gz + leaderboard csv."""
import gzip, json, os, csv, glob, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
LB = glob.glob(os.path.join(HERE, "kaggriculture-publicleaderboard-*.csv"))[0]
OUR = "Sam-wiz"

lb = {}
with open(LB, encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        lb[row["TeamName"]] = (int(row["Rank"]), float(row["Score"]))


def unit_ops(act):
    """set of (op,) tuples for farmer+hands — position-independent signature."""
    if not isinstance(act, dict):
        return Counter()
    c = Counter()
    f = act.get("farmer")
    if f:
        c[f[0] if isinstance(f, list) else f] += 1
    for h in act.get("hands") or []:
        if h:
            c["H:" + (h[0] if isinstance(h, list) else str(h))] += 1
    return c


def market_orders(act):
    if not isinstance(act, dict):
        return []
    return act.get("market") or []


rows = []
for path in sorted(glob.glob(os.path.join(HERE, "replays/*.json.gz"))):
    rec = json.load(gzip.open(path))
    teams = rec.get("teams") or []
    if OUR not in teams or len(teams) != 2:
        continue
    us = teams.index(OUR)
    them = 1 - us
    opp = teams[them]
    rw = rec.get("rewards") or [None, None]
    if rw[us] is None:
        continue
    margin = rw[us] - rw[them]
    acts = rec.get("actions") or []
    n = len(acts)
    ident = 0
    both = 0
    our_sell = Counter()
    opp_sell = Counter()
    our_ord = opp_ord = 0
    opp_first_sell = our_first_sell = None
    for t, pair in enumerate(acts):
        a_us, a_th = pair[us], pair[them]
        u_us, u_th = unit_ops(a_us), unit_ops(a_th)
        both += 1
        if u_us == u_th:
            ident += 1
        mo_u, mo_t = market_orders(a_us), market_orders(a_th)
        our_ord += len(mo_u)
        opp_ord += len(mo_t)
        for o in mo_u:
            if o and o[0] == "SELL":
                our_sell[o[1]] += o[2] if len(o) > 2 and isinstance(o[2], int) else 1
                if our_first_sell is None:
                    our_first_sell = t
        for o in mo_t:
            if o and o[0] == "SELL":
                opp_sell[o[1]] += o[2] if len(o) > 2 and isinstance(o[2], int) else 1
                if opp_first_sell is None:
                    opp_first_sell = t
    rank, score = lb.get(opp, (None, None))
    rows.append({
        "ep": rec["ep"], "opp": opp, "seat": us, "margin": margin,
        "us": rw[us], "them": rw[them],
        "opp_rank": rank, "opp_score": score,
        "ident": ident / max(both, 1),
        "our_ord": our_ord, "opp_ord": opp_ord,
        "nsteps": n, "statuses": rec.get("statuses"),
        "our_sell": dict(our_sell), "opp_sell": dict(opp_sell),
    })

rows.sort(key=lambda r: -r["ep"])
print(f"{'ep':>9} {'opp':<26} {'seat':>4} {'margin':>8} {'oppLB':>7} {'ident':>5} {'oOrd':>5} {'tOrd':>5} {'banks'}")
for r in rows:
    print(f"{r['ep']:>9} {r['opp'][:26]:<26} {r['seat']:>4} {r['margin']:>8.0f} "
          f"{(r['opp_score'] or 0):>7.0f} {r['ident']:>5.2f} {r['our_ord']:>5} {r['opp_ord']:>5} "
          f"{r['us']:.0f}/{r['them']:.0f}")

with open(os.path.join(HERE, "analysis.json"), "w") as f:
    json.dump(rows, f, indent=1)
w = sum(1 for r in rows if r["margin"] > 0)
l = sum(1 for r in rows if r["margin"] < 0)
print(f"\nW{w} L{l} T{len(rows)-w-l}  median margin {sorted(r['margin'] for r in rows)[len(rows)//2]:.0f}")
