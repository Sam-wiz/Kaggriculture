Read moe/BRIEF.md in full, then work your lane. You are the CODEX expert: write only under moe/codex/.

LANE A — ENDGAME MONEY CAPTURE (days 21-29, steps ~504-719).
Against koshinm (and, per live autopsies, against same-tape clones in the 2400-2900 band) the whole
margin opens in the liquidation window: identical production, then we lose ~$1k on price capture
(koshinm's WOOL sells capture +$11/unit; their chassis switches to a dedicated route at step 648).
Also known: the premium overlay reads the PRE-action shed, so units dropped this turn are sold a
turn late (same-turn shed blindspot, ~-$644 in one autopsied loss).
1. Instrument it: in a few paired games vs koshinm (moe/gate.py pool path) and vs subV2_f55rec,
   log per-step fills and prices for our sells in days 21-29 (hook the engine, count FILLS not
   order quantities — orders != fills is a mistake this repo has made repeatedly).
2. Find what koshinm's endgame does differently (its source is in the gate POOL path) and
   quantify it in dollars per game.
3. Build the smallest layer that captures it on top of subV_sir2.py and/or subV2_f55rec.py.
   Prove the layer fires (count its actions), then run moe/gate.py on your seed slice.
Deliver per BRIEF.md: moe/codex/cand_*.py, moe/codex/RESULT.md with a VERDICT line, NOTES.md.
