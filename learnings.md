# Kaggriculture — post-mortem and learnings

Written 2026-10-16, after the final Bradley–Terry evaluation closed (14 Oct). Sources: our own
`HANDOFF.md` / `MISTAKES.md` / `moe/r*/`, the final leaderboard, and the public write-ups listed at the end.

## 1. Outcome

| | |
|---|---|
| **Final rank** | **479 / 10,148** (Kaggle `userRank`, after the final evaluation) — top **4.7%** |
| Medal zone | Silver cut (top 5%) ≈ rank 507 → **inside silver by ~28 places** (confirm the medal on the profile) |
| Final pair | `submissions_acv8_dup.py` (ACv8 — r34l-rudr44's GitHub market-book agent): public 2103.8 / private **4527**; `submissions_m30b_dup.py` (m30b — Harvest V78 chassis + BRX2 sell ordering + `_CA_MARGIN` 30): 1733.2 / 4329. **ACv8 set the team score.** |
| Best public rating ever | pipe16, 2843 peak / 2787 converged (09-20) |
| Winners | 1 M&M&P&Q 3314 · 2 Victor @ Tufa Labs 3260 · 3 DSM 3162 · 4 CDE 3063 · 5 DECEM 3054 · #10 ≈ 2932 |
| Effort | ~4 weeks (first submission 09-03), 50+ submissions, MoE rounds r1–r9 |

## 2. What the top teams did

Their write-ups and code are unusually consistent:

- **#1 M&M&P&Q** — post title: *"A preview of our solution: BC, Self-Play PPO, and Heuristics"* (msd0110; the post body
  is JS-only, so details are not verified here).
- **CarsonBurke (~10th–12th)** — behaviour cloning on hosted replays where both players were rated ≥2600 (only
  bit-exact-reproducible games), then **PPO self-play with a league of the hardest past snapshots**, terminal
  win/draw/loss reward, centralised critic, a **bit-exact Rust batched simulator**, **~10 h on one RTX 5090**.
  Per-unit + per-market-slot action heads with legality masks. Lessons: pretrain the critic, watch action
  distributions for collapse, prefer W/D/L over shaped rewards.
- **atsushi11o7 (top ~17)** — started on the SAME public tape kernels we used (hybrid2965, cha22). Their PR: those
  openings "diverged greatly from real top-player behaviour and scores stalled"; switching the opening to **BC on
  top-player replays "improved the score greatly"**. Then JAX simulator + PPO from day 12, with a state bank and
  BC models of MMPQ/DECEM/DSM/Vadim as league opponents; export the actor to PyTorch for submission.
- **A "7th place (currently)" preview** was also BC-based.
- **feel the agi (~2650–2700, mid-table)** — our architecture (recorded-opening library + reactive executor +
  CMA-ES). Their conclusions match ours word for word: own income isn't the score; *"selling is denial, holding is
  a gift"*; the top-3 run one integrated controller and *"bolting any piece of it onto a tape-plus-executor agent
  lost every single time… it has to be built as one thing."*
- **subramanya (LLM auto-research, heuristics)** — peaked 3056 live on 08-22, final upload 1648: optimising on a
  reused development panel produced small cash gains and new strategic losses.

**Bottom line: every team above ~2900 that published anything used a learned policy (BC → self-play PPO).
Every heuristic/tape lineage — ours included — plateaued around 2100–2700 once the field caught up.**

## 3. Where we went wrong (ranked by cost)

### 3.1 We never built a learned policy — the decisive miss
- Early in the competition HANDOFF reasoned *"this is supervised classification, not RL"*, citing the terminal-only
  reward over 719 turns and a weak public `pure-rl-agent-bc-ppo-self-play` notebook. The user asked *"why aren't we
  using RL?"* around 09-20; we stayed on tapes.
- Our first RL/BC attempts came on **09-29/09-30** (GRPO over macro genomes; a BC'd per-unit dispatcher; a
  DSM-program clone). They failed on closed-loop drift — exactly the problem PPO-after-BC exists to fix — with
  no time left to add the RL stage.
- We had every ingredient a month earlier: a bit-exact C++ simulator (kagsim), exact replay, the top replays, and
  local compute. CarsonBurke needed ~10 GPU-hours.
- **Cost:** the whole gap from silver to gold/top-10. Everything else below is second-order.

### 3.2 We ignored the best data source until the last 4 days
- Kaggle's **official daily top-episode dumps** (`kaggle/kaggriculture-episodes-YYYY-MM-DD`, ~600 games/day of
  ≥~2900-rated play, from **07-30**) were first pulled on **09-26**. That is the BC training set the winners used.
- The **Kaggle CLI can read the forum** (`kaggle competitions topics list|show|topic-messages`); we relied on manual
  dumps and an expiring browser cookie until 09-30.
- Full tape re-simulation (`actions[t+1]` answers `obs[t]`) was cracked at scale only on 09-30 (1128/1128 tapes
  bit-exact) — the off-by-one itself was known on 09-20.

### 3.3 Our evaluation instruments did not predict live results
- Public-pool round-robin: ranked shepherd #1 of 17 (0.841) → live ~2160.
- Open-loop replay substitution (opponent replayed as a frozen tape): predicted 0.656 vs ≥2200 → live ~0.2.
  Frozen opponents flatter any layer whose edge is pre-empting the rival (MISTAKES C18).
