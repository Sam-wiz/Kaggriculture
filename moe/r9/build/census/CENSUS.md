# MoE r9 — ARTIFACT CENSUS + EVIDENCE TABLE (lane `census`, ~14:15 UTC)

Sources: `kaggle competitions submissions kaggriculture -v` (50 data rows), repo file
enumeration, moe/r3-r9 threads + HANDOFF.md. **Era ruler:** subK2_pipe16 resubmit
converged **1786** vs subK's 2787 (freshness window dead); f55rec 2552→1930,
2489→1793. Any score earned ≤09-27 is inflated ~400-1000 vs the current field.
Only 09-28+ convergences are current-era reads.

## ⚠ CRITICAL FINDING — two different "v8" chassis share one name

| | **own-v8 chassis** (40KB) | **r34-v8 chassis** (83KB) |
|---|---|---|
| file | `agents/v8.py` (+ variants) | `rivalsGH/r34l-rudr44_kaggriculture/agents_v8.py` = `subAC_v8.py` |
| arch | class-based "marginal-value task scheduler", pie-slice zones, `sell_orders(self)` w/ `sold_today`/`horizon` bug | functional market-book planner, `sell_orders(t, sells)`, no `sold_today` |
| provenance | agents/v1..v31 series, iterated since Sep 3 (NOTES.md:76 design doc); NOT byte-matched to any rivals*/ file | r34l-rudr44 GitHub, found 09-27 |
| submissions on it | **v8.py 56683242, v8s 56683236, v8w 56687244, v8x 56692930, v8hh 56707845** | **subAC_v8 56633475, v8p 56674116, v8p2 56674110** |

Proof the live "v8 family" is the 40KB chassis: the live d10-15 sell bug
(`q=ceil(total/horizon*bias)−already`, `sold_today` suppression) exists only in
`agents/v8.py`; `agents/v8w.py`=v8+5 lines, `v8x`=v8w+20, `v8hh`=v8x+142,
`moe/r7/build/devin/v8s.py`=v8+32. The submission descriptions' "r34l-rudr44 v8"
credit lines are **misattributed boilerplate** for v8s/v8w/v8x/v8hh (and likely
v8.py itself — "was sub 56633475" claim conflicts with file evidence; residual
uncertainty noted). Matrix lane: when a doc says "v8 vs m30b" check which file was
loaded — r34-v8 **beats** m30b h2h (~65-75%), own-v8 **loses** 0-24/0-48.

## Submission inventory (all 50)

