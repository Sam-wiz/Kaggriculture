"""Sensitivity of the T2E oracle ceiling to cohort-A's non-land cost; isolates the d12-cohort share of the gain."""
import random, statistics as st
exec(open('moe/r4/build/opusb/t2e/ceiling.py').read().split('def world')[0].replace("print(", "(lambda *a, **k: None)("))
TYPES = ['PIZZA_SHOP','FARMERS_MARKET','BAKERY','BRUNCH_SPOT','YARN_STORE','ICE_CREAM_SHOP','PET_CAFE','SMOOTHIE_SHOP']
for NLA in (3828, 2500, 1500, 500):
    rng = random.Random(7); N = 20000; gA = []; fired = 0
    for _ in range(N):
        seq = [rng.choice(TYPES) for _ in range(8)] if 'TYPES' in dir() else None
        rB = run(seq, 18, [B])[0]; rAB = run(seq, 12, [A, B]); rA = rAB[0]
        rB_exp = run(seq, 18, [B], pend={22: .25, 24: .25})[0]
        c1 = (rB - C) if rB_exp >= 9000 else 0.0           # C1's actual policy
        withA = max(rA - LAND - NLA, sum(rAB) - LAND - NLA - NONLAND)  # A alone, or A+B sharing the land
        g = max(0.0, withA - c1)                            # oracle adds cohort A only if it beats C1's own B decision
        gA.append(g); fired += g > 0
    f = fired / N
    print('cohortA nonland $%d: P(A helps)=%.3f mean +$%.0f/g  ceiling vs C1 %.3f' % (NLA, f, st.mean(gA), 0.5 + f / 2))
