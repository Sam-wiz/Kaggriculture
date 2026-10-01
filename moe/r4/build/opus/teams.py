"""Per-team decode summary from decode.py output(s).
usage: teams.py DEC.jsonl[,DEC2.jsonl] [MIN_GAMES] [TEAM ...]
Prints per team: games, W-L, mean bank, opening signatures, land steps, hires/day, herd at d10/d20/d29,
seeds by crop, premium sales (units, price index, share sold d25-29), buy-backs, plan determinism
(share of days whose unit-op hash equals the team's modal hash for that day).
"""
import collections, json, statistics as S, sys

files = sys.argv[1].split(","); MIN = int(sys.argv[2]) if len(sys.argv) > 2 else 5
ONLY = set(sys.argv[3:])
recs = []
for fn in files:
    for line in open(fn):
        r = json.loads(line)
        if "err" in r or not all(r["match"]): continue
        recs.append(r)
by = collections.defaultdict(list)
for r in recs:
    for s in range(2):
        by[r["teams"][s]].append((r, s))


def med(x): return S.median(x) if x else 0


def sigkey(sig):
    return " | ".join(",".join("%s %s %s" % tuple((o + [None, None])[:3]) if len(o) >= 2 else o[0] for o in m) for m in sig[:2])


for team, gs in sorted(by.items(), key=lambda kv: -len(kv[1])):
    if len(gs) < MIN or (ONLY and team not in ONLY): continue
    W = sum(1 for r, s in gs if r["rewards"][s] > r["rewards"][1 - s]); Lo = sum(1 for r, s in gs if r["rewards"][s] < r["rewards"][1 - s])
    banks = [r["rewards"][s] for r, s in gs]
    marg = [r["rewards"][s] - r["rewards"][1 - s] for r, s in gs]
    print("=" * 100)
    print(f"{team}: n={len(gs)} W-L {W}-{Lo}  bank med {med(banks):,.0f}  margin med {med(marg):+,.0f}")
    sigs = collections.Counter(sigkey(r["seats"][s]["sig"]) for r, s in gs)
    for k, v in sigs.most_common(3): print(f"   open x{v}: {k[:150]}")
    lands = collections.Counter(tuple(r["seats"][s]["land"]) for r, s in gs)
    print("   land steps:", lands.most_common(4))
    hpd = [sum(r["seats"][s]["hires"].values()) for r, s in gs]
    print(f"   hires total med {med(hpd)}; per-day (modal game) {list(gs[0][0]['seats'][gs[0][1]]['hires'].values())[:30]}")
    for dd in (5, 10, 20, 29):
        c = collections.Counter()
        for r, s in gs:
            h = r["seats"][s]["herd"]
            if len(h) > dd:
                for k, v in h[dd].items():
                    if k in ("COW", "SHEEP", "GOOSE", "P_WHEAT", "P_CARROT", "P_TOMATO", "P_STRAWBERRY", "P_MELON", "weed", "quads"): c[k] += v
        print(f"   dawn d{dd+1:2d} mean: " + " ".join(f"{k}={v/len(gs):.1f}" for k, v in sorted(c.items())))
    seeds = collections.Counter()
    for r, s in gs:
        for crop, dd in r["seats"][s]["seeds"].items(): seeds[crop] += sum(dd.values())
    print("   seeds bought mean:", {k: round(v / len(gs), 1) for k, v in seeds.most_common()})
    an = collections.Counter()
    for r, s in gs:
        for a, dd in r["seats"][s]["animals"].items(): an[a] += sum(dd.values())
    print("   animals bought mean:", {k: round(v / len(gs), 1) for k, v in an.most_common()})
    rows = []
    for it in ("MILK", "WOOL", "STRAWBERRY", "MELON", "EGG", "TOMATO", "CARROT", "WHEAT", "FERTILIZER"):
        u = [r["seats"][s]["sell"].get(it, {}).get("u", 0) for r, s in gs]
        rev = [r["seats"][s]["sell"].get(it, {}).get("rev", 0) for r, s in gs]
        late = [r["seats"][s]["sell"].get(it, {}).get("ph", [0, 0, 0])[2] for r, s in gs]
        if sum(u) == 0: continue
        pi = sum(rev) / sum(u) / dict(WHEAT=25, CARROT=35, TOMATO=60, STRAWBERRY=120, MELON=250, EGG=50, MILK=160, WOOL=200, FERTILIZER=100)[it]
        rows.append(f"{it[:5]} u={S.mean(u):.0f} rev={S.mean(rev)/1000:.1f}k pi={pi:.2f} late={sum(late)/max(1,sum(u)):.2f}")
    print("   sells:", "; ".join(rows))
    bp = collections.Counter(); bc = collections.Counter()
    for r, s in gs:
        for it, (u, c) in r["seats"][s]["buyp"].items(): bp[it] += u; bc[it] += c
    print("   buy-backs mean:", {k: (round(v / len(gs)), round(bc[k] / max(1, v), 1)) for k, v in bp.items()},
          " discard mean", round(S.mean(r["seats"][s]["discard"] for r, s in gs), 1),
          " sell-steps mean", round(S.mean(r["seats"][s]["nsell_steps"] for r, s in gs)))
    # determinism: per day, share of games equal to the modal hash
    det = []
    for day in range(30):
        c = collections.Counter(r["seats"][s]["dayhash"][day] for r, s in gs)
        det.append(c.most_common(1)[0][1] / len(gs))
    print("   unit-op day-hash modal share d1..30:", " ".join(f"{x:.1f}" for x in det))
    opp = collections.Counter(r["teams"][1 - s] for r, s in gs)
    print("   opponents:", opp.most_common(8))