| ref | file | date UTC | score | era | local path | family |
|---|---|---|---|---|---|---|
| 56707845 | v8hh.py | 09-30 12:52 | 536.9 mid | cur | `agents/v8hh.py` | own-v8+PROG |
| 56698987 | subAB_m30b.py | 09-30 06:05 | 1735.4 climbing | cur | `subAB_m30b.py` ≡ `moe/r6/build/devin/harvest_m30_brx2.py` | Harvest/m30b |
| 56692930 | v8x.py | 09-30 01:07 | 470.5 mid | cur | `agents/v8x.py` | own-v8 |
| 56687244 | v8w.py | 09-29 20:48 | 475.5 mid | cur | `agents/v8w.py` | own-v8 |
| 56683242 | v8.py | 09-29 17:26 | 493.2 mid | cur | `agents/v8.py` | own-v8 |
| 56683236 | v8s.py | 09-29 17:26 | 430.4 mid | cur | `moe/r7/build/devin/v8s.py` | own-v8+shop-herd |
| 56674116 | v8p.py | 09-29 11:47 | 1696.3 evict-mid | cur | `moe/r7/build/devin/v8p.py` | r34-v8+patch |
| 56674110 | v8p2.py | 09-29 11:47 | 1643.5 evict-mid | cur | `moe/r7/build/devin/v8p2.py` | r34-v8+patch |
| 56633475 | subAC_v8.py | 09-28 07:31 | **2048.5 conv** | cur | `subAC_v8.py` | r34-v8 |
| 56633341 | subAB_m30b.py | 09-28 07:27 | **2220.6 conv** | cur | `subAB_m30b.py` | Harvest/m30b |
| 56612454 | subAA_harvest.py | 09-27 15:17 | 2054.1 conv | cur-ish | `subAA_harvest.py` | Harvest |
| 56611551 | subZ_C1R2.py | 09-27 14:38 | 1840.8 conv | cur-ish | `subZ_C1R2.py` | shepherd+C1R2 |
| 56560349 | subY_C1_predict2.py | 09-25 21:18 | 1682.2 | stale | `subY_C1_predict2.py` | shepherd+C1 |
| 56551754 | subX_hyb2965.py | 09-25 13:29 | 1885.6 | stale | `subX_hyb2965.py` | shepherd-adj (V57+shiiin9) |
| 56549546 | subW_shepherd.py | 09-25 11:39 | 2091.4 | stale | `subW_shepherd.py` | shepherd |
| 56547613 | subK2_pipe16.py | 09-25 09:56 | **1786.4** = RULER | stale | `subK2_pipe16.py` | pipe16 |
| 56547525 | subV2_sir2.py | 09-25 09:52 | 1709.4 | stale | `subV2_sir2.py` | metav4+SIR |
| 56532595 | subV_sir2.py | 09-24 22:13 | 1890.4 | stale | `subV_sir2.py` | pipe16+SIR |
| 56531508 | subV2_f55rec.py | 09-24 20:58 | 1930.1 | stale | `subV2_f55rec.py` | metav4+f55rec |
| 56531504 | subV_f55rec.py | 09-24 20:58 | 1793.2 | stale | `subV_f55rec.py` | pipe16+f55rec |
| 56526468 | subV2_sirxL96.py | 09-24 16:33 | 2253.0 | stale | `subV2_sirxL96.py` | metav4+SIRX+L96 |
| 56495194 | subV_sirxL96.py | 09-23 13:55 | 2214.1 | stale | `subV_sirxL96.py` | pipe16+SIRX+L96 |
| 56489061 | subV2_sirxP.py | 09-23 09:09 | 2071.8 | stale | `subV2_sirxP.py` | metav4+SIRX |
| 56489058 | subV_sirxP.py | 09-23 09:09 | 2124.2 | stale | `subV_sirxP.py` | pipe16+SIRX |
| 56476666 | subV2_sir.py | 09-23 00:02 | 2304.6 | stale | `subV2_sir.py` | metav4+SIR |
| 56476637 | subV_sir.py | 09-23 00:01 | 1907.1 | stale | `subV_sir.py` | pipe16+SIR |
| 56465708 | subV2_f55rec.py | 09-22 13:27 | 2552.3 | ancient | `subV2_f55rec.py` | metav4+f55rec |
| 56465704 | subV_f55rec.py | 09-22 13:27 | 2489.2 | ancient | `subV_f55rec.py` | pipe16+f55rec |
| 56458087 | subV2_f55.py | 09-22 08:02 | 2397.7 | ancient | `subV2_f55.py` | metav4+f55 |
| 56458085 | subV_f55b30d10.py | 09-22 08:02 | 2207.8 | ancient | `subV_f55b30d10.py` | pipe16+f55 |
| 56455434 | subV_a.py | 09-22 06:18 | 2055.4 | ancient | `subV_a.py` | pipe16+prem |
| 56439429 | subV2_mvprem.py | 09-21 17:15 | 2405.7 | ancient | `subV2_mvprem.py` | metav4+prem |
| 56416380 | subOb_pipe16prem.py | 09-21 04:39 | 2685.7 | ancient | `subOb_pipe16prem.py` | pipe16+prem |
| 56416374 | subP2_metav4prem.py | 09-21 04:39 | 2601.9 | ancient | `subP2_metav4prem.py` | metav4+prem |
| 56416179 | subP_metav4prem.py | 09-21 04:29 | 845.9 evict-early | ancient | `subP_metav4prem.py` | metav4+prem |
| 56416177 | subO_pipe16clamprem.py | 09-21 04:28 | 776.6 evict-early | ancient | `subO_pipe16clamprem.py` | pipe16+clamp |
| 56407594 | subN_metav4.py | 09-20 23:10 | 2428.7 | ancient | `subN_metav4.py` | metav4+clamp |
| 56407588 | subO_pipe16clamprem.py | 09-20 23:10 | 2466.9 | ancient | `subO_pipe16clamprem.py` | pipe16+clamp |
| 56394286 | subL_metav4.py | 09-20 12:48 | 2311.6 | ancient | `subL_metav4.py` | metav4 |
| 56394147 | subK_pipe16.py | 09-20 12:43 | 2787.4 | ancient | `subK_pipe16.py` | pipe16 |
| 56366726 | subJ_2945.py | 09-19 17:13 | 2549.5 | ancient | `subJ_2945.py` | pipe-lineage V39+v9 |
| 56366720 | subH2_v48.py | 09-19 17:13 | 2271.0 | ancient | `subH2_v48.py` | V48 |
| 56331238 | subI_pipe7.py | 09-18 13:27 | 2107.4 | ancient | `subI_pipe7.py` | pipe7 |
| 56331236 | subH_v48.py | 09-18 13:27 | 2339.7 | ancient | `subH_v48.py` | V48 |
| 56268027 | subG_v44.py | 09-16 03:12 | 2212.3 | ancient | `subG_v44.py` | V44 |
| 56268024 | subF_v45.py | 09-16 03:12 | 2272.6 | ancient | `subF_v45.py` | V45 |
| 56250536 | subE_pipe2.py | 09-15 09:00 | 2505.9 | ancient | `subE_pipe2.py` | pipe2 |
| 56250532 | subD_v43.py | 09-15 09:00 | 2612.4 | ancient | `subD_v43.py` | V43 |
| 56159600 | sub_router2.py | 09-11 05:57 | 1520.5 | ancient | `sub_router2.py` | own router |
| 56159593 | sub_hover.py | 09-11 05:57 | 1400.5 | ancient | `sub_hover.py` | own hover |

