"""r6 opusb: are low-rank COW1+WHEAT5 seats the same code as the top family? day-0..2 unit/market tape identity
(steps 1..72) of each such seat vs the modal tape of each top-family team; plus result of that game."""
import json, gzip, glob, collections
KEY = {"BUY_ANIMAL COW 1", "BUY_PRODUCT WHEAT 5"}
FAM = ["Majkel1337", "DSM", "Unknown Mother-Goose", "Vadim Vasilenko", "M & M & P & Q", "DECEM", "mtmr_s1", "Azat Akhtyamov", "TheEggman", "Arda Ceylan"]
N = 72
def U(a): return json.dumps([a.get("farmer")] + list(a.get("hands") or [])) if isinstance(a, dict) else "x"
def M(a): return json.dumps(a.get("market") or []) if isinstance(a, dict) else "x"
fam = collections.defaultdict(list); low = []
for g in ["mine/opp/*.json.gz", "mine/top/*.json.gz", "mine/top10/*.json.gz"]:
    for p in glob.glob(g):
        try: d = json.load(gzip.open(p, "rt"))
        except Exception: continue
        A = d["actions"]
        if len(A) < N + 1: continue
        for s in range(2):
            a = A[1][s]; m = a.get("market") if isinstance(a, dict) else None
            if not m or not KEY <= {" ".join(str(x) for x in o) for o in m[:3]}: continue
            tape = ([U(A[t][s]) for t in range(1, N + 1)], [M(A[t][s]) for t in range(1, N + 1)])
            t = d["teams"][s]
            if t in FAM and len(fam[t]) < 80: fam[t].append(tape)
            elif t not in FAM and g.startswith("mine/opp"):
                low.append((t, d["episode_id"], d["teams"][1 - s], d["rewards"][s], d["rewards"][1 - s], tape))
modal = {t: ([collections.Counter(x[0][k] for x in L).most_common(1)[0][0] for k in range(N)],
             [collections.Counter(x[1][k] for x in L).most_common(1)[0][0] for k in range(N)]) for t, L in fam.items()}
for t, ep, o, b, ob, tape in sorted(low, key=lambda x: x[1]):
    best = sorted(((sum(x == y for x, y in zip(tape[0], modal[f][0])) / N, sum(x == y for x, y in zip(tape[1], modal[f][1])) / N, f) for f in modal), reverse=True)[:3]
    print(f"{ep} {t[:18]:18s} vs {o[:10]:10s} {b:>9,.0f} v {ob:>9,.0f} | nearest fam (U,M): " + "; ".join(f"{f[:10]} {u:.2f},{m:.2f}" for u, m, f in best))
print("fam modal pairwise U identity:")
F = list(modal)
for i in range(len(F)):
    print("  ", F[i][:12].ljust(12), " ".join(f"{sum(x == y for x, y in zip(modal[F[i]][0], modal[F[j]][0])) / N:.2f}" for j in range(len(F))))
