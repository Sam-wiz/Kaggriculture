Read moe/BRIEF.md in full, then work your lane. You are the OPUS expert: write only under moe/opus/.

LANE B — WHERE WE LOSE TO THE 2400-2900 BAND, AND ONE FIX.
Our builds win ~0.9 below 2200 and only 0.36-0.50 against 2400-2800 opponents (HANDOFF 09-25).
1. Use the cached live replays (live_eps/, mine/opp/, mine/top*, and tools like
   live_eps/band_analyze.py, fingerprint_loss2.py, mine/fetch_ours.py outputs already on disk —
   do not re-download what is cached; you have no Kaggle credentials anyway) to decompose the
   money gap in our losses to 2400-2900 opponents: by game phase (days 0-9 build, 10-20 steady
   state, 21-29 liquidation) and by channel (production volume per product, sell price achieved
   per product, labour/hire cost, animals placed). Use FILLS, not order quantities.
2. Identify the single largest recoverable channel. Known candidates: production mix (opponent
   tomato/carrot annex; our V219 gate declines when only 2 tomato-demand shops exist), early
   strawberry timing (top agents start day 2 vs our day 5), cow count (top ~10 vs our 6-8).
   Structural ports have failed before on the plan-bound tape — read why in HANDOFF before trying.
3. Build the smallest change that recovers it on top of subV_sir2.py or subV2_f55rec.py. Prove it
   fires, then run moe/gate.py on your seed slice.
Deliver per BRIEF.md: moe/opus/cand_*.py, moe/opus/RESULT.md with a VERDICT line, NOTES.md.
