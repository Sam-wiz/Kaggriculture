# prog lane — v8x + decoded top-team program overlay

Candidate: `v8prog.py` = `agents/v8x.py` + `PROG` config layer
(per-subsystem scheduled-vs-reactive flags via `V8PROG` env json).

Program tables (DSM decode, clone_dsm_bc + r8 brief):
- HIRE_TABLE = 4,4,6,6,6,6,8,9,9,10, 11x18, 10,10 — money-gated
- LAND days: NE d5, SW d7, (SE d9 only with quads=4) — money>=cost+250
- HERD_PLAN cumulative windows: COW 2@d1-5 +9@d6-11 +3@d9-18,
  SHEEP 3@d1-5 +5@d7-15 +3@d12-21, GOOSE 4@d6-11; batch capped at deficit
- CROP_PLAN tile floors: MELON14 d0-2 +8 d10-16, STRAW30 d2-18,
  TOM15 d6-26, CARROT70 d9-29; prepended to reactive plan
- sells: UNCHANGED (v8x standing-sell fix kept byte-identical)

## Screen 1 — single subsystems, seeds 6200-6207 x2 seats vs v8x

| variant      | W-L-T | margin  |
|--------------|-------|---------|
| hire only    | 16-0  | +22,222 |
| herd only    | 12-4  | +11,509 |
| all sched(3q)| 8-8   |  -2,082 |
| all sched(4q)| 8-8   |  -7,225 |
| crop only    | 4-12  |  -6,711 |
| land4 only   | 4-12  |  -8,161 |

## Screen 2 — combos, same seeds vs v8x

| variant                    | W-L-T | margin  |
|----------------------------|-------|---------|
| hh = hire+herd             | 14-2  | +27,664 |
| hhc = hire+herd+crop       | 16-0  | +23,939 |
| hhl3 = +sched land (3q)    | 10-6  |  +6,538 |
| hhl4 = +sched land (4q)    | 9-7   |  +1,318 |
| hhw = hh + wheat_fill      | 16-0  | +21,099 |
| hhf = hh + herd-first buys | 14-2  | +25,267 |

## Gate 1 — vs agents/v8x.py, fresh seeds 7100-7119 x2 seats

| variant | W-L-T | margin  |
|---------|-------|---------|
| hh      | 40-0  | +27,474 |
| hhc     | 35-5  | +17,214 |

## Gate 2 — vs subAB_m30b.py, seeds 8000-8023 x2 seats

| side         | W-L-T | margin   |
|--------------|-------|----------|
| hh (v8prog)  | 0-48  | -84,667  |
| v8x baseline | 0-24  | -110,089 |

0 wins vs the elite chassis = the documented v8-family cap, but v8prog
closes ~25k of the family gap (consistent with the +27.5k mirror gain).

## Final variant

`v8prog.py` as shipped = hh: `V8PROG={"land":0,"crop":0}` baked as defaults.
- hires: HIRE_TABLE [4,4,6,6,6,6,8,9,9,10]+[11]*18+[10,10], same money gate
- herd: HERD_PLAN cumulative windows, affordability+batch-cap only
- land/crops/sells: untouched v8x reactive core

## Reading

- Scheduled HIRES is the single biggest win (+22k alone): v8x's workload-
  derived hiring under-hires through the mid-game compounding window; the
  decoded 4→11 ramp funds labor ahead of the work.
- Scheduled HERD (+11.5k alone) confirms the 09-29 live-loss diff: v8x
  under-invests in animals. HERD_PLAN windows + affordability gate beat
  the forecast-hurdle `best_animal`.
- Scheduled LAND hurts in every combo (hhl3 +6.5k, hhl4 +1.3k vs hh
  +27.7k): v8x's land_pays ROI check is better than fixed calendar days —
  extends the falsified max_quads=4 result to scheduled buys.
- Scheduled CROP floors hurt alone (-6.7k) and inside combos (hhc gate
  -10k vs hh): committed melon/strawberry tiles burn opening cash that
  the reactive value-scorer would have spent better.
- Best variant: hh (hire+herd scheduled; land, crops, sells reactive).
