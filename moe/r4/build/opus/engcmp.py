"""Compare per-seat economics: our self-play pair (engdec.py output) vs the recorded top pair (decode.py output) on
the same dump episodes (same seed, same pinned shops). Means per seat over matched episodes.
usage: engcmp.py ENGDEC.jsonl DEC_TOP10.jsonl
"""
import json, sys, statistics as S, collections
SEED = dict(WHEAT=10, CARROT=20, TOMATO=50, STRAWBERRY=100, MELON=80)
ANIM = dict(GOOSE=300, COW=400, SHEEP=500)
FIB = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
PRODS = ("MILK", "WOOL", "STRAWBERRY", "MELON", "EGG", "TOMATO", "CARROT", "WHEAT", "FERTILIZER")
eng = [json.loads(l) for l in open(sys.argv[1])]
top = {json.loads(l)["ep"]: json.loads(l) for l in open(sys.argv[2])}


def top_seat(s):
    c = dict(seed=sum(SEED[k] * sum(v.values()) for k, v in s["seeds"].items()),
             animal=sum(ANIM[k] * sum(v.values()) for k, v in s["animals"].items()),
             hire=sum(sum(FIB[:n]) for n in s["hires"].values()), land=[0, 1000, 3000, 7000][len(s["land"])])
    return dict(bank=s["bank"], sell={k: dict(u=v["u"], rev=v["rev"]) for k, v in s["sell"].items()},
                buyp=s["buyp"], cost=c, herd=s["herd"], land=s["land"])


def herdmean(seats, day, k):
    return S.mean(x["herd"][day].get(k, 0) if len(x["herd"]) > day else 0 for x in seats)


by = collections.defaultdict(list)
for r in eng:
    if "err" in r or r["ep"] not in top: continue
    by[r["name"]].append(r)
for name, rs in by.items():
    ours = [s for r in rs for s in r["seats"]]
    tops = [top_seat(s) for r in rs for s in top[r["ep"]]["seats"]]
    print(f"== {name}: {len(rs)} worlds (shops pinned ok {sum(r['shops_ok'] for r in rs)}/{len(rs)})")
    print(f"   bank/seat  ours {S.mean(x['bank'] for x in ours):9.0f}  top {S.mean(x['bank'] for x in tops):9.0f}  diff {S.mean(x['bank'] for x in ours)-S.mean(x['bank'] for x in tops):+8.0f}")
    print(f"   {'product':10} {'u ours':>7} {'u top':>7} {'rev ours':>9} {'rev top':>9} {'d rev':>8} {'p ours':>7} {'p top':>7}")
    tot = 0
    for p in PRODS:
        uo = S.mean(x["sell"].get(p, {}).get("u", 0) for x in ours); ut = S.mean(x["sell"].get(p, {}).get("u", 0) for x in tops)
        ro = S.mean(x["sell"].get(p, {}).get("rev", 0) for x in ours); rt = S.mean(x["sell"].get(p, {}).get("rev", 0) for x in tops)
        tot += ro - rt
        print(f"   {p:10} {uo:7.0f} {ut:7.0f} {ro:9.0f} {rt:9.0f} {ro-rt:+8.0f} {ro/max(uo,1e-9):7.1f} {rt/max(ut,1e-9):7.1f}")
    print(f"   {'revenue':10} {'':7} {'':7} {'':9} {'':9} {tot:+8.0f}")
    for k in ("seed", "animal", "hire", "land"):
        co = S.mean(x["cost"][k] for x in ours); ct = S.mean(x["cost"][k] for x in tops)
        print(f"   cost {k:6} ours {co:8.0f} top {ct:8.0f}  d {-(co-ct):+7.0f} (effect on bank)")
    for it in ("WHEAT", "FERTILIZER"):
        bo = S.mean(x["buyp"].get(it, [0, 0])[1] for x in ours); bt = S.mean(x["buyp"].get(it, [0, 0])[1] for x in tops)
        uo = S.mean(x["buyp"].get(it, [0, 0])[0] for x in ours); ut = S.mean(x["buyp"].get(it, [0, 0])[0] for x in tops)
        print(f"   buy {it:10} units ours {uo:6.0f} top {ut:6.0f}  cost d {-(bo-bt):+7.0f}")
    for day in (5, 10, 15, 20, 28):
        print(f"   dawn d{day+1:2d} " + " ".join(f"{k[-5:]}={herdmean(ours, day, k):.1f}/{herdmean(tops, day, k):.1f}"
                                       for k in ("COW", "SHEEP", "GOOSE", "P_STRAWBERRY", "P_TOMATO", "P_CARROT", "P_WHEAT", "P_MELON")))
    print("   land steps ours", collections.Counter(tuple(x["land"]) for x in ours).most_common(2), " top", collections.Counter(tuple(x["land"]) for x in tops).most_common(2))
