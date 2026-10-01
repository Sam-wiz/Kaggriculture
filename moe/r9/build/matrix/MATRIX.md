# MoE r9 — lane `matrix`: decisive local screen for the final pair

**When:** 09-30 ~19:00-19:45 UTC. **Data:** 640 episodes via `harness.run_episode`
(official interpreter), zero errors, zero non-DONE statuses.
**Seeds:** 9300-9311 (vs-m30b screen, ×2 seats), 9312-9319 (7-agent RR, ×2 seats),
9300-9307 (v8p/v8p2 supplement, ×2 seats). All fresh — no overlap with r8's 7100-7119.
**Runner:** `run_matrix.py` (ProcessPoolExecutor, W=4), raw records in `results.jsonl`,
aggregate via `analyze.py` / `rank.py`. Commands at bottom.

## 1. Hedge matrix — every candidate vs m30b (seeds 9300-9311, both seats, n=24)

| candidate | class | W-L vs m30b | mean margin | mean bank | seeds it won |
|---|---|---|---|---|---|
| **subAC_v8** (r34-v8, public verbatim) | reactive market-book | **14-10** | **+936** | **112,875** | 9300,01,05,08,09,10,11 |
| subAA_harvest | Harvest V78 = m30b chassis | 6-18 | −149 | 97,036 | 9300,05,07 |
| subW_shepherd | shepherd tape | 6-18 | −506 | 97,049 | 9301,02,07 |
| subZ_C1R2 | shepherd+C1R2 | 2-22 | −694 | 96,804 | 9307 |
| subN_metav4 | metav4+slack-clamp | 0-24 | −1,090 | 96,150 | — |
| subV2_f55rec | metav4+f55+reconcile | 0-24 | −1,775 | 95,366 | — |
| **v8hh (live slot-2, 56707845)** | own-v8x+PROG | **0-24** | **−80,343** | **65,393** | — |
| agents/v8x | own-v8w+stand-sell | 0-24 | −113,741 | 53,498 | — |
| agents/v8 | own-v8 base | 0-24 | −119,638 | 48,652 | — |
| v8hh2 (suppl., n=12) | own-v8hh+MMPQ tables | 0-12 | −101,346 | — | — |
| v8p (suppl., n=16, seeds 9300-07) | r34-v8+patch | **10-6** | **+1,950** | — | 9300,01,05,06,07 |
| v8p2 (suppl., n=16) | r34-v8+patch2 | **10-6** | **+2,665** | — | 9301,04,05,06,07 |

Per-seed margin (candidate − m30b), mean of both seats:

```
seed |   ACv8  harvest  sheph   C1R2  f55V2   mv4N    v8hh
9300 |  +7248    +134    -505    -181   -1246   -1359  -61246
9301 |  +4007    -215    +123    -514   -2147    -611  -75315
9302 |    -90    -348     +73     -16    -944     -33 -102834
9303 |  -6015    -117    -682    -785   -2664   -1161  -78391
9304 |  -2892    -166    -429    -779   -1913   -1158  -99738
9305 |  +7419     +10      -3    -444   -2245   -1539  -65768
9306 | -10431    -368    -829   -1071   -1820   -1165  -90080
9307 |  -8309     +34    +385     +39   -2143    -781  -61582
9308 |  +6798    -116   -1308   -1093   -1555   -1715  -82357
9309 |  +1683    -379    -472   -1210   -1303    -228 -107536
9310 |  +4395     -38    -896   -1162   -1074   -1035  -57479
9311 |  +7420    -224   -1526   -1108   -2249   -2298  -81790
```

Read: the tape-lineage candidates (harvest/shepherd/C1R2/f55rec/metav4) are all
near-mirrors earning ~95-97k vs m30b — coinflip losses, never threatening.
**subAC_v8 is the only agent that genuinely beats m30b** (earns MORE than m30b's
own bank, 112.9k vs 111.9k). m30b does not need a collapse to lose to it —
ACv8 won seed 9300 where m30b banked 165k.

## 2. Intrinsic strength — 7-agent RR (seeds 9312-9319, 16 eps/pair, n=120/agent)

Mean winrate and mean margin vs pool (incl. m30b games):

```
M30B        0.877   +38.7k
ACv8(pub)   0.742   +16.5k
harvest     0.625   +10.3k
C1R2        0.550   +10.7k
shepherd    0.533   +10.5k
f55recV2    0.342   +10.5k
metav4N     0.242   +10.4k
v8hh        0.091   −73.5k   (12 of its 12 non-losses are vs agents/v8)
```

Pairwise W-L (16 eps): ACv8 13-3 harvest, 12-4 C1R2, 12-4 shepherd,
11-5 f55rec, 11-5 metav4, 16-0 v8hh. harvest 9-7 shepherd, 11-5 C1R2,
15-1 f55rec, 15-1 metav4. C1R2 11-5 shepherd, 13-3 f55rec, 15-1 metav4.
shepherd 11-5 f55rec, 15-1 metav4. f55rec 11-5 metav4.
Supplementary: v8p 13-3 vs ACv8; ACv8 10-6 vs v8p2; v8hh 12-0 vs agents/v8.

**Strength order: m30b > ACv8 > harvest > C1R2 ≈ shepherd > f55rec > metav4 > {v8hh, v8, v8x, v8hh2}.**

## 3. The v8hh finding (critical for the live pair)

The live slot-2 submission 56707845 (`agents/v8hh.py`) is **worthless locally:
0-120 vs every real candidate** — loses 16-0 to even the weakest pool member
(metav4N, −92k margin), banks ~56-65k where every real agent banks 95-97k.
Not a crash (all DONE, no errors) — it simply earns ~2/3 of competitive agents.
Live trajectory agrees: 536.9 mid-convergence, below start.

