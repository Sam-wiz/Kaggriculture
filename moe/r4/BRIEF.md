# MoE r4 brief — 2026-09-26 ~05:30 UTC. Deadline 2026-09-30 23:59 UTC (upload hard stop 09-30 18:00).

Experts (all xhigh): **Opus 5.5 (decode), Opus 5.5 (build, "opusb"), Sonnet 5.** Fable removed at user request. Codex astra/sol are usage-capped until
~09-27 21:53 UTC and may join later. Claude Code orchestrates, participates, holds the only Kaggle
credentials, and uploads. **You cannot submit.** Machine: 8 cores / 8.6 GB shared — **max 2 worker
processes each**, nice 10. Write only under `moe/r4/` (your .md) and `moe/r4/build/<you>/`.

## The user's three questions (all experts address all three; each owns one lane)
1. **How do we move to 3k+?** (top ~5; #10 = 2899, #500 = 2409 silver, #1000 = 2211 bronze today)
2. **Decode all top-10 episodes, reverse-engineer their games, and build a submission from them.**
   Think explicitly about HOW to reverse-engineer a game: what is recoverable from a replay (full
   action streams both seats, seed, final banks, shop draws; exact engine replay gives every fill,
   price, stock, cash at every tick) and what is not (their code, their reaction to states never seen).
3. **Build a submission for the PRIVATE field that can beat it — decode the private agents so the
   public pool can't fool us again.** Our offline gates failed twice because they used public agents
   (moe/gate.py) or frozen tapes (moe/replay/subst.py). An instrument must RETRODICT live results
   before it may rank anything (MISTAKES C17, C18).

## Lanes (own one, critique the others in round 2)
- **Opus 5.5 — decoding (Q2 method + Q3 instrument).** Per top team: farm plan (land order/timing,
  crops/plantings by day, herd size/timing, hires/day), market policy (what/when/how much they sell,
  price index captured, buy-backs), variance across games (tape vs reactive: does the plan change
  with shop draw / opponent?), and a replay-driven "private proxy" opponent per team. Validate by
  retrodiction: proxy(team X) vs proxy(team Y) must reproduce their recorded head-to-head outcomes.
- **Opus 5.5 #2 ("opusb") — build (Q2 submission + Q3 submission).** From the decoded top-10, build a candidate
  that plays like the best of them (e.g. shop-conditioned router over top-team tapes with a runtime
  executor/repair, or port the decoded production/market policy onto our C1 chassis), and a candidate
  tuned to beat the decoded private proxies. Gate against the proxies that passed retrodiction +
  closed-loop vs our live builds.
- **Sonnet 5 — strategy/red team (Q1).** What realistically reaches 3k (+~900 from hyb2965's 1974 /
  C1's early read)? What separates 3000+ agents from 2800-2900 ones in the dump (head-to-head among
  top teams)? Attack the other two lanes' assumptions; own the live-test protocol for 09-26..09-30.

## Data (Claude Code is filling it now)
- **`mine/top10/<ep>.json.gz`** — Kaggle's official daily dumps of top-rated episodes
  (`kaggle/kaggriculture-episodes-2026-09-2{3,4,5}`, ~576-620/day, median player ~2970). Streaming in
  (~2 h/day; progress `mine/fetch_epindex.log`). Fields: episode_id, date, seed, teams, rewards,
  agents, shops150, shops (final), actions ([seat0, seat1] per step; **actions[t] is the action that
  PRODUCED step t — the reply to obs t is actions[t+1]**).
- Older top replays: `mine/top/`, `mine/rawtop/`, `mine/top3/`; features dataset `meta/`.
- Our live games: `mine/opp/` (ids in `moe/r3/live_episode_ids.json`; C1 = sub 56560349 being fetched).
- LB snapshot 09-26 05:00 UTC: `moe/r3/lb_0926_0500.json`.
- Engine `.venv/.../kaggle_environments/envs/kaggriculture/kaggriculture.py`; kagsim bit-exact C++
  sim; replay idioms in `moe/opus/ledger_eps.py`, `moe/replay/subst.py`, `moe/r3/opus_scratch/`.

## Known facts / traps (verify, don't re-litigate)
- Live pair: **hyb2965** (sub 56551754, 1974, 139 games) + **C1** (sub 56560349 = shepherd + PREDICT2
  forecaster with 456 post-lock rival streams; 1542 at 65 games but 56-9, fed <1500 opponents; 4-4 vs
  >=2000). Every public-lineage agent converges 1.8-2.2k live; top is private.
- **Weed/shop RNG coupling**: one RNG draw per EMPTY tile; the shop draw depends on both farms'
  empty-tile counts. Changing either farm's tile plan re-rolls future shops -> a replayed tape is only
  valid while the shop sequence matches (check `shops`). Syed Asad Ali's landmine: re-rolled shops
  flatter the substitute (78% vs 40%).
- Tape replay of someone else's stream recovers ~88% of the owner's score (nofreewill42); our own
  mined-tape router measured -0.586 WR (09-20, HANDOFF §5). Understand WHY before proposing tapes.
- PREDICT (rival-sale forecast from a stream library) is worth +$1.3k/g closed-loop (r3 Opus E-A);
  libraries containing the opponent family's streams arm it (dose-dependent, unsaturated).
- Final standing = static Bradley-Terry fit (probably post-deadline games only); pre-deadline rating
  ~worthless; uploads >=8 h apart; last two uploads (09-30 ~08:00/14:00 UTC) = final pair.
- Read: HANDOFF.md from `## 09-25d` to end; MISTAKES.md C14-C18; `moe/r3/*.md` (esp. opus_r2, fable_r2,
  build/opus/RESULT.md).

## Deliverable (round 1)
`moe/r4/<you>.md` (opus.md / opusb.md / sonnet.md): 1 answers to Q1-Q3 from your lane with checked
evidence; 2 your method for reverse-engineering a game (concrete, tested on at least a few dump
episodes); 3 what you built or will build, with its gate and retrodiction test; 4 next 12 h;
5 `P(3k+)`, `P(top-10)`, `P(silver)`, `P(bronze)`. Report failures honestly. Round 2 = cross-exam.

## ADDENDUM — Jev (TypeSafe System One) available as an OPTIONAL offline triage tool
`from moe.tools.jev import ask` (see the file's docstring; run from the repo root). Returns calibrated
probabilities for typed questions (choice / score / noul) about a TEXT state, ~250 ms/call. It does
NOT generate text, cannot learn from examples (zero-shot only), and cannot be used inside a Kaggle
submission (no network there). Good for: labelling hundreds of top-10 games by family from a short
summary, flagging reactive-vs-tape behaviour, ranking which losses deserve a full engine autopsy.
Anything decision-relevant must still be verified by exact engine replay. Keep calls modest (a few
thousand total); never print or log the key.
