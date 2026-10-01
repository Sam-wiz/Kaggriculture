"""Trace what the six-day budget guard actually does during an episode."""
import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import harness  # noqa: E402

OPP = sys.argv[1] if len(sys.argv) > 1 else "rivals/boatlee_v29-r1-adaptive-market-hysteresis/main.py"
SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 1

spec = importlib.util.spec_from_file_location("gtrace", os.path.join(ROOT, "port2/h_guard.py"))
M = importlib.util.module_from_spec(spec)
sys.modules["gtrace"] = M
spec.loader.exec_module(M)

log = []
_orig = M._apply_six_day_budget_guard


def traced(state, action, requirements):
    out = _orig(state, action, requirements)
    if state.step % int(M.P["interval"]) == 0:
        budget = requirements[0]
        cash = state.money
        for item in range(M.N_PRODUCTS):
            sold = min(max(0, state.shed[item]),
                       M._existing_sale(action[3], len(action[3]), item))
            cash += sold * state.prices[item]
        added = [(M._ITEMS[o[1]], o[2]) for o in out[3]
                 if o[0] == M.M_SELL] if out[3] != action[3] else []
        log.append(dict(step=state.step, budget=budget, cash=cash,
                        short=budget - cash, before=len(action[3]),
                        after=len(out[3]), changed=out[3] != action[3],
                        shed=[(M._ITEMS[i], state.shed[i])
                              for i in range(M.N_PRODUCTS) if state.shed[i] > 0],
                        prices=[(M._ITEMS[i], state.prices[i])
                                for i in range(M.N_PRODUCTS) if state.shed[i] > 0],
                        protect=[(M._ITEMS[i], requirements[2][i])
                                 for i in range(M.N_PRODUCTS) if requirements[2][i] > 0],
                        sells=added))
    return out


M._apply_six_day_budget_guard = traced
opp = os.path.join(ROOT, OPP) if OPP.endswith(".py") else OPP
r = harness.run_episode(M.agent, opp, seed=SEED, catch_errors=False)
print(f"opp={OPP} seed={SEED} bank={r['reward']} errors={r['errors']}")
for e in log:
    print(f"step {e['step']:>3} budget={e['budget']:>9.0f} cash={e['cash']:>9.0f} "
          f"short={e['short']:>+9.0f} orders {e['before']}->{e['after']} "
          f"changed={e['changed']}")
    print(f"      shed={e['shed']}")
    print(f"      protect={e['protect']}  prices={e['prices']}")
    print(f"      final SELLs={e['sells']}")
