
### [astra] 09-30t — Distant-trip signatures; the 54% premise is misleading

**Q1: one event-signature test**, 16s foreground; first 20 DSM episodes in `bc2s_DSM`, reconstructed from rawkeep. Same-day contiguous trips ending at a departure-feasible service; six service types, FEED cargo-masked. Future endpoints are outcomes only. Reused episodes, descriptive evidence, no held-out win claim.

Among **1,317 trips of distance ≥3 leaving workable tiles**:
- Scarcest positive-count type: **152/1,317 (11.5%)**; nearest-of-that-type AND scarcest: **53/1,317 (4.0%)**. Literal scarcity-first fails this cohort.
- Target ready at dawn: **1,308/1,317 (99.3%)**, versus **12,419/12,466 (99.6%)** short trips. Dawn readiness does **not** distinguish a queue.
- Daily-service subset: only **139/1,129 (12.3%)** cross quadrants; **79/1,129 (7.0%)** enter a quadrant with a larger remaining fraction of dawn jobs. Weak support for cross-zone backfill; quadrants are only a proxy for territories.

Artifacts: `build/astra/round_c_probe.{py,json}`, `round_c_trips.jsonl`. Target selection remains unresolved.

**Q2: baseline correction.** `bc2s.d` stores ONE BFS first direction, not target offsets, and distance-zero entries hide other same-type jobs. On these episodes, original probe: **35,808/66,163 (54.1%)**; raw-board any-shortest-direction agreement: **57,431/67,476 (85.1%)**. Different eligibility; latter is set-valued, **not top-1 accuracy**. “Other half = distant commitment” does not follow.

Spec holes: missing item/quantity heads, species-specific inventory/seeds, absolute position, peer positions, and causal history with dawn reset. Global nearest summaries omit alternative targets. Gate movement initiation separately from continuation; also gate leave/stay and arguments, group episodes/seeds, then closed-loop survival/paired wins. Static ZH cannot establish territory causally.

**Next action (devin):** repair geometry baselines and freeze splits before walker training; no submissions.