## Local-only artifacts (never submitted)

| file | family | evidence |
|---|---|---|
| `agents/v8hh2.py` | own-v8+PROG(MMPQ tables) | 10-6 +1k vs v8hh (≈equivalent) |
| `agents/v8xs.py` | own-v8x+shop-herd | mirror vs v8x 14-18-16 (~-1%); lost to v8hh 3-13 |
| `agents/v8w2.py` | own-v8w+momentum | FALSIFIED 4-20 vs v8w |
| `agents/v8ws.py` | own-v8w+shop-herd | 17-27-4 vs v8w (−1832) — held back |
| `agents/v8m.py`/`v8m2.py` | own-v8+mission-commit | −46k / 40-40 wash — dead; 0-24 vs m30b |
| `moe/r8/build/prog/v8prog.py` | own-v8x+PROG layer | = v8hh pre-bake; hh 40-0 +27.5k vs v8x |
| `moe/r6/build/devin/harvest_m30b_p324.py` | m30b+324 streams | RR 2393≈2402 wash; ~97% outcome-identical — a copy, not a hedge |
| `moe/r6/build/devin/harvest_m30.py` | Harvest+_CA-30 | RR 2377 [2178,2538]; parent of m30b |
| `moe/r6/build/devin/harvest_m{15,18,26,34,38,42}.py` | _CA sweep | all ≤ parent — dead |
| `moe/r6/build/devin/harvest_m30b_{buf14,cash300,feed0,from4}.py` | knob sweep | all neutral/worse — knob space exhausted |
| `moe/r6/build/devin/harvest_qc.py` | Harvest+censor-Q | wash (Q dormant) |
| `moe/r7/build/devin/agents_v8_*.py` (rw0/rw25/lab6/rw0lab6/g6/g8/g6a26/g8a28/c14/hl6/hd4/d/brx2/dsm/dsmf/dsmf2/ssell/tom) | r34-v8 variants | ALL ≤ base r34v8 (12-variant sweep); brx2 graft +20 mean only |
| `moe/r7/build/devin/clone_{dsm,dsm_bc,bc_pool}.py`, `moe/r8/build/clonefix/clone_{dsm_bc2,nomlp}.py`, `moe/r8/build/devin/clone_mmpq{,_bc}.py` | clone class | FALSIFIED: ~1.7k–60k banks; 0-32 vs v8x, 0-8 vs m30b; six architectures dead |
| `subJ_2780.py`/`subJ_2802.py` | pipe-lineage | pool agents; m30b sweeps jaxa2802/melon2749/jaxa2780 20-0 |
| shepM1 (haideptry shepherd 09-29 update) | shepherd+EarlyCycle/WaterRepair | 2-22 vs m30b — dead; no stable archived file (rivals9 holds Sep-27 snapshot; layer text present inside subY/subZ) |
| `kaggriculture-island-ga`, exec3 genome lineages | RL/genome | chassis caps ~35k bank — 0/60 vs finalists (r7) |

