"""r5 opus an1: how fixed is the family macro? land steps, hires/day, herd buys, crop plantings, dawn cash."""
import pickle, collections, statistics as st, json
D = pickle.load(open("moe/r5/build/opus/fam.pkl", "rb")); F = D["fam"]
print("family seats", len(F), "by team", collections.Counter(r["team"] for r in F))
# land
lc = collections.Counter(tuple(s for x in r["dec"] for s in x.get("land_step", [])) for r in F)
print("\nLAND steps (top 6):", lc.most_common(6), " share of top:", round(lc.most_common(1)[0][1] / len(F), 3))
# hires by day
print("\nHIRES/day: mean, sd, modal share")
H = [[r["dec"][d]["hire"] for r in F] for d in range(30)]
print(" ".join(f"d{d}:{st.mean(H[d]):.1f}±{st.pstdev(H[d]):.1f}({collections.Counter(H[d]).most_common(1)[0][0]}@{collections.Counter(H[d]).most_common(1)[0][1]/len(F):.2f})" for d in range(30)))
print("hires/game mean", st.mean(sum(r["dec"][d]["hire"] for d in range(30)) for r in F), "hire $/game", st.mean(sum(r["dec"][d]["hcost"] for d in range(30)) for r in F))
# dawn cash
print("\nDAWN CASH median / p90 by day")
print(" ".join(f"d{d}:{int(st.median(r['dawn'][d]['money'] for r in F))}/{int(sorted(r['dawn'][d]['money'] for r in F)[int(.9*len(F))])}" for d in range(0, 30)))
# animal buys by day
print("\nANIMAL buys: mean per day (COW,SHEEP,GOOSE)")
for d in range(0, 20):
    m = [st.mean(r["dec"][d]["animal"].get(a, 0) for r in F) for a in ("COW", "SHEEP", "GOOSE")]
    print(f" d{d}: " + " ".join(f"{x:.2f}" for x in m), end=";")
print()
print("\nHERD at dawn (mean COW/SHEEP/GOOSE), plants mean by crop, empty, weeds")
for d in (1, 3, 6, 7, 9, 10, 11, 12, 15, 18, 21, 24, 27, 29):
    h = [st.mean(r["dawn"][d]["herd"].get(a, 0) for r in F) for a in ("COW", "SHEEP", "GOOSE")]
    p = {c: round(st.mean(r["dawn"][d]["plants"].get(c, 0) for r in F), 1) for c in ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON")}
    e = st.mean(r["dawn"][d]["empty"] for r in F); w = st.mean(r["dawn"][d]["weeds"] for r in F)
    print(f" d{d:2d} herd {h[0]:.1f}/{h[1]:.1f}/{h[2]:.1f}  plants {p}  empty {e:.1f} weeds {w:.2f}")
# seed buys per day by crop
print("\nSEED buys mean per day by crop")
for d in range(30):
    print(f" d{d:2d} " + " ".join(f"{c[:3]}={st.mean(r['dec'][d]['seed'].get(c, 0) for r in F):5.1f}" for c in ("WHEAT", "CARROT", "TOMATO", "STRAWBERRY", "MELON")) +
          f"  buypWHEAT={st.mean(r['dec'][d]['buyp'].get('WHEAT', 0) for r in F):5.1f} FERT={st.mean(r['dec'][d]['buyp'].get('FERTILIZER', 0) for r in F):4.1f}")
print("\nBANK by team: mean, WR vs non-family, n")
for t in sorted({r["team"] for r in F}):
    R = [r for r in F if r["team"] == t]
    nf = [r for r in R if not r["opp"] in {x["team"] for x in F}]
    print(f" {t:22s} n={len(R):4d} bank={st.mean(r['bank'] for r in R):8.0f} WR(all)={st.mean(r['bank'] > r['obank'] for r in R):.2f}")