Root cause per census: `agents/v8*.py` is the in-house v-series chassis with the
`sold_today`/`horizon` sell-suppression bug — a different codebase from r34-v8
(`subAC_v8`), which the submission descriptions misattribute. The in-family
ladder v8→v8w→v8x→v8hh is real (+47k vs agents/v8, 12-0, reproduced here) but
climbed **within a broken family**: even the base `agents/v8.py` goes 0-24
−120k vs m30b. Every own-v8 variant ever submitted (v8s 430, v8x 470, v8w 475,
v8 493, v8hh 537) is mid-convergence below start rating.

## 4. Pair math

Slot value = P(candidate lock rating > m30b lock rating). Under best-of-two a
weak slot-2 costs nothing but contributes nothing.

| option | slot-2 | P(>m30b at lock) | basis |
|---|---|---|---|
| current | v8hh | **≈0** | 0-120 local, live ~537 sinking |
| swap | **subAC_v8** | **~10-25%** | only candidate beating m30b locally (14-10); calibrated 2048.5 conv 09-28 (m30b 2220.6 same era); ACv8 also beats the whole tape-archetype pool (59-21 vs harvest/C1R2/shepherd/f55rec/metav4) |
| swap | v8p | ~10-25%, higher variance | locally strongest r34 (10-6 vs m30b, 13-3 vs ACv8) but live read truncated at 1696 mid-convergence — unproven ceiling |
| swap | harvest | ≈0 | same chassis as m30b minus BRX2/_CA — strictly dominated AND fully correlated failure modes |
| swap | shepherd/C1R2/f55rec/metav4 | ≈0 | lose to m30b; decayed/stale convergence reads (2091/1840/1930/…) |

**Decorrelation** (why r34-v8 is the right hedge shape): autopsy lane shows m30b
loses 2-12 to same-chassis+overlay variants while winning pure mirrors 28-9 —
its failure is being out-traded by better sell-timing on the same tape skeleton.
r34-v8's documented failure is the opposite — it drops ~25% vs weak/erratic
anchors (book-forecast breaks on noise) while beating every tape-archetype
candidate here. Different weakness, different opponent slice. A field shift
toward strong variants hits m30b and leaves ACv8; a weak field leaves m30b's
tape grinding fine.

## 5. Mechanics caveat (decision-critical)

Eviction is by age: the next upload evicts **m30b** (06:05), not v8hh (12:52).
Replacing v8hh therefore costs BOTH remaining slots and resets m30b:
`upload subAC_v8.py` → pair [v8hh, ACv8′]; `upload subAB_m30b.py` → pair
[ACv8′, m30b′]. Both restart ~600 with ~5-6h to lock (~50-70 eps; m30b took
~7h/87 eps to reach 1735 today). Fresh-pair E[max] ≈ 1800-2000 vs keeping
m30b's accumulated climb ≈ 2000-2200. A single upload of ACv8 alone leaves
[v8hh, ACv8′] — evicts m30b, keeps the dead slot, strictly worst.

## 6. Recommendation

**Keep [m30b, v8hh] as default.** No candidate beats m30b except the r34-v8
family, and installing it costs m30b's 87-game convergence for a hedge that
cannot finish converging by lock — expected EV −150 to −300 vs keeping.

**If a swap is made anyway** (e.g., decision weights tail-decorrelation over
EV, or m30b's live trajectory visibly stalls below ~1900): upload
`subAC_v8.py` then `subAB_m30b.py` → final pair [ACv8′, m30b′].
subAC_v8 over v8p for the proven 2048 ceiling; v8p only if local strength
outweighs calibration.

**Never spend the slots on** harvest (m30b's own chassis — correlated),
shepherd/C1R2/f55rec/metav4 (lose to m30b, stale/decayed reads), or any
own-v8 file (v8hh included — the family is locally falsified, 0-120).

## Commands (repro)

```bash
# phase 1: candidates vs m30b, 12 seeds x2 seats (168 eps)
.venv/bin/python moe/r9/build/matrix/run_matrix.py \
  --pairs "subAB_m30b.py:agents/v8hh.py,subAB_m30b.py:subAA_harvest.py,subAB_m30b.py:subV2_f55rec.py,subAB_m30b.py:subZ_C1R2.py,subAB_m30b.py:subAC_v8.py,subAB_m30b.py:subW_shepherd.py,subAB_m30b.py:subN_metav4.py" \
  --seeds 9300-9311 --workers 4 --out moe/r9/build/matrix/results.jsonl
# phase 2: 7-agent RR, 8 seeds x2 seats (336 eps)
.venv/bin/python moe/r9/build/matrix/run_matrix.py --pairs "<21 pairs>" \
  --seeds 9312-9319 --workers 4 --out moe/r9/build/matrix/results.jsonl
# suppl: agents/v8 + v8x vs m30b; v8hh-vs-v8 + v8hh2-vs-m30b; v8p/v8p2 vs {m30b,ACv8}
# (same runner, smaller seed ranges — see results.jsonl for exact sets)
.venv/bin/python moe/r9/build/matrix/analyze.py moe/r9/build/matrix/results.jsonl
.venv/bin/python moe/r9/build/matrix/rank.py    moe/r9/build/matrix/results.jsonl
```

Caveats: local H2H ≠ live rating (field composition drives convergence — see
census/autopsy lanes); margins vs m30b suppress candidate banks since market is
shared (candidates' ~96k is vs the strongest opponent). Partial seed coverage
for v8p/v8p2/v8hh2 (8/12 seeds, n=16/12) — treat those margins as indicative.