- Mirror/in-family gates: measured intra-family deltas only (v8hh "+20k" → 0-120 vs the real pool).
- The first instrument that retrodicted live ratings (Opus's lineage RR map anchored on 5 live-rated builds)
  arrived on **09-26**. Several slots and days went to candidates the old gates promoted.

### 3.4 We chased the displayed ladder and churned slots
- 10 submissions in 72 h (09-22→09-25); each restart sends a build back to ~600 and makes the display meaningless.
- We mistook field drift for a code regression (09-25: "revert to the pre-09-23 stack", refuted by paired
  replay the same day) and burned a slot on a pipe16 "control".
- Resubmitting historical bests (2609 → 1400, 2576 → 1520) — identical code converged ~250–400 apart.
- Staff had already answered in the forum (logged as HANDOFF 09-21a) that the final is one BT fit and the team
  score is the better of two agents; pre-deadline rating is only seeding.

### 3.5 We spent days grafting the top family's plan onto our tape chassis
- Tape replay (8/125), routers (0.24), TS/NN planners (3/32, 0/8), day-splicing (0/20 clean), macro options
  O1/O2/O3 (−$9k..−17k/g), clean-room clones (~45–60k vs ~110k), C1noV233 — all measured dead.
- Each kill was correct, but the series was predictable: macro without its executor does not transfer.
  feel the agi reached the same verdict independently.

### 3.6 Market behaviour: we held when we should have sold
- Our own `agents/v8.py` (not ACv8 — two different agents were both called "v8") had a sell meter that hoarded 31–57 premium units (−$10–15k/game, undermanned mid-game) — found 09-30.
- Several premium "hold for price" layers were net-negative against reactive opponents.
- Rating counts wins only; margin is invisible to BT. Denial (sell first) beats price optimisation.

### 3.7 Late discovery of public improvements
- The public pool kept moving AFTER the 09-23 sharing lock via notebook updates (Harvest Ledger V78 on 09-27 —
  the biggest single jump of the last week) and GitHub (ACv8, which set our final score).

### 3.8 Orchestration overhead
- Several concurrent sessions (Claude/Codex/Devin) submitting over each other (slot collisions, a 429
  mis-attributed as our upload); MoE debate rounds that replaced building; expert sessions dying mid-run and
  background jobs lost on restarts; shell footguns (zsh word-splitting, multiprocessing from stdin).
- None of these alone was large; together they cost days in the final two weeks.

## 4. What worked — keep doing this

- **Re-baselining onto the newest strong public base** produced every big jump (V48 → pipe16 2843 → Harvest →
  m30b). Sweep Kaggle notebooks AND GitHub daily until the deadline.
- **Paired, seed-matched closed-loop benchmarking** (paired sd ~$373 vs ~$8,000 unpaired).
- **Bit-exact replay and simulation**, with self-reproduction checks (a replay must reproduce banks to the dollar).
- **Pre-registering gates before seeing results**, and an instrument that **retrodicts live** before it may rank.
- **Final pair = best + most decorrelated**, chosen from a 640-game fresh-seed matrix (ACv8 + m30b: no overlapping
  failure seeds) — ACv8 carried the final.
- **Append-only HANDOFF / MISTAKES** and honest kills — they made every retrospective claim here checkable.

## 5. Playbook for the next simulation competition

1. **Day 1–2:** inventory every data source (official episode dumps, forum via CLI, public notebooks, GitHub);
   read the final-scoring rules and ask staff early.
2. **Week 1:** bit-exact fast simulator + exact replay + a paired evaluator anchored on live ratings.
3. **Week 1–2:** BC from top replays → closed-loop evaluation → **self-play PPO with a league** (pretrain the
   critic; W/D/L reward; per-unit + market heads with legality masks; monitor action distributions).
4. **In parallel:** keep the best public/heuristic base as the slot-2 anchor and re-baseline it daily.
5. **Gates:** an instrument earns trust only by retrodicting live results; use responsive (closed-loop) opponents.
6. **Slots:** one submitter; no churn for the displayed ladder when the final is a refit; final pair = best +
   most decorrelated.
7. **Market games:** count wins, not margin; sell to deny; never trust layers that only beat frozen tapes.

## 6. Sources

- Kaggle discussion: *[1st Place (currently)] A preview of our solution: BC, Self-Play PPO, and Heuristics* —
  https://www.kaggle.com/competitions/kaggriculture/discussion
- CarsonBurke — https://github.com/CarsonBurke/kaggriculture
- atsushi11o7 — https://github.com/atsushi11o7/kaggriculture (PR #21)
- feel the agi — https://github.com/amrrs/kaggriculture-feel-the-agi (WRITEUP.md)
- subramanya — https://subramanya.ai/2026/09/30/kaggriculture-autoresearch/
- BillXu21 — https://github.com/BillXu21/Kaggriculture · rangga-jakti — https://github.com/rangga-jakti/kaggriculture-agent
- rishijain07 — https://github.com/rishijain07/kaggriculture