## RR-map numbers (opus lineage anchors — retrodicts live)

M30B **2402 [2192,2562]** > p324 2393 ≈ > m30 2377 > Harvest **2329 [2160,2514]** > C1R2 **2152 [2021,2294]** > r34-v8 **2150 [2047,2229]** > rw25 2110 > C1 2076 > C1noV233 2058 > shepherd ~2100 > hyb2965 ~1990 > v5_evolve 1533. Guru-v4/tetsutani/lynn = 2285 [2136,2414] (public pool agents, unbuilt).

## Local h2h vs m30b (the decisive column)

| artifact | record vs m30b | notes |
|---|---|---|
| **r34-v8 (subAC_v8)** | **WON ~65-75%**: 19-1 (+8803, 97-seeds), 11-9/11-9 (+2.8k both seats), 15-5 (+6176 map seeds) | only agent that beats m30b locally; high seed-variance; still maps/lives LOWER (2150/2048) because it drops ~25% to weak anchors |
| **v8p2 (r34)** | **WON 16-4 +7090** | live-evicted early at 1643 — local win did NOT transfer |
| **v8p (r34)** | **WON 9-1 +8595** | live-evicted at 1696 |
| own-v8 (v8x/v8w) | 0-24, −110k..−87k | family cap — tape engine >> walker |
| v8hh | 0-48, −84.7k; live m30b vs v8hh ~+75k/g (matrix lane running: 177k vs 102k typ.) | closes ~25k of family gap, still zero wins |
| shepherd | 0-20 (m30b RR map) | |
| hyb2965 | 0-20 | |
| shepM1 | 2-22 | near-parity money, loses mirror margins |
| f55V2/sirV1/C1/C1R2 | 0-20/1-19/1-19/1-19 | m30b near-sweeps the whole anchor field |
| clone_dsm_bc2 | 0-8, −129.6k | falsified |

## Ranking by CURRENT-ERA intrinsic strength

