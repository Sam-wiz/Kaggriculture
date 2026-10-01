# Endgame plan — optimise the metric that PAYS

This is the MEMORY.md lesson repeating: *"Optimize the metric that PAYS, not the one that looks
good."* In the OpenAI competition the $50k rode on a private board where our high-public marker
scored 0. Here, the live leaderboard we have been optimising for two weeks **is not what pays.**

---

## What actually determines the prize

Straight from the competition text:

> **September 30** — Final Submission Deadline.
> **October 1 → ~October 15** — games continue to run "to continue to reduce uncertainty,
> **especially for new agents**".
> **"A final Bradley-Terry tournament will be run on those episodes to produce the final
> leaderboard."**
> **"The latest 2 submissions are also used for final leaderboard evaluation."**
> **"On the leaderboard, only your best-scoring bot will be shown."**

And the prize table:

| place | prize |
|---|---|
| 1st … 10th | **$5,000 each** |

---

## Consequence 1: the objective is P(top-10), not rank

**#1 and #10 pay identically.** There is no financial reason to chase #1, and chasing it means
accepting variance we are not paid for. The correct objective is

> **maximise P(finish in the top 10)**

which argues for *reducing* variance in the final placement. Our earlier "#1 or nothing" framing was
optimising something the prize structure does not reward.

## Consequence 2: the ~240-point convergence lag does not exist in the final metric

The live ladder is a **sequential** estimator: every submission starts at 600 and moves ~4.5 points
per game, so a strong agent looks weak for ~100 games. That lag is the single biggest distortion in
everything we have measured.

Bradley-Terry is a **batch** fit:

```
P(i beats j) = sigmoid(theta_i - theta_j)
```

estimated by maximum likelihood over the **entire win/loss network at once**. There is no starting
value, no path dependence, no lag. Our displayed 2,613 and keiz's 3,047 are artifacts of the
sequential estimator run for different numbers of games; the final tournament refits from scratch.

**So our current ladder position does not pay.** Agent quality during Oct 1-15 does.

## Consequence 3: but the deadline rating still matters — indirectly

Post-deadline, matchmaking still pairs by rating. So:

```
rating on Sept 30  ->  who we are matched against Oct 1-15  ->  the games BT is fitted on
```

Beating strong opponents raises BT strength far more than beating weak ones. A submission that
arrives at the deadline with a low rating gets seeded against weak opponents, and BT then has little
evidence that it belongs higher. So we want to arrive at Sept 30 **rated high**, even though the
rating itself is not scored.

## Consequence 4: the final two submissions are a free hedge

Only the latest 2 count, and only the **best** of them is shown. So the last two submissions should
be **two genuinely different agents**, not two copies — we get the max of two draws at no cost.
This is MEMORY.md lesson 4 ("hedge hidden-metric finals manually") applied directly.

---

## The plan

| window | action |
|---|---|
| **now → ~Sept 26** | Experiment freely. Pre-deadline ladder position does not pay, so the only value of a submission is as a *measurement instrument*. Use the mirror benchmark for candidate selection and spend slots only to resolve questions the mirror cannot. |
| **~Sept 26-29** | Stop experimenting. Get our best agent live and let it climb so the deadline rating is high, seeding good post-deadline matchmaking. |
| **Sept 30** | Submit the final two: **the best agent, and a genuinely different second agent** as a hedge. Not two copies. |
| **Oct 1-15** | Nothing to do. BT is fitted on these games. |

## Open question being measured

Whether BT is fitted on *only* the Oct 1-15 episodes or on the full history is ambiguous in the
wording ("those episodes"). It matters: if only post-deadline games count, everything before Sept 30
is purely instrumental. We are fitting BT offline on the public episode dumps to understand the
metric's behaviour either way — and because that same fit answers whether a real policy gap exists
(see `BRIEFING_UPDATE.md`).

## Note on the dumps

`kaggle/kaggriculture-episodes-index` lists ~37 daily dumps of ~665 episodes each (~500 MB
compressed per day). **They are curated to the top-rated agents** — 34 distinct teams in the
2026-09-04 dump, and we are not among them. So the dumps place the top of the ladder but cannot
place us directly; connecting our own episodes to that graph requires opponents that appear in both.
