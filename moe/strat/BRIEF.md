# Strategy MoE — "from our max to 3k+", Kaggriculture, 2026-09-25

Two independent experts (Codex gpt-6-astra xhigh, Claude Opus 5.5 xhigh) answer the SAME question
without seeing each other's work. Claude Code synthesises. **No Kaggle submissions; you have no
credentials.** This is a strategy task: reading, analysis and small targeted checks — NOT a long
build/benchmark campaign. If you run simulations: `--workers 1`, keep them under ~20 minutes total;
two build experts are already using the machine (8 cores / 8.6 GB).

## The question
Our best-ever live agent is `subK_pipe16.py` (public nathanjacob pipe16): converged 2787, peak
2843, on 09-20. Top-10 cutoff today ~2940; 3k+ is roughly top-5. Deadline 2026-09-30 23:59 UTC
(5 days). Final standings = Bradley-Terry refit over post-deadline games; team = better of its two
active agents; prizes flat $5k for ranks 1-10. **What is the most credible path to a 3k+ agent in
5 days — and if there isn't one, what maximises P(top-10)?** Be concrete and quantitative.

## Facts you must account for (verify anything you rely on)
- Submission history (50 subs, `kaggle`-exported in HANDOFF 09-25f): builds submitted <=09-22
  converged 2.4-2.8k; every build from 09-23 on converged 1.8-2.3k (all carry rec+reclaim, most SIR).
  A live control (exact pipe16, ref 56547613) was resubmitted 09-25 09:57 UTC to separate
  "our regression" from "field drift after the 09-23 share lock". Result pending.
- Offline gate `moe/gate.py` plays PUBLIC agents only; it ranked vanilla pipe16 7th of 9 while
  live pipe16 is our best ever. Treat offline-vs-public results as weak evidence of live strength.
- Opus build-expert (moe/opus/NOTES.md): 197 replayed games vs 2400-2900 opponents — they are
  production clones of us (same wheat/herd/hires/land); 74/118 losses within $1k, median loss
  ~-$200; money lost in ~18 same-turn SELL-vs-SELL index races/game; rival keeps our NATIVE sell
  order 88% of the time. Blowouts = opponent-induced cash trough days 6-9 (rescue thread closed).
- Codex build-expert (moe/codex/NOTES.md, RESULT.md): reclaim layer stalls sheep workers ~12
  turns in the endgame; fix `cand_capture.py` +$944/game vs koshinm on a dev panel; held-out gate
  running.
- Top-11 (HANDOFF "09-21 PM" + 09-21e pig7selene notes): private reactive policies sharing our
  skeleton; ~10 cows vs our 6-8, strawberry day 2 vs day 5, tick-timed premium sells; top-3 sell
  premium at price index ~1.01 vs V43-family 0.61; structural ports onto our plan-bound tape
  FAILED repeatedly. Roman-class opponents win by continuous staple conversion.
- Rating maths (beta~200): +200 over an agent needs ~75-80% head-to-head vs the same field.
- Everything in HANDOFF §5 and marked dead in the timeline is falsified — do not re-propose it
  without new evidence.

Read: HANDOFF.md (§0-§5 and timeline 09-20..09-25f), MISTAKES.md, moe/BRIEF.md, moe/*/NOTES.md,
discussions.md (forum dump; Versions 1-5) for what top competitors say they do.

## Deliverable — write ONLY `moe/strat/<you>.md` (codex.md or opus.md)
1. Diagnosis: why our ceiling is ~2.8k (mechanism, with evidence you checked).
2. Ranked plan: up to 5 moves. For each: expected rating gain (with reasoning), confidence,
   days of work, what evidence would confirm/kill it within 24h, and the risk of it being
   another offline-only mirage.
3. Slot policy for the next 5 days (what should be live when, given convergence time ~4-8h
   and our history of churn).
4. The single thing you would do in the next 12 hours.
5. One paragraph: the strongest argument that 3k+ is NOT reachable by 09-30, and what then.
End with `CONFIDENCE 3k+ by 09-30: <p>%` and `CONFIDENCE top-10: <p>%`.
