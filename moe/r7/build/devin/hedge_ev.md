# devin-q: slot-B hedge EV under max-of-two scoring

## Measured correlation structure (140 shared cells: 7 opps x 20 seeds)
- M30B loss cells: 4/140 (seeds {6,15,17} + 17); v8 loss cells: 31/140 (seeds {1..5,8,11,12,18...})
- **both-lose cells: 0**; M30B's bad-seed set ∩ v8's bad-seed set = EMPTY; phi = -0.09.
- v8's failures are seed-draw-dependent; M30B's are rare and disjoint. Structurally a real hedge.

## EV model: R_X = mean + N(0,150), shared failure component via rho
Central world (no chassis collapse):
- second M30B (independent draws): E[max] ≈ 2487  (+85 over single M30B)
- v8: E[max] ≈ 2414  (+12)
- hyb2965: ≈ 2402  (+0)

Collapse world (M30B mean -400 = monoculture countered):
- second M30B: E[max] ≈ 2029-2073 (falls with it)
- v8 (rho~0 given disjoint failures): E[max] ≈ 2171  (+~142 vs copy)

## Breakeven
v8 wins the slot iff P(collapse) ≳ 35%: 85·(1-p) ≈ 12·(1-p) + 140·p.
Arguments for high collapse probability: shepherd lineage is the most-published class in the
competition; post-deadline field is deliberately stronger (agents pulled pre-deadline); the
mirror-band overlays all target this exact chassis.
Arguments for low: our anchors DO calibrate (shepherd 2091 live vs 2100 mapped); v8's own rating
is 252 below and needs the tail to matter.

## Ranking (current evidence)
1. **v8** — best hedge if P(collapse)>35%; license review pending (codex); public file verbatim.
2. **second M30B-class file** — +85 central-world EV, zero tail protection. Better if collapse is unlikely.
3. **hyb2965** — dominated.
4. **GH remainder** — unknown; could dominate BOTH (different class + higher mean). Unscreened.

## Caveats
Anchor-field correlation may not transfer to the post-deadline field; rho model is a stand-in for
"shared chassis-failure mass". v8's downside is impossible under max-of-two — only its upside counts.
