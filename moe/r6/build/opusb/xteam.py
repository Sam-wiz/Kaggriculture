"""r6 opusb: cross-team lineage by modal day-0..2 tapes (steps 1..72; seed-independent before shop draws).
For each team (>=4 seats in mine/top10): modal unit-op string and market list per step. Pairwise identity = share of
steps 1..72 where modal unit ops equal (U) / market lists equal (M). Also modal step-1 market."""
import glob, gzip, json, collections, itertools
N = 72
seats = collections.defaultdict(list)
for p in sorted(glob.glob("mine/top10/*.json.gz")):
    d = json.load(gzip.open(p, "rt"))
    for s in range(2):
        a = d["actions"]
        seats[d["teams"][s]].append(([json.dumps([a[t][s].get("farmer")] + list(a[t][s].get("hands") or [])) if isinstance(a[t][s], dict) else "x" for t in range(1, N + 1)],
                                      [json.dumps(a[t][s].get("market") or []) if isinstance(a[t][s], dict) else "x" for t in range(1, N + 1)]))
modal = {}
for t, L in seats.items():
    if len(L) < 4: continue
    mu = [collections.Counter(x[0][k] for x in L).most_common(1)[0] for k in range(N)]
    mm = [collections.Counter(x[1][k] for x in L).most_common(1)[0] for k in range(N)]
    modal[t] = ([m[0] for m in mu], [m[0] for m in mm], sum(m[1] for m in mu) / N / len(L))
lane = ["KawattaTaido", "Azat Akhtyamov", "TheEggman", "Arda Ceylan", "nah id win"]
top = ["DECEM", "Boey", "M & M & P & Q", "Vadim Vasilenko", "Majkel1337", "DSM", "Unknown Mother-Goose", "Fourth Quadrant"]
names = sorted(modal, key=lambda t: (t not in lane, t not in top, t))
res = {}
for a in lane:
    if a not in modal: continue
    row = []
    for b in names:
        if b == a: continue
        U = sum(x == y for x, y in zip(modal[a][0], modal[b][0])) / N; M = sum(x == y for x, y in zip(modal[a][1], modal[b][1])) / N
        row.append((round(U, 2), round(M, 2), b))
    row.sort(reverse=True); res[a] = row
    print(f"{a} (self-consistency {modal[a][2]:.2f}) nearest by day-0..2 unit tape:", row[:6])
json.dump(res, open("moe/r6/build/opusb/xteam.json", "w"), ensure_ascii=False)
print("step-1 unit ops:", {t: modal[t][0][0][:60] for t in lane if t in modal})
