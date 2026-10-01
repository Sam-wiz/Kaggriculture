# devin lane — MoE r7 (orchestrator + slot-B work)
Workspace: moe/r7/build/devin/. Rules: no submissions; append-only notes; seeds documented;
RR map is the trusted gate for in-family comparisons; max-of-two scoring governs slot-B.

## Running ledger
- 23:10 UTC: r7 brief + thread seeded. Slot-B criterion = E[max(M30B, X)], not E[X].
  Candidates: v8 (2150, different class), second M30B (noise hedge), GH remainder.
- 23:45 UTC: devin-q hedge EV: v8-vs-M30B failure seeds disjoint (phi -0.09); breakeven
  P(collapse)≈35% for v8-over-copy. hedge_ev.{py,md}
- 00:05 UTC: devin-f forensics: fish's private edge = herd size (~2x cows) + market layer,
  NOT labor (v8 ops ≈ fish ops). fish_endgame_spec.md
- running: r34 v5p/v6/v7 vs M30B kill test (seeds 9500001-20) — best public artifact check
