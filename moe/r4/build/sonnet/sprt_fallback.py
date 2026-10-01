import math

def sprt(p0, p1, alpha, beta):
    A = math.log((1-beta)/alpha)   # cross up -> reject p0 (favor p1, "validated")
    B = math.log(beta/(1-alpha))   # cross down -> reject p1 (favor p0, "shepherd-shaped")
    llr_win = math.log(p1/p0)
    llr_loss = math.log((1-p1)/(1-p0))
    return A, B, llr_win, llr_loss

def apply(w, l, p0, p1, alpha, beta, label):
    A, B, lw, ll = sprt(p0, p1, alpha, beta)
    llr = w*lw + l*ll
    verdict = "PROMOTE-signal (crosses A)" if llr >= A else ("KILL-signal (crosses B)" if llr <= B else "inconclusive, continue")
    # binomial exact prob of this-or-more-extreme under each hypothesis (one-sided, observed w wins out of n)
    n = w + l
    from math import comb
    p_under_p1 = sum(comb(n,k)*p1**k*(1-p1)**(n-k) for k in range(0, w+1))   # P(<=w wins | p1) one-sided "as bad or worse"
    p_under_p0 = sum(comb(n,k)*p0**k*(1-p0)**(n-k) for k in range(w, n+1))   # P(>=w wins | p0)
    print(f"{label}: n={n} w={w} l={l} p0={p0} p1={p1} | A={A:.3f} B={B:.3f} llr_win={lw:.3f} llr_loss={ll:.3f} | LLR={llr:.3f} -> {verdict}")
    print(f"    P(<= {w}/{n} wins | true p={p1}) = {p_under_p1:.4f}   P(>= {w}/{n} wins | true p={p0}) = {p_under_p0:.4f}")
    # games needed to cross each boundary from 0 on a pure streak
    n_kill = math.ceil(-B/(-ll)) if ll < 0 else None
    n_promote = math.ceil(A/lw) if lw > 0 else None
    print(f"    pure-loss-streak games to hit kill bound: {n_kill}; pure-win-streak games to hit promote bound: {n_promote}")
    print()

for alpha, beta in [(0.10,0.10), (0.05,0.05)]:
    print(f"=== alpha=beta={alpha} ===")
    apply(1,1, 0.59, 0.80, alpha, beta, "2000-2200 (shepherd p0=0.59)")
    apply(2,1, 0.27, 0.80, alpha, beta, "2200-2400 (shepherd p0=0.27)")
    apply(0,3, 0.15, 0.80, alpha, beta, "2400+    (shepherd p0=0.15)")
    apply(4,4, 0.30, 0.80, alpha, beta, "pooled >=2000 (generic collapse p0=0.30)")
