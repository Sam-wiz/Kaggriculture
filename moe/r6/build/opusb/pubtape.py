"""r6 opusb: do the new public agents (rivals9 + subAA_harvest) open like any decoded top-20/lane team?
Self-play each candidate in kagsim on 6 seeds for 48 steps; mean full-action identity vs each team's recorded seats
(xident.py convention, steps 1..48), next to each team's within-team identity."""
import json, gzip, glob, sys, collections, itertools
sys.path.insert(0, "moe/r3/build/opus"); sys.path.insert(0, "kaggriculture-cppsim")
from run import load, act
import kagsim
N = 48
C = ["subAA_harvest.py", "subY_C1_predict2.py"] + sorted(glob.glob("rivals9/*/_entry.py"))
def F(a): return json.dumps([a.get("farmer"), list(a.get("hands") or []), a.get("market") or []]) if isinstance(a, dict) else "x"
tapes = {}
for c in C:
    T = []
    for seed in range(9100001, 9100007):
        try:
            a, _ = load(c, "pa"); b, _ = load(c, "pb"); g = kagsim.Game(seed=seed); tp = [[], []]
            for t in range(N):
                o0, o1 = g.observe(0), g.observe(1); x, y = act(a, o0), act(b, o1)
                tp[0].append(F(x)); tp[1].append(F(y)); g.step(x, y)
            T += tp
        except Exception as e:
            print("ERR", c, repr(e)[:60]); break
    if T: tapes[c] = T
TEAMS = ["DSM", "Vadim Vasilenko", "Unknown Mother-Goose", "DECEM", "M & M & P & Q", "Majkel1337", "Boey", "Fourth Quadrant", "mtmr_s1",
         "KawattaTaido", "Azat Akhtyamov", "Russell Kirk", "kigasudayooo", "TheEggman", "Arda Ceylan", "nah id win", "Smackaveli"]
S = collections.defaultdict(list)
for p in sorted(glob.glob("mine/top10/*.json.gz")):
    try: d = json.load(gzip.open(p, "rt"))
    except Exception: continue
    for s in range(2):
        t = d["teams"][s]
        if t in TEAMS and len(S[t]) < 30: S[t].append([F(d["actions"][k][s]) for k in range(1, N + 1)])
def I(a, b): return sum(x == y for x, y in zip(a, b)) / N
print("cand".ljust(40), "self", " ".join(t[:6].rjust(6) for t in TEAMS))
for c, T in tapes.items():
    within = sum(I(x, y) for x, y in itertools.combinations(T, 2)) / max(1, len(T) * (len(T) - 1) // 2)
    print(c.split("/")[-2 if c.startswith("rivals") else 0][:39].ljust(40), f"{within:.2f}", " ".join(f"{sum(I(x, y) for x in T for y in S[t]) / (len(T) * len(S[t])):6.2f}" if S[t] else "   n/a" for t in TEAMS))
