# MoE round 3 — Opus position (2026-09-25, 18:50–19:45 UTC)

**Short answer.**
- **Why shepherd and hyb2965 lose above 2200.** The 2200–2600 band is made of private edits of the same public agents we run. Our two live agents are verbatim public kernels, so they are the benchmark those teams tuned against.
- **Why both instruments fail.** They are built from public code and stale recordings, and that field no longer exists.
- **The single largest opponent group.** About 30% of our ≥2200 opponents run one identical, unpublished-to-us variant of the wonderful-life / yummers family (I call it **WLV**).
  - It beats us **11–3**, which implies it is ~**+225** stronger than our current agents (~**2400**).
  - It is ~$2k/game stronger than its public ancestor, which our agents beat 13–14/14 closed-loop.
- **The plan.**
  1. Get WLV's exact code, or rebuild it (it shares our tape byte-for-byte).
  2. Live-test it in a probe slot.
  3. Use both slots freely until 09-30 12:00. The final Bradley–Terry fit uses post-deadline games only, so pre-deadline churn costs nothing.
- **Instrument.** Exact-opponent closed-loop replay reproduces live margins **to the dollar (2/2)**. Proxy-by-public-ancestor **fails** retrodiction (1/11 sign agreement), so it is out.

Scratch scripts and outputs are in `/tmp/opus_r3/` (I was told to write only this file). Everything used ≤2 workers and ~30 CPU-min.

---

## 1. Diagnosis (checked evidence)

**Data.** 164 of our live episodes (shepherd 88, hyb2965 76), fetched 09-25 ~18:50 UTC into `mine/opp/`. They are rated against `moe/r3/lb_0925_1612.json`. I identified the build from the step-1 order: shepherd opens `BUY_PRODUCT WHEAT 8`, hyb2965 opens `WHEAT 20`, verified by running both agents.

### E1 — Live strength vs the medal cutoffs

Rating is a maximum-likelihood fit (Elo-400) against the fixed snapshot.

| build | games | fitted rating | vs ≥2000 opponents | WR 2200–2400 | WR 2400–2600 | WR 2600+ |
|---|---|---|---|---|---|---|
| shepherd | 88 | **2171** | 2169 (n=66) | 0.25 (20), median −$187 | 0.17 (12), −$586 | 0/2 |
| hyb2965 | 76 | 2146 | **2211 (n=23)** | 2/3 | 1/2 | 0/2, −$18.5k |

**Cutoffs on the same snapshot (N = 10,008):**

| cutoff | rank | rating |
|---|---|---|
| bronze | 1000 | **2239** |
| silver | 500 | **2437** |
| gold (10 + 0.2%) | ~30 | 2813 |
| top-10 | 10 | 2923 |

- **Medal thresholds.** Kaggle's standard tiers for ≥1000 teams give those ranks. The forum confirms medals are awarded ("silver medal zone" line 318; "gold medal leaderboard" line 4813). I could not confirm the final team count used.
- **The gap.** Bronze is ~+30..+70 away, silver ~+230..+270, top-10 ~+750.

### E2 — The band is production clones that differ in the market layer

- All 37 opponents in 2200–2600 have unit-op identity ≥0.83 with us, mostly 0.97–1.00. (41 games ≥2200 in total: shepherd 34, hyb2965 7.)
- Their market ops agree with ours on only 53–97% of turns.
- **No band opponent is a verbatim public kernel except two.** I replayed each ≥2000 opponent against our recorded tape with every runnable library agent in its seat (603 of 635 loaded, including all 29 rivals7 lock-window kernels). The first divergence step identifies the agent.
  - Max Fofanov (2234) runs exact **hyb2965**, and beat shepherd −$196.
  - Konstantin Zorin (2412) runs exact public **metav4 v13**.

Shepherd's ≥2200 record by opponent family:

