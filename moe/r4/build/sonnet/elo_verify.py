"""Verify opus's 07:26 Elo-implied win-count claims (RR-mapped C1 rating vs the 8 real
>=2000 opponents from claude-code's 06:55 fingerprint table), and compute the
Poisson-binomial P(observed | model) that the thread has not yet reported.

No sim, no workers -- pure arithmetic re-derivation of a claim already made in THREAD.md.
"""
import itertools

def p_win(r_a, r_b, scale=400.0):
    return 1.0 / (1.0 + 10 ** ((r_b - r_a) / scale))

# claude-code 06:55 fingerprint table: (name, rating, result W/L)
opponents = [
    ("Clement Lau",   2558, "L"),
    ("Fanch",         2485, "L"),
    ("kazuhiro3381",  2403, "L"),
    ("tamref",        2393, "L"),
    ("Juste Me",      2341, "W"),
    ("豆包",           2273, "W"),
    ("hinemos",       2187, "W"),
    ("SatoGo",        2028, "L"),
]

def poisson_binomial_pmf(probs):
    pmf = [1.0]
    for p in probs:
        new = [0.0] * (len(pmf) + 1)
        for k, pk in enumerate(pmf):
            new[k] += pk * (1 - p)
            new[k + 1] += pk * p
        pmf = new
    return pmf

for R in (2040, 2085, 2145):
    probs_all = [p_win(R, r) for _, r, _ in opponents]
    ge2400_idx = [i for i, (_, r, _) in enumerate(opponents) if r >= 2400]
    probs_ge2400 = [probs_all[i] for i in ge2400_idx]

    exp_wins_all = sum(probs_all)
    exp_wins_ge2400 = sum(probs_ge2400)
    p_0of3 = 1.0
    for p in probs_ge2400:
        p_0of3 *= (1 - p)

    pmf = poisson_binomial_pmf(probs_all)
    p_exactly3 = pmf[3]
    p_le3 = sum(pmf[:4])

    print(f"R={R}")
    print(f"  per-opponent P(C1 win): " + ", ".join(f"{n}={p:.3f}" for (n, _, _), p in zip(opponents, probs_all)))
    print(f"  E[wins | 8 games]     = {exp_wins_all:.3f}  (observed 3)")
    print(f"  E[wins | >=2400 trio] = {exp_wins_ge2400:.3f}  (observed 0)")
    print(f"  P(0/3 win | >=2400 trio, this R) = {p_0of3:.3f}")
    print(f"  Poisson-binomial P(X=3 | 8 games) = {p_exactly3:.3f}, P(X<=3) = {p_le3:.3f}  (observed X=3)")
    print()
