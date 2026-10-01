# MoE round 3 brief — 2026-09-25 19:00 UTC. Deadline 2026-09-30 23:59 UTC (~5 days).

Participants: Codex gpt-6-astra xhigh, Claude Opus 5.5 xhigh, Claude Code (orchestrator AND
participant; writes its own position before reading yours). Three rounds: independent positions
-> cross-examination -> decision. **You have no Kaggle credentials and cannot submit.**
Machine: 8 cores / 8.6 GB shared by all participants — **max 2 worker processes each**.

## Where we are (verify from files; do not trust this summary blindly)
- Team 2090, **rank 1359 / 10,008**. #10 ~2915, #100 ~2666, #500 ~2437, #1000 ~2239.
- Live pair (frozen since 09-25 13:30): **shepherd** (`subW_shepherd.py`, 2100 @89 games, implied
  ~2160; WR 0.95 <2000, 0.59 2000-2200, **0.27 2200-2400, 0.15 2400+**) and **hyb2965**
  (`subX_hyb2965.py`, 1921 @77 games, still converging, ~2135 implied on 47 games).
- Every public-lineage agent measured live since the 09-23 share lock converges **1.8-2.2k**
  (sir, f55rec, L96, sirxP, pipe16, shepherd, hyb2965). Nathan Jacob (pipe16's author) runs a
  private agent at ~2460 (rank ~438). The top is private reactive/RL agents.
- Read HANDOFF.md from `## 09-25d` to the end, MISTAKES.md C17-C18, and `moe/strat/*.md` (the
  previous MoE — do not rerun its arguments; build on them).

## Two instruments have FAILED to predict live results — this is the core problem
1. `moe/gate.py` (round-robin vs public agents): ranked shepherd 1st of 17 (0.841).
2. `moe/replay/subst.py` (recorded post-lock games, opponent open-loop): shepherd WR 0.656 vs
   >=2200, z=3.28. **Live: ~0.2.** Why: stale opponents (teams replaced agents after the lock) and
   frozen opponents cannot react to layers that pre-empt/anticipate their sells.
Live is currently the ONLY trustworthy signal, and it is slow: ~6-12 h and 40-80 games before a
build reaches the 2200+ band where the read is informative.

## Objectives (in order)
1. P(top-10) — flat $5k prizes. Honest priors from the last MoE: 1-4%.
2. **Medal**: for ~10k teams Kaggle's usual thresholds are bronze = top 10% (~rank 1000, ~2240 now),
   silver = top 5% (~rank 500, ~2440). Verify these thresholds if you can from the repo/forum dump
   (discussions.md) before relying on them. We are ~150 below bronze.
3. Final standing = Bradley-Terry refit on post-deadline games between each team's two active
   agents; team = better of its two. Only the LAST TWO submissions count; each upload evicts the
   OLDER active one. ~5 uploads/day. New uploads restart at ~600.

## Resources
- Every public agent: `rivals*/` (rivals7 = the 09-21..09-25 lock-window pull, 29 runnable).
- Live replays of our games (`live_eps/`, `mine/`), incl. vs the 2200-2900 band; `mine/fetch_ours.py`.
- Top-11 replays (`mine/top*`), georgymamarin episode features (`meta/`).
- kagsim C++ bit-exact simulator (`data/donors/` / destbreso cppsim) for fast search.
- The engine source (`.venv/.../kaggriculture/kaggriculture.py`).

## The question
With ~5 days, live as the only reliable signal, and a ~150-point gap to bronze / ~800 to top-10:
**what is the plan that maximises P(medal) and P(top-10)?** Address explicitly:
(a) **An instrument that predicts live.** Can we build one from live episodes (e.g. use our 2200+
    losses as the target: which candidate would have won THOSE games, closed-loop against the
    opponent's agent where we have its code, or reactive opponent models where we don't)? How
    would you validate it against the live reads we already have (shepherd, hyb2965, sir, pipe16)?
(b) **A live-testing protocol** that uses the 2 slots and ~5 uploads/day without losing our best
    anchor (eviction is by recency — design around it) and reads results fast enough to act.
(c) **Candidates with real upside**: what, concretely, beats the 2200-2400 band that shepherd loses
    to? Look at who those opponents are and what they run (replays + fingerprints). Reactive
    replanning, opponent-conditioned sell policy, a different public base, anything — with the
    evidence and the failure risk.
(d) What to STOP doing.

## Deliverable
Write ONLY `moe/r3/<you>.md` (codex.md / opus.md). Sections: 1 diagnosis (with checked evidence),
2 instrument proposal + how it is validated against existing live reads, 3 live-test protocol,
4 ranked candidates (expected gain, confidence, hours, kill test), 5 the next 12 hours,
6 what to stop. End with `P(top-10): x%  P(silver): y%  P(bronze): z%`.
You may run small analyses (<= 2 workers, <= ~45 min CPU). Report failures honestly.

## ADDENDUM 19:30 UTC — new data on disk (fetched by Claude Code; you cannot fetch)
- **All live games of the current pair**, compact format (`episode_id, seed, teams, rewards, actions`;
  `actions[t]` is the action that PRODUCED step t, so the reply to obs t is `actions[t+1]`):
  `mine/opp/<episode_id>.json.gz`. Episode id lists: `moe/r3/live_episode_ids.json`
  (key 56549546 = shepherd, 89 games; 56551754 = hyb2965, 77 games).
- Leaderboard snapshot 09-25 16:12 UTC, team -> score: `moe/r3/lb_0925_1612.json` (10,008 teams).
Use these for (a) and (c): shepherd's 2200+ losses are the target set.

## ADDENDUM 2 (20:10 UTC) — Codex hit its usage limit; replaced by Claude Fable 5.1 xhigh (writes moe/r3/fable.md).
Claude Code's own identification result (`moe/r3/identify.py`, pilot 5 clone games x 32 candidates):
**no public agent we hold reproduces any clone exactly** — best 0.74-0.90 action match, all diverge at
step 0-1. The band's "clones" are shepherd/pipe16-family farm plans with PRIVATE market openings/overlays.