| opponent family | n | shepherd WR | median $ |
|---|---|---|---|
| **WLV** (wonderful-life opening, identical variant) | 9 | **0.11** | −806 |
| pipe16/hyb-opening family (diverge from hyb2965 / V57 at t=92–457) | 11 | 0.18 | −277 |
| shepherd derivatives (diverge from shepherd at t=91–400, a different step each) | 5 | 0.20 | −152 |
| unmatched opening | 5 | 0.40 | −73 |
| structural non-clones (≥2600, 0% identity) | 2 | 0.00 | −6,084 |

**Reading:**
- Shepherd loses to private edits of **itself**, of **hyb2965**, and of **WL**.
- Each shepherd derivative diverges at a different step. That is many teams each tuning a private edit of the kernel we run verbatim.
- A public kernel with 5 votes, posted days before the lock, is the sparring partner for every private tweak.

### E3 — WLV is one agent, it is new, and it is our biggest loss source

- **One agent.** In all 14 of our games against it (14 different teams), the opponent matches public `a-wonderful-life` / `yummers` / `2950-peak-farm` until **exactly step 53**. There hand 0 idles (PASS at 53–58, again at 84–91) where the ancestor harvests.
- **Not a kagsim artefact.** On the real Python engine the ancestor diverges at the same step. Shepherd reproduces that same live game exactly, both banks to the dollar.
- **Where the change comes from.** WLV's hand-0 schedule at t=52–92 is **identical to shepherd's and hyb2965's**. All seven files share a byte-identical tape blob (`_R108_DATA` md5 a4b4f66f…): WL×3, shepherd, hyb2965, pipe16, pipe16clamp.
  - So the change is a runtime layer that shepherd and hyb2965 carry and WL lacks.
  - Shepherd has ~60 more functions than yummers: `_y_controller`/`_y_agent_shopherd`, `herdsafe_*`, `rescue_agent`, `e402`, and others.
  - **WLV ≈ the WL market/opening wrapper plus the herd layer(s).**
- **Our record and implied strength.** We go **3–11** against it, mean −$546. That implies WLV ≈ our agents + 226 ≈ **2400**. Its teams' ratings are 2179–2562 (median 2391), which agrees.
- **It is new.** In the 09-23/24 recordings the replay instrument used, the WL-family opening was **28/318 (9%)** of ≥2200 games, and our builds went **17–11** against it. Now it is **12/41 (29%)** of our ≥2200 games (14 WLV games counting two at 2179–2189), and we go 3–11.
- **Checked: not a lock-kernel we missed.** I extracted and tested the three statma "herd-safe sale-window" kernels (they failed extraction on 09-25 but `submission.tar.gz` is on disk). They are shepherd-family: t=0 divergence from WLV, t=91 from shepherd derivatives.
- **Also checked:** I rebuilt Gluzdov's herd-safe-LB2700, 7-turn rescue and two-coins from their notebooks, and fingerprinted guru v4 and fieldcraft. None opens like WLV.

### Why both instruments failed

| instrument | failure | root cause |
|---|---|---|
| **Public-pool gate** | Ranked shepherd 1st of 17 | Contains only public agents. Beating public WL ancestors is easy: our agents beat them 13–14/14 on the exact WLV seeds, +$1.5–1.7k (§2). |
| **Replay-substitution** | Predicted shepherd 0.656 vs ≥2200 | Its corpus is the 09-23/24 field, where WLV was 9% and beatable, and it is open-loop. |

**Neither instrument contains the private deltas that make up today's band.**

**One-paragraph version.** We are running the two most-copied lock-window kernels, verbatim. The ~40% of the band that matters to us runs private edits of those same kernels, or of their WL cousin, tuned against them. We therefore converge to where the public kernel sits in its own derivative cloud: ~2150–2200. That is just under bronze.

---

## 2. Instrument proposal, and how it is validated against live

**Principle.** An instrument is only allowed to rank candidates after it **retrodicts our own live results** on the same games. Faithful replay of the recorded agent is not enough (C18).

### What I tested

