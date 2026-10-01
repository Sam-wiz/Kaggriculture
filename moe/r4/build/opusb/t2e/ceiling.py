"""T2E ceiling: can a day-12 tomato cohort (harvest d20-23) on top of V219's day-18 cohort (d26-29) pay?
Model = C1's own CXTB revenue model (drain 1+6*shops-2.4/day, 20 units/day on harvest days, engine TOMATO
price), fed ORACLE shop sequences (upper bound on what a d12 decision can know). Cohort cost is calibrated
from measured closed-loop values in t2/{A,B}.jsonl (value = measured dmargin vs CXTB projected revenue)."""
import json, math, random, statistics as st
P = {'base': 60, 'I0': 10000, 'T': 200}
def price(inv):
    b, I0, T = 60, 10000, 200
    if inv < I0:
        u = (I0 - inv) / T; return max(1, int(round(b + 0.4 * b * (u + 8 * max(0, u - 1) ** 2))))
    return max(1, int(round(b - 0.6 * b / math.sqrt(T) * math.sqrt(inv - I0))))
TOM = lambda s: s in ('PIZZA_SHOP', 'FARMERS_MARKET')
def nshops(seq, d): return sum(TOM(s) for i, s in enumerate(seq) if 3 * (i + 1) <= d)
def inv_at(seq, d): return 10000 - d - 6 * sum(max(0, d - 3 * (i + 1)) for i, s in enumerate(seq) if TOM(s))
def run(seq, d0, cohorts, slack=2.4, pend=None):
    """cohorts: list of harvest-day tuples; returns revenue per cohort. pend: CXTB expectation instead of oracle."""
    inv = float(inv_at(seq, d0)); rev = [0.0] * len(cohorts); last = max(max(c) for c in cohorts)
    sh = float(nshops(seq, d0)) if pend is not None else None
    for d in range(d0, last + 1):
        if pend is not None: sh += pend.get(d, 0.0); s = sh
        else: s = nshops(seq, d)
        inv -= 1.0 + 6.0 * s - slack
        for k, c in enumerate(cohorts):
            if d in c:
                for _ in range(20): rev[k] += price(int(round(inv))); inv += 1
    return rev
A, B = (20, 21, 22, 23), (26, 27, 28, 29)
# --- calibrate cohort cost from measured closed-loop (V219 OFF rows: value=-dm; minrev5500 rows: value=dm)
cal = []
for fn in ('moe/r4/build/opusb/t2/A.jsonl', 'moe/r4/build/opusb/t2/B.jsonl'):
    for l in open(fn):
        r = json.loads(l)
        if 'cx' not in r or not r['cx']: continue
        cal.append((r['seed'], r['o'], r['minrev'], r['cx'][0]['revenue'], r['m'], r['shops']))
base = {(s, o): m for s, o, mr, rv, m, sh in cal if mr == 9000}
costs = []
for s, o, mr, rv, m, sh in cal:
    if mr == 9000 or (s, o) not in base: continue
    dm = m - base[(s, o)]; v219_on = mr < 9000
    val = dm if v219_on else -dm
    if abs(dm) > 1e-9: costs.append(rv - val)
print('calibration n', len(costs), 'cost median %.0f  IQR %.0f..%.0f' % (st.median(costs), *st.quantiles(costs, n=4)[::2]))
C = st.median(costs); LAND = 4000; NONLAND = C - LAND
# model check on the 24 real seeds: our d18 projection vs CXTB's reported revenue
chk = [(rv, run(sh, 18, [B], pend={22: .25, 24: .25})[0]) for s, o, mr, rv, m, sh in cal if mr == 9000 and o == 'shep']
print('model vs CXTB-reported d18 revenue: max |diff| %.0f over %d seeds' % (max(abs(a - b) for a, b in chk), len(chk)))
def world(seq):
    rB_exp = run(seq, 18, [B], pend={22: .25, 24: .25})[0]
    rB = run(seq, 18, [B])[0]; rA = run(seq, 12, [A])[0]; rAB = run(seq, 12, [A, B])
    c1 = (rB - C) if rB_exp >= 9000 else 0.0
    opts = {'none': 0.0, 'B': rB - C, 'A': rA - C, 'AB': sum(rAB) - LAND - 2 * NONLAND}
    best = max(opts, key=opts.get)
    return c1, opts[best], best, rA, rAB
TYPES = ['PIZZA_SHOP', 'FARMERS_MARKET', 'BAKERY', 'BRUNCH_SPOT', 'YARN_STORE', 'ICE_CREAM_SHOP', 'PET_CAFE', 'SMOOTHIE_SHOP']
rng = random.Random(7); N = 20000; gains = []; picks = {}; cnt = 0
for _ in range(N):
    seq = [rng.choice(TYPES) for _ in range(8)]
    c1, t2e, best, rA, rAB = world(seq); g = t2e - c1; gains.append(g); picks[best] = picks.get(best, 0) + 1
f = sum(g > 0 for g in gains) / N
print('ORACLE T2E vs C1 over %d random shop draws: P(gain>0)=%.3f  mean gain $%.0f/g  picks %s' % (N, f, st.mean(gains), picks))
print('  => head-to-head ceiling vs C1 (non-firing games are exact mirrors = ties) <= %.3f' % (0.5 + f / 2))
for s, o, mr, rv, m, sh in cal:
    if mr == 9000 and o == 'shep':
        c1, t2e, best, rA, rAB = world(sh); print('  seed', s, 'shops', sum(map(TOM, sh)), 'rA %.0f rA+B %.0f+%.0f' % (rA, *rAB), 'best', best, 'gain %.0f' % (t2e - c1))
