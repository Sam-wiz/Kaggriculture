### [astra] 09-30r — A: test raw actions; B: skip unless closed-loop gates pass

**A.** Stay-or-step is a useful hypothesis, not a decoded mechanism: repeated same-tile services and short moves also follow from nearest-job scoring.

**Action space:** a union, not a product: four moves, PASS, and current-tile operations, with item/species and quantity heads for parameterized commands. Apply causal feasibility masks; preserve rejected teacher commands as diagnostics.

**Input:** 5×5 tile features plus absolute position/unit index, cargo, species-specific seeds/shed, day/hour, global urgent-job counts and nearest feasible job/shed directions. Compare frame-only against four prior raw actions/observed states; reset worker history at dawn. Local-only cannot represent distant supply trips.

**Labels:** predict the immediate raw command from `obs[t−1]→action[t]` on ALL turns. `bc2s.y` supplies op/item but loses quantities; reconstruct neighborhoods/arguments from replays. The 92k INIT endpoints and `y2` are future-job diagnostics, not next-action labels or history features.

**Leakage:** group duplicate episodes/seeds/both seats; reserve untouched episodes after repeated last-ten tuning. Homes use training data only. No future endpoints, same-turn peer commands, post-action state, or cross-dawn hand identities.

**Audit:** current `tilefit.py` computes `oktr` but never applies it in training; unavailable/masked targets contribute invalid gradients. Thus 20% does not establish that candidate scoring is structurally wrong. Evidence: `build/astra/walker_audit.json`.

**Falsification gate:** ≥85% held-out raw op/item accuracy AND ≥5pp over a deterministic stay/nearest baseline; report movement/service/argument strata. Then require closed-loop survival and wins, not teacher accuracy.

**B: skip tonight's slot.** Neither graft nor hand-coded territory has qualifying evidence; replacing v8s has opportunity cost despite max-of-two scoring. Reconsider only after a frozen candidate gains ≥5pp paired field win rate over v8s, with seed-bootstrap 95% lower bound >0 on ≥40 untouched seeds, both seats, a fixed pool including responsive opponents; loader/official-env pass, counted interventions, zero internal exceptions. Incomplete gate means no-go. Cheapest diagnostic: causal shed-pickup→service failures and dawn resets; do not reopen falsified market leftovers.

**Next action (devin):** correct the training mask, preregister the raw-action comparison, and retain [v8s,v8] absent a complete gate.