| instrument | validation vs live | verdict |
|---|---|---|
| **A. Exact-opponent closed-loop.** Opponent identified by a full 719-step exact-prefix match; candidate plays it closed-loop on the recorded seed and seat (kagsim) | shepherd vs exact hyb2965 → **−$196 (live −$196)**; hyb2965 vs exact metav4 v13 → **+$1,124 (live +$1,124)**. Our builds also self-reproduce 4/4 under kagsim, both seats. | **VALID, bit-exact.** Coverage today is only 2/41 band games, and ~14/41 if WLV is obtained. |
| **B. Proxy by nearest public ancestor.** Longest-prefix library agent stands in for a private variant | 14 WLV games, 3 ancestors × 2 builds (84 games). **Predicted: our builds win 13–14/14, +$1.5–1.7k. Live: 3–11, −$546.** Sign agreement on own-build games: shepherd **1/11**, hyb2965 **1/3**. | **FAILS. Do not use.** The private delta is worth ~$2k/game here. |
| C. Public-pool gate (`moe/gate.py`) | Shepherd 1st of 17 (0.841) against live ~2170 | Fails (already known) |
| D. Replay-substitution (`moe/replay/subst.py`) | Predicted 0.656 against live 0.25 | Fails (already known). Keep only for self-reproduction checks. |

My first run of A on the metav4 game did not reproduce (+2,362). The cause was my own mistake: I picked `guruprasaathas…master-engine-v3`, which diverges at t=0, instead of the full-match file. Rerun with the correct file: exact.

### The proposal

1. **Refresh.** Every ~6 h, fetch our new live episodes (`mine/fetch_recent.py <subA> <subB>`).
2. **Classify.** Run exact-prefix matching (`/tmp/opus_r3/exact.py`, ~2 CPU-min per 40 games) and the family table (`/tmp/opus_r3/opps.py` + `opengroup.py`).
3. **Build the corpus.**
   - Every opponent with a full 719-step match joins the **exact closed-loop corpus** (`/tmp/opus_r3/closed.py`, ~5 s/game).
   - Every family with a rebuilt variant joins only after the rebuild passes two gates:
     - (i) it matches the recorded opponent's actions for ≥700 steps in ≥10 of that family's recorded games;
     - (ii) our live build, played closed-loop against the rebuild, reproduces the live outcomes: sign agreement ≥80%, and aggregate WR within ±0.10.
4. **Score candidates** only on that corpus, weighted by live family prevalence. Private families without code stay an explicit **unknown** mass, and only live can measure them.

**Validation against the existing live reads:**
- Done: shepherd and hyb2965 exact games (2/2, to the dollar).
- Still to do: the ancestor-proxy failure above is the negative control, and any rebuild must beat it.
- For sir / pipe16 / L96: run the same exact matching on their 09-23/24 corpus (`moe/opus/eps_index.json`, 318 ≥2200 games). The instrument must reproduce their exact-opponent games to the dollar and match their live WR on that subset. This is not done — CPU budget.

**Honest limit.** Instrument A can only cover opponents whose code we have. Today that is ~5% of the band. It becomes ~40% only if WLV is obtained or rebuilt. **Live remains the primary signal.** A is for pre-screening and for tuning against identified families.

---

## 3. Live-test protocol

**What the final ranking actually depends on:**
- Final ranking = one Bradley–Terry fit over the post-deadline window.
- Staff (discussions.md l.100): "we will continue allowing submissions to run episodes for two weeks … single Bradley-Terry Tournament".
- Forum and HANDOFF 09-21d: ratings reset to 600 at close. Only the two agents active at the deadline matter; the team is scored by the better of them.
- **So pre-deadline rating and convergence are worth ~0.** The "freeze 09-28 so the pair converges" rule (my round 2 included) is **withdrawn**.
- The binding constraints are **information** and the fact that **the final pair = the last two uploads**.

**Protocol:**

1. **Both slots are probes until 09-30 ~12:00 UTC.**
   - Shepherd's read is complete (88 games, 34 ≥2200, fit 2171 ±~65).
   - hyb2965 needs ~8 more hours to reach ~20 band games.
   - Both files stay on disk and can be re-uploaded byte-for-byte at the end at no cost.
