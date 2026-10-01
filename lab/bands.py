"""Non-parametric comparison: win rate by opponent rating band.

The Bradley-Terry fit needs a beta, and no beta reproduces sub_final's known converged rating, so
its output is not trustworthy. Bucketing by opponent rating removes the assumption entirely: if the
router is really stronger, it must win MORE against opponents of the same strength.
"""
import glob
import gzip
import json
import statistics
import subprocess

KA = ".venv/bin/kaggle"
SUBS = {56053687: "router_slot", 56051487: "router2", 56050947: "router", 56039245: "sub_final",
        56036103: "sub_impact"}
BANDS = [(0, 2100), (2100, 2250), (2250, 2400), (2400, 2550), (2550, 9999)]


def collect():
    own = {}
    for s, n in SUBS.items():
        r = subprocess.run([KA, "competitions", "episodes", str(s), "-v"],
                           capture_output=True, text=True)
        for line in r.stdout.splitlines()[1:]:
            p = line.split(",")[0].strip()
            if p.isdigit():
                own[int(p)] = n
    LB = json.load(open("data/lb.json"))
    rows = []
    for p in glob.glob("mine/opp/*.json.gz"):
        d = json.load(gzip.open(p, "rt"))
        t = d["teams"]
        if "Sam-wiz" not in t or not d.get("rewards"):
            continue
        ep = int(d["episode_id"])
        if ep not in own or t[0] == t[1]:
            continue
        me = t.index("Sam-wiz")
        R = LB.get(t[1 - me])
        if R is None:
            continue
        m = d["rewards"][me] - d["rewards"][1 - me]
        rows.append(dict(b=own[ep], R=R, m=m,
                         res=1.0 if m > 0 else (0.5 if m == 0 else 0.0)))
    return rows


def line(name, rows):
    out = f"{name:<14}"
    for lo, hi in BANDS:
        g = [r for r in rows if lo <= r["R"] < hi]
        out += (f"{sum(r['res'] for r in g)/len(g):>6.2f}({len(g):>2})" if g else f"{'--':>10}")
    return out


if __name__ == "__main__":
    rows = collect()
    fam = [r for r in rows if r["b"] in ("router", "router2", "router_slot")]
    old = [r for r in rows if r["b"] in ("sub_final", "sub_impact")]
    hdr = f"{'build':<14}" + "".join(f"{f'{lo}-{hi}':>10}" for lo, hi in BANDS)
    print("WIN RATE BY OPPONENT RATING BAND   value(n)\n")
    print(hdr)
    print(line("ROUTER family", fam))
    print(line("newtape line", old))
    print()
    print("MEAN MARGIN BY BAND")
    print(hdr)
    for nm, rs in (("ROUTER family", fam), ("newtape line", old)):
        out = f"{nm:<14}"
        for lo, hi in BANDS:
            g = [r for r in rs if lo <= r["R"] < hi]
            out += (f"{statistics.mean(r['m'] for r in g):>+10,.0f}" if g else f"{'--':>10}")
        print(out)
    print(f"\ntotals: router family {len(fam)} games, mean opp "
          f"{statistics.mean(r['R'] for r in fam):.0f}, score "
          f"{sum(r['res'] for r in fam)/len(fam):.3f}")
    print(f"        newtape line  {len(old)} games, mean opp "
          f"{statistics.mean(r['R'] for r in old):.0f}, score "
          f"{sum(r['res'] for r in old)/len(old):.3f}")
