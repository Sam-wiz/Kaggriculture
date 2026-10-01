"""Build harvest_m30_brx2.py = harvest_m30.py + BRX2 wrapper ported from moe/opus/cand_brx2.py.

BRX2 (sonnet r6 #3): on turns with >=2 distinct-item SELL orders, try every permutation of
which SELL row fills which slot, scored by per-item lockstep market sim vs a predicted
rival order (native vs SIR-sorted, weighted by an online log-odds). Only SELL slots are
permuted. Measured 0.844 WR on the old pool; never retested on C1/Harvest.

Port: SIR helpers (price model is game-defined, identical) + BRX helpers + BRX2 agent,
parent rebound from _sir_parent to Harvest's final agent.
"""
src = open("moe/r6/build/devin/harvest_m30.py").read()
brx = open("moe/opus/cand_brx2.py").read().splitlines(keepends=True)

# SIR helpers: lines 6724..6782 (imports, _SIR_PARAMS, _SIR_SHOPS, _sir_shape, _sir_price,
# _sir_demand, _sir_score) -- excludes _sir_agent/_sir_parent wiring.
sir_helpers = "".join(brx[6723:6782])
# BRX helpers: 6811..6929 (_brx_it .. _brx_choose) -- excludes _brx_agent.
brx_helpers = "".join(brx[6810:6929])
# BRX2 block: 6963..7113 (imports .. end of _brx2_agent).
brx2_block = "".join(brx[6962:7113])
brx2_block = brx2_block.replace("_sir_parent(", "_BRX2_PARENT(")

assert "_sir_score" in sir_helpers and "_brx_choose" in brx_helpers and "_brx2_agent" in brx2_block
assert "_sir_parent(" not in brx2_block

app = (
    "\n\n# --- BRX2 port onto the Harvest chassis (devin lane, 09-27) ----------------------------\n"
    "_BRX2_PARENT = agent\n\n"
    + sir_helpers + "\n" + brx_helpers + "\n" + brx2_block
    + "\nagent = _brx2_agent\n"
)
src += app
open("moe/r6/build/devin/harvest_m30_brx2.py", "w").write(src)
print("wrote harvest_m30_brx2.py", len(src))