2. **Space uploads ≥8 h apart.** Eviction is by recency, so each probe then lives ~16 h: preliminary read at +8 h, final read at +16 h. This allows ~2 uploads/day and ~8 probe reads before the final day.
3. **Read rule.**
   - Take one fixed LB snapshot per read and fit every arm against it by maximum likelihood, using ≥2000 opponents.
   - Report WR per family (WLV / shepherd-derivative / pipe16-family / unknown) next to the overall fit.
   - SE is ~±65 per arm at ~35 band games, so a single read only detects effects ≥~150. **Only probe candidates with a plausible ≥+150 effect.** Whisker layers (BRX2, delivery: +20–35) are not live-testable in the time left.
4. **Kill rule.** At +8 h, if the fit vs ≥2000 is below shepherd −100 and WR vs WLV is ≤ shepherd's, replace the probe at the next upload.
5. **Final window.**
   - 09-30 ~08:00 UTC: upload the hedge.
   - 09-30 ~12:00 UTC: upload the best-measured agent.
   - The final pair is **the best-measured agent + the best agent from a *different* family**.
   - Run `kaggle_load_check` and confirm one validation episode for each before 18:00. No uploads after 18:00 except crash replacement.
6. **Never** upload two probes within 8 h of each other (the second evicts the first unread). Never re-upload an identical file to "re-roll".

---

## 4. Ranked candidates

| # | candidate | expected gain | confidence | hours | kill test |
|---|---|---|---|---|---|
| 1 | **WLV, exact.** Pull the newest versions of the WL family (see note A) and run `exact2.py` on the 14 WLV games | ~**+225** (3–11 head-to-head; teams median 2391) → ~2350–2420 live | Strength: medium. Finding a public exact copy: **~45%** | 0.5 (orchestrator) + 16 live | No full 719-step match on ≥10/14 games → go to #2 |
| 2 | **WLV rebuilt** (see note B) | Same target. Partial reproduction may keep most of the ~$2k delta | Medium-low: ~50% to reach ≥700-step matches in ≤6 h | 4–6 build + 16 live | After 6 h, median first-divergence <400; or shepherd-vs-rebuild wins >5/14 (fails retrodiction) |
| 3 | **Keep hyb2965 as the hedge; decide on its read.** It is the only one of our two with a fit ≥2200 vs ≥2000 opponents (2211, n=23) | 0 now. It could be the bronze carrier if it holds ≥2240 at 20+ band games | Medium | 0 | Fit <2150 at ≥20 band games → shepherd or the best probe becomes the hedge |
| 4 | **WLV + band-tuned sell order.** Once #1 or #2 exists: BRX2-style best-response, tuned **only** on the exact closed-loop corpus (WLV mirrors, exact hyb2965, exact metav4 v13) | +20–60 over WLV | Low | 4–8 | Must be ≥ +$150/g paired vs WLV-itself on the exact corpus; otherwise ship plain WLV |
| 5 | Everything else measured so far: BRX2, delivery/capture, koshinm cell, other lock kernels | ≤+35, invisible to valid instruments | — | — | Not probed |

**Note A — orchestrator pull for #1:**
- Pull `romantamrazov/kaggriculture-yummers`, `haideptry/the-2950-peak-farm`, `hanifnoerrofiq/a-wonderful-life`, and `leoprovorov/a-song-of-ice-and-fire*` (version from 09-25 already ruled out).
- Search kernels for yummers / wonderful / peak farm / herd-safe / shepherd published 09-18..09-23, including forks by the WL authors.
- `data/kernels.json` has `last_run=null` for all four family kernels. That is why a date-filtered lock pull would miss a newer version (Codex flagged this in round 2).

**Note B — rebuild for #2:**
- Everything shares the tape blob, and WLV = WL wrapper + shepherd's herd layer(s). Start from `rivals4/kaggriculture-yummers/_entry.py` and graft shepherd's extra layers one at a time, in shepherd's wrapper order.
- Keep WL's opening and market wrapper; do not graft shepherd's `opening_liquidity_agent`, because WLV opens like WL.
- Objective metric: mean first-divergence step vs the recorded WLV actions on the 14 games (`/tmp/opus_r3/exact2.py name=path`). Bisect layers until t=53–58 and 84–91 match, then continue.

