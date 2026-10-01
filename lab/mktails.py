"""Force each of the router's four tails, to measure how much its routing rule leaves on the table.

All four tails are byte-identical before the turn that selects them, so pinning one from t=0 is
exactly what switching to it does -- it just removes the condition. Comparing the routed agent to
the per-seed best tail gives the oracle gap: the most that better routing could ever be worth.
"""
import os
src = open("sub_router.py").read()
TAILS = {"MAIN": "MAIN", "YARN": "YARN", "YARN_CARROT": "YARN_CARROT", "MILK_GLUT": "MILK_GLUT"}
os.makedirs("bench_frozen", exist_ok=True)
for name, const in TAILS.items():
    out = src + f'''

# --- pinned tail: {name} (routing disabled) ---
DECISIONS = ()
_pin_Agent = Agent


class _PinnedAgent(_pin_Agent):
    def __init__(self):
        _pin_Agent.__init__(self)
        self.cur = {const}


Agent = _PinnedAgent
_pin_base = agent
del agent


def agent(obs):
    return _pin_base(obs)
'''
    p = f"bench_frozen/T_{name}.py"
    open(p, "w").write(out)
    print("wrote", p)
