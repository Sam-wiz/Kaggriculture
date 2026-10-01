# devin-q lane: E[max(R_M30B, R_X)] for slot-B candidates under max-of-two scoring.
# (1) per-seed loss correlation v8 vs M30B on shared opponents/seeds.
# (2) scenario EV table.
import json, math, itertools, os
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)

def rows(p):
    try:
        out = []
        for l in open(p):
            try:
                r = json.loads(l)
                if "err" not in r: out.append(r)
            except Exception: pass
        return out
    except FileNotFoundError:
        return []

def wr(rows_, cand, opp=None):
    g = [r for r in rows_ if r.get("sw", 0) == 0 and (opp is None or r["b"] == opp)]
    w = sum(r["ra"] > r["rb"] for r in g); l = sum(r["ra"] < r["rb"] for r in g)
    return w, l, len(g)

m30b = rows("moe/r6/build/devin/screen2_M30B.jsonl")
v8 = rows("moe/r6/build/devin/screen2_r34v8.jsonl") or rows("moe/r6/build/resume/r34_rr.jsonl")

# shared opponents between the two screens
ops = sorted({r["b"] for r in m30b} & {r["b"] for r in v8})
print("shared opponents:", ops)

# per (opp, seed) outcome vectors
def outc(rs, opp, seed):
    g = [r for r in rs if r.get("sw", 0) == 0 and r["b"] == opp and r["seed"] == seed]
    return (g[0]["ra"] > g[0]["rb"]) if g else None

pairs = []
for opp in ops:
    for s in range(9100001, 9100021):
        a, b = outc(m30b, opp, s), outc(v8, opp, s)
        if a is not None and b is not None: pairs.append((opp, s, a, b))

both_loss = sum(1 for _, _, a, b in pairs if not a and not b)
m30b_loss = sum(1 for _, _, a, b in pairs if not a)
v8_loss = sum(1 for _, _, a, b in pairs if not b)
v8_loss_given_m30b = sum(1 for _, _, a, b in pairs if not a and not b)
print(f"shared cells: {len(pairs)}  M30B losses: {m30b_loss}  v8 losses: {v8_loss}  both-lose cells: {both_loss}")
print("cells where M30B lost:", [(o, s) for o, s, a, b in pairs if not a])
print("cells where v8 lost:", [(o, s) for o, s, a, b in pairs if not b][:20])

# phi correlation on shared cells
n11 = sum(1 for _, _, a, b in pairs if a and b); n10 = sum(1 for _, _, a, b in pairs if a and not b)
n01 = sum(1 for _, _, a, b in pairs if not a and b); n00 = sum(1 for _, _, a, b in pairs if not a and not b)
den = math.sqrt((n11+n10)*(n01+n00)*(n11+n01)*(n10+n00)) or 1
phi = (n11*n00 - n10*n01)/den
print(f"outcome table: both-win {n11}, M30B-only-win {n10}, v8-only-win {n01}, both-lose {n00}; phi={phi:.2f}")

# seed-level: does v8's bad-seed set overlap M30B's? v8 bad seeds known: 5,8,12 (+4)
v8bad = {4, 5, 8, 12}
m30b_bad = {s for o, s, a, b in pairs if not a}
print("M30B's loss seeds:", m30b_bad, "| v8's known bad seeds:", v8bad, "| overlap:", m30b_bad & v8bad)

# (2) scenario EV
def emax(m1, m2, s=150):
    return m1 + (m2 - m1) * 0 + 0  # placeholder

def emax_corr(m1, m2, rho, s1=150, s2=150, n=40000):
    import random
    rng = random.Random(7)
    tot = 0.0
    for _ in range(n):
        z1 = rng.gauss(0, 1); z2 = rng.gauss(0, 1)
        r1 = m1 + s1 * z1
        r2 = m2 + s2 * (rho * z1 + math.sqrt(1 - rho * rho) * rng.gauss(0, 1))
        tot += max(r1, r2)
    return tot / n

print("\nE[max(M30B=2402, X)] scenarios (150pt ladder noise):")
for name, mx in (("M30B copy", 2402), ("v8", 2150), ("hyb2965", 1885)):
    for rho in (0.0, 0.3, 0.6, 0.9, 1.0):
        print(f"  X={name:10} rho={rho}: E[max] ≈ {emax_corr(2402, mx, rho):.0f}")
# collapse scenario: M30B's realized mean drops 400 (monoculture countered)
print("\ncollapse scenario (M30B mean -400):")
for name, mx in (("M30B copy", 2002), ("v8", 2150), ("hyb2965", 1885)):
    print(f"  X={name:10} rho=0.3: E[max] ≈ {emax_corr(2002, mx, 0.3):.0f}   rho=0.9: {emax_corr(2002, mx, 0.9):.0f}")
