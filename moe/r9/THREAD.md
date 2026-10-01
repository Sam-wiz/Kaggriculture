# MoE r9 — THREAD (cross-lane log)

## [matrix] ~19:45 UTC — decisive local screen done (640 eps, 0 err)

Seeds 9300-9319 fresh, both seats, harness.py. Full tables: `build/matrix/MATRIX.md`.

**vs m30b (n=24 each):** subAC_v8 **14-10 +936** — the ONLY candidate that beats
m30b | harvest 6-18 −149, shepherd 6-18 −506, C1R2 2-22 −694, metav4N 0-24 −1090,
f55recV2 0-24 −1775 | **v8hh 0-24 −80,343**; own-v8/v8x/v8hh2 all 0-24,
−101k..−120k.

**RR strength (n=120/agent):** m30b 0.877 > **ACv8 0.742** > harvest 0.625 >
C1R2 0.550 > shepherd 0.533 > f55recV2 0.342 > metav4N 0.242 > v8hh 0.091.
v8p (r34-v8+patch) beat m30b 10-6 AND ACv8 13-3 on 9300-07 — locally the
strongest r34 artifact, but live read truncated at 1696.

**KEY FINDING — live slot-2 v8hh is locally falsified: 0-120 vs every real
candidate** (loses 0-16 to even metav4N −92k), banks ~56-65k vs their ~96k.
No crashes — just earns ~2/3. The own-v8 family (v8/v8w/v8x/v8hh/v8hh2) is a
different codebase from r34-v8/subAC_v8 and all variants sit <600 live.
Its "+20k over v8" gate was in-family (reproduced: v8hh 12-0 +47k vs agents/v8)
but the base itself loses 0-24 −120k to m30b — the family climbed a broken
ladder. P(v8hh > m30b at lock) ≈ 0.

**Pair rec:** keep [m30b, v8hh] by default — the only real hedge (r34-v8:
ACv8 preferred for calibrated 2048, v8p for local strength) requires BOTH
remaining slots because next upload evicts the OLDER pair member = m30b.
Fresh-pair E[max] ≈ 1800-2000 < keeping m30b's 1735-climbing ≈ 2000-2200.
If swapped: `subAC_v8.py` then `subAB_m30b.py` → [ACv8′, m30b′]. Never spend
a slot on harvest (same chassis, correlated) or any own-v8 file.

Decorrelation note: m30b loses to chassis+overlay variants (autopsy 2-12);
r34-v8 loses ~25% to weak/erratic anchors — opposite weakness. ACv8 beat the
whole tape-archetype pool 59-21 here, so it covers the slice m30b fails on.
