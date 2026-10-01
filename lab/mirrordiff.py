"""What do the near-clone opponents do in the 1-10% of turns where they differ from us?

50.8% of our opponents are >=90% action-identical to our own agent and we win only 0.349 of those.
A true mirror is 0.50 by construction, so whatever those opponents do on their few divergent turns
is a real, reproducible edge over the crowd we are stuck in -- and it is recorded in their tapes.

This finds every episode where the opponent shares most of our action stream, isolates the turns
where the two seats differ, and characterises the difference along the axes that can actually carry
value: which operation they use instead of ours, when in the season it happens, and -- separately,
because the market is where slot order and price impact live -- how their market orders differ.

Split by outcome throughout: differences that appear in games we LOSE are the candidates; ones that
appear equally in games we win are noise.
"""
import collections
import glob
import gzip
import json
import os
import statistics
import subprocess
import sys

KA = ".venv/bin/kaggle"
SUBS = {"56394147": "pipe16", "56394286": "metav4", "56366726": "subJ_2945",
        "56366720": "subH2_v48", "56331236": "subH_v48"}
MOVES = {"NORTH", "SOUTH", "EAST", "WEST"}


def owners():
    own = {}
    for sub, name in SUBS.items():
        r = subprocess.run([KA, "competitions", "episodes", sub, "-v"],
                           capture_output=True, text=True)
        for line in r.stdout.splitlines()[1:]:
            p = line.split(",")[0].strip()
            if p.isdigit():
                own[int(p)] = name
    return own


def units(a):
    if not isinstance(a, dict):
        return []
    return [a.get("farmer")] + list(a.get("hands") or [])


def op_of(u):
    if not u:
        return None
    return u[0] if isinstance(u, list) else str(u)


def load(own, min_same=0.90, max_same=1.01):
    out = []
    for p in glob.glob("mine/opp/*.json.gz"):
        try:
            d = json.load(gzip.open(p, "rt"))
        except Exception:
            continue
        t = d.get("teams") or []
        if "Sam-wiz" not in t or not d.get("rewards") or t[0] == t[1]:
            continue
        if int(d["episode_id"]) not in own:
            continue
        acts = d.get("actions") or []
        if not acts:
            continue
        me = t.index("Sam-wiz")
        same = sum(1 for a in acts if a[me] == a[1 - me]) / len(acts)
        if not (min_same <= same < max_same):
            continue
        a, b = d["rewards"][me], d["rewards"][1 - me]
        out.append(dict(ep=d["episode_id"], opp=t[1 - me], me=me, acts=acts,
                        same=same, won=a > b, margin=a - b))
    return out


def analyse(recs, label):
    if not recs:
        print(f"\n{label}: no episodes")
        return
    unit_sub = collections.Counter()      # (ours -> theirs) operation swaps
    mkt_diff = collections.Counter()
    day_hist = collections.Counter()
    extra_sell = collections.Counter()
    their_first = collections.Counter()
    n_turns = 0
    for r in recs:
        me, opp = r["me"], 1 - r["me"]
        for t, pair in enumerate(r["acts"]):
            A, B = pair[me], pair[opp]
            if A == B:
                continue
            n_turns += 1
            day_hist[t // 24] += 1
            ua, ub = units(A), units(B)
            for i in range(max(len(ua), len(ub))):
                oa = op_of(ua[i]) if i < len(ua) else None
                ob = op_of(ub[i]) if i < len(ub) else None
                if oa != ob:
                    ka = "MOVE" if oa in MOVES else (oa or "-")
                    kb = "MOVE" if ob in MOVES else (ob or "-")
                    unit_sub[(ka, kb)] += 1
            ma = [tuple(o) for o in ((A or {}).get("market") or [])]
            mb = [tuple(o) for o in ((B or {}).get("market") or [])]
            if ma != mb:
                mkt_diff["turns with different market"] += 1
                sa = [o for o in ma if o and o[0] == "SELL"]
                sb = [o for o in mb if o and o[0] == "SELL"]
                if [o[1] for o in sa] != [o[1] for o in sb] and sorted(o[1] for o in sa) == sorted(o[1] for o in sb):
                    mkt_diff["same sells, DIFFERENT ORDER"] += 1
                qa = sum(int(o[2]) for o in sa if len(o) > 2)
                qb = sum(int(o[2]) for o in sb if len(o) > 2)
                if qb > qa:
                    mkt_diff["they sell MORE units"] += 1
                    extra_sell["units"] += qb - qa
                elif qa > qb:
                    mkt_diff["we sell more units"] += 1
                if len(mb) > len(ma):
                    mkt_diff["they use more order slots"] += 1
                for o in mb:
                    if o and o[0] != "SELL":
                        their_first[o[0] + ":" + (o[1] if len(o) > 1 else "")] += 1
    print(f"\n=== {label}  ({len(recs)} episodes, {n_turns} divergent turns, "
          f"{n_turns/len(recs):.0f} per game) ===")
    print(f"median action identity {statistics.median(r['same'] for r in recs):.1%}, "
          f"mean margin {statistics.mean(r['margin'] for r in recs):+,.0f}")
    print("\n  top unit-op substitutions (ours -> theirs):")
    for (ka, kb), c in unit_sub.most_common(12):
        print(f"     {ka:<20} -> {kb:<20}{c:>7}")
    print("\n  market differences:")
    for k, c in mkt_diff.most_common():
        print(f"     {k:<34}{c:>7}")
    if extra_sell["units"]:
        print(f"     extra units they sell, total        {extra_sell['units']:>7}"
              f"  ({extra_sell['units']/len(recs):.0f}/game)")
    if their_first:
        print("\n  non-SELL market ops they issue on divergent turns:")
        for k, c in their_first.most_common(8):
            print(f"     {k:<34}{c:>7}")
    print("\n  when they diverge (day -> turns):")
    days = sorted(day_hist)
    line = "     "
    for d in days:
        line += f"{d}:{day_hist[d]} "
    print(line)


if __name__ == "__main__":
    lo = float(sys.argv[1]) if len(sys.argv) > 1 else 0.90
    hi = float(sys.argv[2]) if len(sys.argv) > 2 else 1.01
    own = owners()
    recs = load(own, lo, hi)
    print(f"{len(recs)} episodes in the {lo:.0%}-{hi:.0%} action-identity band")
    analyse([r for r in recs if not r["won"]], "GAMES WE LOST (the candidates)")
    analyse([r for r in recs if r["won"]], "GAMES WE WON (control)")
