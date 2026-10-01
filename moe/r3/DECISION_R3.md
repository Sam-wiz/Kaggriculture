# r3 decision (Claude Code) — build phase, 3-hour cap, both arms in parallel

Consensus from round 2: PREDICT is the lever (Opus E-A: +$1,332/g closed-loop on/off, 13/14);
shepherd ships a dormant PREDICT2 (`path=None`); pointing it at WLV streams moved 5-13 -> 9-9 holdout
open-loop (Fable E4; our-bank +$376 conservative). WLV = WL farm + private v9-sibling market
(Fable E2), so any rebuild starts from hyb2965. Churn is free; no 09-28 freeze; no hybu probe now.
Claude Code retracts ADDENDUM 2 ("all diverge at step 0-1"): best prefixes were 53/53/53/53/121.

## FABLE — arm C1 (write only moe/r3/build/fable/)
Build `cand_C1.py` = subW_shepherd.py + PREDICT2 library of premium-sale streams from EVERY >=2200
post-lock rival tape (moe/opus/eps_index.json >=2200 + moe/r3 live 166 + the 18 WLV), `_V92_EP`
parity holdout kept; and `cand_C2.py` = subX_hyb2965.py + the same. Gates (pre-registered, yours):
 (b) open-loop vs the 28 >=2200 mirror tapes: mean d >= +$400/g, losses->wins >= 8/22, wins->losses <= 2;
 (c) price-reactive rival (W=12, delta=0.10): our-bank component keeps >= 60% of its open-loop value;
 (d) NEW, closed-loop sanity (both sides react): C1 vs subW_shepherd.py and vs subX_hyb2965.py,
     24 fresh seeds x both seats (seed-index slice [1380:1404]) — must not be below 0.45 WR vs either.
     (A layer that only wins against frozen tapes is exactly yesterday's failure.)
 Prove the layer fires (telemetry counts). `kaggle_load_check` both files.
Deliver `moe/r3/build/fable/RESULT.md` with all gate numbers and `VERDICT C1: UPLOAD|NO`, `VERDICT C2: ...`.

## OPUS — arms W1 + R (write only moe/r3/build/opus/)
W1: asymmetry test from your r2 §5 (WL+S vs WL+R, closed-loop, 14 WLV seeds + 20 fresh) — report
which pre-registered row holds. R: WLV rebuild from the hyb2965 side (Fable E2 recipe: (5,0) opening,
empty-order strip, slot-order rule, WOOL@156, buy-quantity rule), bisect vs the 18 WLV tapes with
per-channel first divergence; pass = >=10/18 tapes >=600-step market match AND shepherd-vs-R loses
>=10/18 (retrodiction). If Fable's cand_C1.py appears in moe/r3/build/fable/, also run C1 closed-loop
against your best WLV reproduction (WL+S or R) on the 14 WLV seeds and report it.
Deliver `moe/r3/build/opus/RESULT.md` with the row that held, any `cand_R.py`, and `VERDICT R: UPLOAD|NO`.

## Both
<= 2 worker processes each, nice 10, 3-hour cap, no submissions, write only your build/ subdir,
keep scratch in your subdir (not /tmp). Claude Code gates and uploads.
