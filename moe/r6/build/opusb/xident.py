"""r6 opusb: mean pairwise step-identity of full actions (units+market) over steps 1..N between seats of team A and team B
(within-team on the diagonal). Ratio cross/within ~1 => code indistinguishable over the opening. N=48 (days 0-1)."""
import json, gzip, glob, collections, itertools, random, sys
N = int(sys.argv[1]) if len(sys.argv) > 1 else 48
TEAMS = ["Majkel1337", "DSM", "Unknown Mother-Goose", "Vadim Vasilenko", "M & M & P & Q", "DECEM", "Boey", "Fourth Quadrant", "mtmr_s1",
         "KawattaTaido", "Azat Akhtyamov", "Russell Kirk", "kigasudayooo", "TheEggman", "Arda Ceylan", "nah id win", "tetsuya & yuanzhe & guoqi", "HowardLeeTW", "Smackaveli"]
def F(a): return json.dumps([a.get("farmer"), list(a.get("hands") or []), a.get("market") or []]) if isinstance(a, dict) else "x"
S = collections.defaultdict(list)
random.seed(1)
for p in sorted(glob.glob("mine/top10/*.json.gz")):
    try: d = json.load(gzip.open(p, "rt"))
    except Exception: continue
    A = d["actions"]
    for s in range(2):
        t = d["teams"][s]
        if t in TEAMS and len(S[t]) < 30: S[t].append([F(A[k][s]) for k in range(1, N + 1)])
def ident(a, b): return sum(x == y for x, y in zip(a, b)) / N
T = [t for t in TEAMS if len(S[t]) >= 1]
M = {}
for a in T:
    for b in T:
        if a == b:
            pr = list(itertools.combinations(S[a], 2)); M[a, b] = sum(ident(x, y) for x, y in pr) / len(pr) if pr else float("nan")
        else:
            M[a, b] = sum(ident(x, y) for x in S[a] for y in S[b]) / (len(S[a]) * len(S[b]))
print(f"N={N}; n seats:", {t[:10]: len(S[t]) for t in T})
print(" " * 13 + " ".join(t[:6].rjust(6) for t in T))
for a in T: print(a[:12].ljust(13) + " ".join(f"{M[a, b]:6.2f}" for b in T))
json.dump({f"{a}|{b}": v for (a, b), v in M.items()}, open(f"moe/r6/build/opusb/xident_{N}.json", "w"), ensure_ascii=False)
