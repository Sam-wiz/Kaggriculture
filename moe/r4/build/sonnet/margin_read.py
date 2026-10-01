"""
Margin-based re-read of claude-code's 06:55 UTC C1-vs->=2000 fingerprint table
(moe/r4/THREAD.md). Purpose: luna (05:50 post) disputed my sprt_fallback.py for
using a win/loss-only statistic on a matched-but-small (n=8) slice. This checks
whether a margin-aware statistic (mean, median, paired t, Wilcoxon signed-rank)
tells a different story than the 4-4 sign record, using ONLY the numbers already
posted in-thread (no new engine runs needed -- this is arithmetic on existing data).
"""
import statistics as st

# (opponent, rating, our_margin) from claude-code 06:55 UTC post, mine/opp/ fingerprints
rows = [
    ("Clement Lau", 2558, -98),
    ("Fanch", 2485, -381),
    ("kazuhiro3381", 2403, -338),
    ("tamref", 2393, -2216),
    ("Juste Me", 2341, 4733),
    ("我的AI是豆包", 2273, 2423),
    ("hinemos", 2187, 4977),
    ("SatoGo", 2028, -448),
]

margins = [m for _, _, m in rows]
n = len(margins)
wins = sum(1 for m in margins if m > 0)
mean_m = st.mean(margins)
median_m = st.median(margins)
sd_m = st.stdev(margins)
se_m = sd_m / n**0.5
t_stat = mean_m / se_m

print(f"n={n}  wins={wins}  losses={n-wins}  (sign record {wins}-{n-wins})")
print(f"mean margin   = {mean_m:+.1f}")
print(f"median margin = {median_m:+.1f}")
print(f"stdev         = {sd_m:.1f}")
print(f"SE            = {se_m:.1f}")
print(f"one-sample t  = {t_stat:+.3f}  (df={n-1}; |t|>2.365 needed for p<0.05 two-tailed)")

# Wilcoxon signed-rank vs 0 (exact ranks, small n, no ties in |margin|)
ranked = sorted(range(n), key=lambda i: abs(margins[i]))
ranks = [0] * n
for rank, idx in enumerate(ranked, start=1):
    ranks[idx] = rank
w_pos = sum(ranks[i] for i in range(n) if margins[i] > 0)
w_neg = sum(ranks[i] for i in range(n) if margins[i] < 0)
mean_w = n * (n + 1) / 4
var_w = n * (n + 1) * (2 * n + 1) / 24
z = (w_pos - mean_w) / var_w**0.5
print(f"Wilcoxon W+={w_pos}  W-={w_neg}  (of {n*(n+1)//2} total)  z={z:+.3f}  (|z|>1.96 needed for p<0.05)")

print()
print("sorted margins:", sorted(margins))
print(f"sum of losses (whiskers)  = {sum(m for m in margins if m<0):+d} over {n-wins} games")
print(f"sum of wins (blowouts)    = {sum(m for m in margins if m>0):+d} over {wins} games")
