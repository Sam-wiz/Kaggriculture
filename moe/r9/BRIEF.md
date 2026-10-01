# MoE r9 — FINAL PAIR OPTIMIZATION (deadline round)

**Mission**: Determine the optimal 2-submission pair for final scoring lock (23:59 UTC today).
Upload cutoff: 18:00 UTC (~5h). Episodes keep running to lock — converged rating at lock = score.
Team score = BEST of the two live submissions.

**Current live pair**: `m30b` (sub 56698987, ~1750 and converging, previous convergence 2220.6)
+ `v8hh` (sub 56707845, ~537 mid-convergence — submitted 12:52 UTC).
**2 submission slots remain.**

## The optimization

Under best-of-two: slot value = P(agent's lock rating > anchor's lock rating).
- Anchor = highest converged intrinsic strength vs CURRENT field.
- Hedge = second-highest expected lock rating AND maximally decorrelated failure modes vs anchor.

Decay evidence (IMPORTANT — old scores are stale):
- subK2_pipe16 resubmit converged 1786 vs original's 2787 (freshness window dead)
- f55rec resubmits: 2552→1930, 2489→1793
- Only current-era convergence counts: subAC_v8 (verbatim v8) hit 2048.5 on 09-28;
  m30b hit 2220.6 on 09-28; current m30b resubmit ~1750 climbing.

## Lanes (write findings to `moe/r9/build/<lane>/FINDINGS.md`, post summary to `moe/r9/THREAD.md`)

### Lane `census` (read-only)
Build the complete artifact table. Sources: `kaggle competitions submissions kaggriculture -v`
(51 rows), `agents/`, `submissions*/`, `moe/*/build/`, `rivals*/`, root-level *.py.
For each: file path, family (v8-market-book / Harvest-m30b tape / metav4 / pipe16 /
shepherd / clone), evidence tier (live-converged+era / RR-mapped / gated-local / untested),
and measured result vs m30b if any exists in moe/*/THREAD.md or gate logs.
Deliver: `CENSUS.md` ranked by CURRENT-era intrinsic strength; shortlist top ~8 anchors,
top ~6 hedges. Flag any artifact never tested vs m30b that plausibly maps ≥2000.

### Lane `intel` (read-only)
Mine `discussions.md` (531KB, scraped ~Sep 27 20:20) for: private-agent mechanics,
interpreter exploits, market manipulation tricks, hire/weed/shop exploits, and any
"what we did" write-ups by high-ranked teams (sobameshi, MMPQ, DSM, DECEM, Victor@Tufa,
Joseph Adamski, lingxiaojun). Also attempt `kaggle` SDK discussions endpoint or note if
inaccessible — look for posts Sep 28-30 not in the archive (late reveals happen).
Deliver: `INTEL.md` — mechanism list with evidence + whether each is (a) already in our
agents, (b) patchable on m30b/v8hh in <2h, or (c) out of reach.

### Lane `matrix` (write ok)
Decisive local screen for the PAIR question. Using `harness.py` (.venv/bin/python):
1. Hedge-matrix: v8hh vs {harvest-file, f55rec-file, C1R2-file, subAC_v8-file, shepherd}
   and cross-pairs, ~10 seeds ×2 seats each. Locate actual files first (submissions dir
   or moe archives; names: subAA_harvest.py, subV2_f55rec.py, subZ_C1R2.py,
   subAC_v8.py, subW_shepherd.py — check `find . -name "sub*"`).
2. Anchor-check: any census shortlist item claiming ≥m30b gets 12 seeds ×2 seats vs m30b.
3. Output `MATRIX.md`: pairwise W-L + margins, and a recommended pair with the math
   (P(hedge > anchor) reasoning + decorrelation).
Skip artifacts that are trivially m30b-family (Harvest V78 IS m30b's chassis — same
failure modes, bad hedge even if strong).

### Lane `autopsy` (write ok)
m30b live-loss autopsy: use `kaggle competitions episodes 56698987 -v` + 
`kaggle competitions replay <id>` to identify WHICH opponent agents beat m30b in its
last ~40 episodes (replay JSON has agent names/descriptions). Check `mine/` tooling for
existing opponent-mining scripts. Classify losses: private-tier expected losses vs
avoidable losses (same-family, crashes, timeouts). Check `kaggle competitions logs` for
any m30b errors (timeout/exception = hedge-triggering failure mode).
Deliver `AUTOPSY.md`: loss taxonomy, opponent archetypes that beat m30b, and which
candidate hedge (v8hh-family vs metav4-family vs shepherd-family) best covers those
archetypes.

## Rules
- Fresh seeds only (900xxx+, avoid 7100-7119 which r8 used), BOTH seats, official env.
- No submission without explicit human approval. Gates in-writing before claims.
- Report by ~15:30 UTC. Decision ~16:00. Last safe upload ~16:30-17:00.
- Keep every gate command logged so it's reproducible.
