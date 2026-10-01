"""What fraction of our real opponents run the same agent we do?

This decides whether the mirror edge is worth anything. Price-impact slot ordering wins ~93% of
mirror matches (120 games, 0.93 win / 0.00 tie) but only ~+68 against a varied field, so its value
is almost entirely a function of how many opponents are near-clones.

mikelou1 (#21) states public notebooks are "like 90% of the leaderboard", and sobameshi's dump
fingerprinting found 18 teams playing a single public opening on 2026-09-02. If that holds for the
agent WE are running, the edge is large:

    overall win-rate gain  ~=  clone_share x (0.93 - 0.50)

so 30% clones is +0.13 (~+100 rating), 50% is +0.21 (~+170).

Measured here by action identity against our own seat, which is exact: two runs of the same
deterministic agent on the same seed emit the same actions. Reported at several thresholds because
a near-clone (a public base plus someone's overlay) still mirrors for most of the game.
"""
import collections
import glob
import gzip
import json
import math
import os
import subprocess
import sys

KA = ".venv/bin/kaggle"
SUBS = {"56394147": "pipe16", "56394286": "metav4", "56366726": "subJ_2945",
        "56366720": "subH2_v48"}


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


def main():
    own = owners()
    rows = []
    for p in glob.glob("mine/opp/*.json.gz"):
        try:
            d = json.load(gzip.open(p, "rt"))
        except Exception:
            continue
        t = d.get("teams") or []
        if "Sam-wiz" not in t or not d.get("rewards") or t[0] == t[1]:
            continue
        ep = int(d["episode_id"])
        if ep not in own:
            continue
        acts = d.get("actions") or []
        if not acts:
            continue
        me = t.index("Sam-wiz")
        same = sum(1 for a in acts if a[me] == a[1 - me]) / len(acts)
        # prefix identity: how long before the two seats first differ
        div = next((i for i, a in enumerate(acts) if a[me] != a[1 - me]), len(acts))
        a, b = d["rewards"][me], d["rewards"][1 - me]
        rows.append(dict(build=own[ep], opp=t[1 - me], same=same, div=div,
                         res=1 if a > b else (0.5 if a == b else 0), m=a - b))
    if not rows:
        print("no episodes with action tapes for the current builds")
        return
    print(f"{len(rows)} episodes with full action tapes\n")
    print(f"{'threshold':<22}{'games':>8}{'share':>9}{'our win rate':>15}{'mean margin':>14}")
    for thr in (0.999, 0.99, 0.95, 0.90, 0.80, 0.60):
        g = [r for r in rows if r["same"] >= thr]
        if not g:
            print(f"{'>=' + f'{thr:.1%}' + ' identical':<22}{0:>8}{0.0:>9.1%}{'--':>15}{'--':>14}")
            continue
        wr = sum(r["res"] for r in g) / len(g)
        mg = sum(r["m"] for r in g) / len(g)
        print(f"{'>=' + f'{thr:.1%}' + ' identical':<22}{len(g):>8}{len(g)/len(rows):>9.1%}"
              f"{wr:>15.3f}{mg:>+14,.0f}")

    print(f"\n{'prefix shared':<22}{'games':>8}{'share':>9}")
    for lo in (600, 300, 150, 72, 24):
        g = [r for r in rows if r["div"] >= lo]
        print(f"{'first ' + str(lo) + ' turns':<22}{len(g):>8}{len(g)/len(rows):>9.1%}")

    share = len([r for r in rows if r["same"] >= 0.90]) / len(rows)
    gain = share * (0.93 - 0.50)
    def rating(p, beta=200.0):
        p = min(max(p, 1e-6), 1 - 1e-6)
        # crude probit inverse, adequate near 0.5
        return math.sqrt(2) * beta * (p - 0.5) * math.sqrt(2 * math.pi)
    print(f"\nnear-clone share (>=90% identical actions): {share:.1%}")
    print(f"implied overall win-rate gain from a 0.93 mirror edge: {gain:+.3f}")
    print(f"implied rating gain (beta=200): {rating(0.5 + gain):+.0f}")
    print("\nTop opponents by action identity:")
    by = collections.defaultdict(list)
    for r in rows:
        by[r["opp"]].append(r["same"])
    for opp, v in sorted(by.items(), key=lambda kv: -max(kv[1]))[:12]:
        print(f"   {opp[:30]:<32}{max(v):>7.1%}  ({len(v)} games)")


if __name__ == "__main__":
    main()