1. **m30b** — only artifact with a converged ≥2200 current-era read (2220.6, 09-28); resubmit at ~1750+ climbing same trajectory. RR 2402. **The anchor.**
2. **r34-v8 (subAC_v8.py)** — 2048.5 converged 09-28; beats m30b h2h; different class; downside: maps lower, loses ~25% to sub-2000 anchors.
3. **Harvest (subAA)** — ~2050-2070 plateau; strict subset of m30b (same failure modes).
4. **shepherd (subW)** — 2091 on 09-25 (decay-adjusted ~1700-1900); the band is 80% its own clones — strong mirror identity but feeds the field it faces.
5. **v8p/v8p2 (r34)** — r34-class upside; live froze early ~1650-1700 (premature eviction).
6. **C1R2 (subZ)** — 1841 plateau, RR 2152.
7. **hyb2965 (subX)** — 1886 (09-25), outcome-corr 0.50 vs shepherd (least-correlated shepherd-lineage member).
8. **v8hh** — live 537 mid-flight (never converged); local bank ~117k vs m30b ~150-190k; ceiling below m30b, floor questionable (lost live to 540-658-rated off-meta agents).
9. C1_predict2 1682 / pipe16 1786 (ruler) / metav4-premium family ~stale-2400s → plausible 1700-2000 unproven.

## Shortlists

**Anchors (top ~8):** m30b · r34-v8 (subAC_v8) · subAA_harvest · subW_shepherd · v8p2 · v8p · subZ_C1R2 · subX_hyb2965. (v8hh = incumbent slot but strictly < m30b.)

**Hedges (top ~6, decorrelation-ranked):**
1. **r34-v8 (subAC_v8.py)** — only measured cross-class decorrelation: 0 overlapping failure seeds vs M30B (140 shared cells, phi −0.09); ~+142 EV in chassis-collapse world.
2. **v8p2** — same class + animal-investment patch (16-4 vs m30b); different live regime.
3. **v8hh** — different chassis entirely (walker+program); autopsy says its live losses are a different failure mode; but low floor.
4. **hyb2965** — different chassis, least-correlated of the shepherd-lineage (corr 0.50).
5. **subP2_metav4prem / subV2_sirxL96** — metav4 chassis, decorrelated from Harvest; stale-era 2600/2250 ≈ ~1700-1900 now.
6. **shepherd** — different executor, BUT the 2200-2600 field is its own clone band: it fails where m30b wins — hedge value questionable.

## Flags

- **≥2000-equivalent never tested vs m30b:** subV2_sirxL96 (2253@09-24), subV2_sir (2304.6), subV2_mvprem (2405.7), subP2_metav4prem (2601.9), subOb_pipe16prem (2685.7), subV2_f55 (2397.7) — all predate m30b; plausible ~1700-2000 post-decay but unproven. Cheap 10-seed screen if a slot is seriously considered — all are same-architecture market overlays, expected <m30b.
- **r34 agents_v7.py** went 9-11 (−58) vs M30B seat-0-only 20 seeds — near-parity single-read, plausible ≥2000-equivalent, untested both-seats. agents_v6: 6-14. Worth a look only if r34-class is revisited.
- **Strict supersets of submission files:** subAB_m30b ⊃ subAA_harvest (+_CA-30+BRX2); harvest_m30b_p324 ⊃ m30b (~97% identical outcomes); subZ_C1R2 ⊃ subY_C1_predict2 ⊃ subW_shepherd; subK2 = subK+comment; v8hh⊃v8x⊃v8w⊃v8(sub 56683242); v8xs⊃v8x, v8ws⊃v8w; v8p/v8p2 ⊃ subAC_v8; subN⊃subL (+clamp); sirx chain ⊃ sir2 ⊃ f55rec ⊃ f55 ⊃ {pipe16prem|mvprem} ⊃ {subK|subL}.
- **Credit mislabel:** v8s/v8w/v8x/v8hh submission text says "r34l-rudr44" — chassis is actually `agents/v8.py` (own v5-docstring scheduler); only mechanisms (tile_stay/standing-sell/PROG) are decoded from top teams. Cosmetic but relevant if file provenance is re-audited.
- **Every v8 submission was evicted mid-convergence** (430-537 frozen at 3-12h) — none has a converged live read. All "family cap" evidence is local + early-trajectory only.
- subL_metav4 ≡ guruprasaathas111 master-engine-v4 (md5-identical, per subL desc) = same code as rivals9/rivals7 guru_v4 files.
