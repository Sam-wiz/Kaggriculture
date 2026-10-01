"""Are our near-mirror losses a SEAT effect?

The near-clone games are decided by almost nothing: median 99.9% action identity and mean margin
-152. When two nearly identical agents play, the winner is settled by whatever small asymmetry the
engine has -- and the market is the obvious candidate, because orders settle slot-by-slot with our
order #i against their order #i, and both seats submit the same orders on the same turns.

If seat 0 (or 1) systematically wins those, and we sit in the losing seat more often than chance,
that alone explains a 0.349 mirror win rate without any strategy difference at all.

Also checks the margin distribution: a genuine strategy edge produces a shifted distribution, while
a tie-break asymmetry produces a pile of near-zero margins with a consistent sign.
"""
import collections
import glob
import gzip
import json
import statistics
import subprocess
import sys

KA = ".venv/bin/kaggle"
SUBS = {"56394147": "pipe16", "56394286": "metav4", "56366726": "subJ_2945",
        "56366720": "subH2_v48", "56331236": "subH_v48"}


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


if __name__ == "__main__":
    thr = float(sys.argv[1]) if len(sys.argv) > 1 else 0.90
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
        if int(d["episode_id"]) not in own:
            continue
        acts = d.get("actions") or []
        if not acts:
            continue
        me = t.index("Sam-wiz")
        same = sum(1 for a in acts if a[me] == a[1 - me]) / len(acts)
        a, b = d["rewards"][me], d["rewards"][1 - me]
        rows.append(dict(seat=me, same=same, m=a - b, res=1 if a > b else (0.5 if a == b else 0),
                         opp=t[1 - me]))
    near = [r for r in rows if r["same"] >= thr]
    print(f"{len(rows)} episodes, {len(near)} at >= {thr:.0%} identity\n")

    print(f"{'group':<26}{'n':>5}{'seat0 n':>9}{'seat0 wr':>10}{'seat1 n':>9}{'seat1 wr':>10}")
    for lab, g in (("near-clone", near), ("all episodes", rows),
                   (">=99% identity", [r for r in rows if r["same"] >= 0.99])):
        s0 = [r for r in g if r["seat"] == 0]
        s1 = [r for r in g if r["seat"] == 1]
        f = lambda v: f"{statistics.mean(x['res'] for x in v):.3f}" if v else "--"
        print(f"{lab:<26}{len(g):>5}{len(s0):>9}{f(s0):>10}{len(s1):>9}{f(s1):>10}")

    print(f"\nmargin distribution in near-clone games (n={len(near)}):")
    m = sorted(r["m"] for r in near)
    if m:
        for q, lab in ((0, "min"), (0.25, "p25"), (0.5, "median"), (0.75, "p75"), (1, "max")):
            print(f"   {lab:<8}{m[int(q*(len(m)-1))]:>+12,.0f}")
        tiny = [x for x in m if abs(x) < 500]
        print(f"   |margin| < 500 : {len(tiny)}/{len(m)} ({len(tiny)/len(m):.0%})")
        print(f"   of those, we lose: {sum(1 for x in tiny if x < 0)}/{len(tiny)}")

    print("\nper-seat margin sign in near-clone games:")
    for seat in (0, 1):
        g = [r for r in near if r["seat"] == seat]
        if not g:
            continue
        neg = sum(1 for r in g if r["m"] < 0)
        print(f"   seat {seat}: n={len(g):>3}  we lose {neg:>3} ({neg/len(g):.0%})  "
              f"mean margin {statistics.mean(r['m'] for r in g):+,.0f}")