**Why #1–#2 is the right bet:**
- It is the only candidate with (a) direct live evidence of beating our exact agents 11–3, and (b) independent evidence (14 teams' ratings) of ~2400 against the whole band.
- It also moves ~30% of the band from "unknown private" to "exact code". That makes instrument A useful, and #4 is then tunable.

**Failure risks:**
- **Selection.** The 14 games are all against our public builds, which WLV may have been tuned against. Its fit vs the whole field may be nearer 2300 than 2400; team ratings are max-of-two, biased up.
- **Copy dynamics.** Running it verbatim makes us one more clone of an agent others will now counter (the same trap as shepherd), though with 4 days left that drift is limited.
- **Late fielding.** If neither #1 nor #2 lands by 09-28 12:00, we field [hyb2965, shepherd] and expect ~2170–2210.

---

## 5. The next 12 hours (19:45 UTC 09-25 → 07:45 UTC 09-26)

1. **Orchestrator, now, ~30 min: note A.**
   - Pull the WL-family kernels, extract to `rivals8/`, then run:
     `nice .venv/bin/python /tmp/opus_r3/exact2.py 2150 wlA=<path> wlB=<path> …`
     (it reads `/tmp/opus_r3/opps_c.json`; copy `/tmp/opus_r3/` to `moe/r3/opus_scratch/` first — /tmp is not durable).
   - Full match on ≥10/14 → verify closed-loop: shepherd vs WLV on the 14 seeds must lose ~11 (retrodiction). Then `kaggle_load_check` and upload, evicting shepherd.
2. **Builder, in parallel, 4–6 h, ≤2 workers: note B** (the WLV rebuild), stopping as soon as #1 succeeds.
   - At 6 h, upload only if all three hold:
     - median first-divergence ≥600;
     - shepherd-vs-rebuild ≤5/14 on the WLV seeds;
     - the rebuild beats both shepherd and hyb2965 closed-loop on the exact corpus plus 24 fresh seeds.
3. **Leave hyb2965 running** (do not upload a second probe within 8 h of the first).
4. **~01:00 and ~07:00 UTC:** fetch episodes for both active submissions and redo the family table and fits against one fresh LB snapshot. Watch WLV prevalence and our WR against it: they are the leading indicator.
5. **Log in HANDOFF (append-only):**
   - (i) the ancestor-proxy instrument failed retrodiction — MISTAKES C19 candidate: *"a public ancestor is not a proxy for its private descendant"*;
   - (ii) the "freeze for convergence" rule is void under the post-deadline BT.

If nothing from #1/#2 is ready by 07:45 UTC: **no upload.** Hold [shepherd, hyb2965] and continue #2.

---

## 6. What to stop

- **Stop gating on anything built only from public agents.** That covers `moe/gate.py` and ancestor proxies: both fail retrodiction. The public pool orders public agents, and the band is not public agents.
- **Stop replay-substitution as a gate.** Keep it only as a self-reproduction and bit-exactness check.
- **Stop building overlays measured against public opponents** (BRX2, delivery, capture, koshinm-cell tuning). They are ≤+35, below live resolution, and have no valid instrument. Resume only as #4, tuned on the exact corpus.
- **Stop the convergence freeze and stop reading the displayed LB.** Final standing uses post-deadline games only. Pre-deadline churn is free; information is the only asset. Use fixed-snapshot fits.
- **Stop treating verbatim public kernels as final candidates by default.** Shepherd, hyb2965 and metav4 v13 are the reference every private tweak was tuned to beat. The one exception is WLV: it is widely run, but it is the variant that *won* that tuning race.
- **Stop spending effort on top-10.** Nothing measured gets within ~500. The rational objective is the medal line.

**On P(bronze):**
- Rests on the WLV branch (~50% to field an exact or near-exact copy; ~80% bronze if fielded).
- Otherwise on hyb2965's read (~28% bronze if it stays our best).
- The final field and cutoffs will shift post-deadline (rank-1000 fell 2296 → 2239 in 44 h). I did not model that drift.

**P(top-10): 0.3%  P(silver): 10%  P(bronze): 50%**
