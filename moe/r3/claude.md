# Claude Code — MoE r3, round-1 position (written before reading codex.md / opus.md)

## 1. Diagnosis (checked on the 89 live shepherd games now in mine/opp)
**The 2200-2600 band is shepherd's own clone cluster, and we lose the mirror.**
- Shepherd vs opponents >=2200: 34 games, 7 wins. 27 losses; **22 of them at >=97% unit-op identity**
  (same cows 5/5, sheep, land, bank 82k/82k). Median loss −$665. Only 2-3 losses are genuinely
  different agents (Joseph Adamski 0%, Erfan 57%, both ~2700).
- Near-mirror subset (>=95% unit identity, >=2200): **28 games, 6-22.** Seat 0: 2-8, seat 1: 4-14 —
  not a seat artefact.
- In those games unit ops differ on only ~7 turns/game, but **market orders differ on ~100 turns/game
  from step 1**. The clones sell MORE premium units on contested turns (MILK they>us 509 vs us>they
  342; STRAWBERRY 385 vs 216; WOOL 305 vs 235) and their non-SELL orders differ on 608 turns.
- => The band runs **shepherd + a market overlay**. Shepherd was fresh for ~2 h; once it met its own
  copies-with-overlays it converged to their centre and below.
- hyb2965 (early, n=7 vs >=2200): its big losses are NON-clones (lingxiaojun −20k, AI是我的豆包 −17k,
  0% identity, ~2700) — the private tier; it split its clone games 3-2.

## 2. Instrument: closed-loop overlay tournament on the shepherd chassis
Previous instruments failed because opponents were (a) public agents that are not the field, or
(b) frozen tapes that cannot react. Here the field is **shepherd + X**, and X is plausibly one of the
public market overlays we hold (rivals7: shiiin9 order-book, arsgorynich order-book-v3, V55 one-turn
market race edge, V57 funding-order, SIR, prem f55, BRX, clamp) or a combination.
1. **Identify X per clone (exact reproduction).** For each near-mirror game, run shepherd+X_i in the
   opponent seat on the recorded seed, closed-loop against shepherd (our seat is shepherd, which is
   what actually played). If X_i is the clone's overlay, the game reproduces the recorded opponent
   market stream turn-for-turn and both banks to the dollar. This is falsifiable per game and needs
   no frozen tape. Unmatched games = "unknown overlay" mass, kept explicit.
2. **Best response.** Round-robin shepherd+Y vs the identified population {shepherd+X} closed-loop,
   weighted by prevalence. Both sides react, so the pre-empt/front-run flattery of open-loop replay
   does not apply.
3. **Validation against live (pre-registered):** the instrument must reproduce shepherd-vanilla's
   live record vs the matched clones (~6-22) within noise before it is allowed to rank anything.

## 3. Live protocol
- Anchor = shepherd (2100, known). Each upload evicts the older submission; shepherd is the older of
  the pair, so the next upload evicts shepherd, not hyb2965. Plan: upload the best-response build
  B (evicts shepherd); hold [hyb2965, B]; read B after ~60 games / ~15 games vs >=2200 by fitted
  rating on one LB snapshot. If B < shepherd-equivalent, re-upload shepherd (evicts hyb2965) — cost
  one slot, bounded downside.
- Freeze 09-28 12:00 UTC.

## 4. Candidates
| # | candidate | gain | conf | hours | kill test |
|---|---|---|---|---|---|
| 1 | shepherd + best-response overlay from §2 | band is 80% mirrors: 6-22 -> ~14-14 would be +0.29 WR in that band, ~+150-200 | 0.3 | 6-10 | instrument fails validation, or best Y < +0.10 vs population |
| 2 | hyb2965 kept as slot 2 | its converged level is unknown (n=7 vs >=2200) | — | 0 | live read |
| 3 | reactive replanner vs private tier | the real top-10 lever | <0.05 by 09-30 | >5 days | — |

## 5. Next 12 h
Build the overlay library on the shepherd chassis (subW_shepherd.py + each public market overlay,
proven to fire), run step 2.1 identification on the 28 near-mirror games (closed-loop, 2 workers),
then 2.2 if >=50% of the mirror mass is identified.

## 6. Stop
Open-loop replay as a gate for market layers; public-pool gate for strength claims; any submission
not backed by closed-loop evidence against the identified field; tuning prem floors.

P(top-10): 1%  P(silver): 5%  P(bronze): 25%
