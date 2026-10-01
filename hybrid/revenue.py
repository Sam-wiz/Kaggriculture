import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import harness
from kaggle_environments.envs.kaggriculture import kaggriculture as K

BL = "rivals/boatlee_v29-r1-adaptive-market-hysteresis/main.py"
orig = K._commit_unit
CUR = {"step": 0}
REV = [collections.Counter(), collections.Counter()]
QTY = [collections.Counter(), collections.Counter()]
BUY = [collections.Counter(), collections.Counter()]
TIME = []  # (step, player, item, price)

def patched(op, item, price, farm, private, market, shed_capacity=100):
    ok = orig(op, item, price, farm, private, market, shed_capacity)
    if ok:
        p = 0 if farm is CUR["farms"][0] else 1
        if op == "SELL":
            REV[p][item] += price; QTY[p][item] += 1
            TIME.append((CUR["step"], p, item, price))
        elif op in ("BUY_PRODUCT", "BUY_SEED", "BUY_ANIMAL"):
            BUY[p][op + ":" + str(item)] += price
    return ok

K._commit_unit = patched

def run(a, b, seed=1):
    for c in REV + QTY + BUY: c.clear()
    TIME.clear()
    def on_step(step, state, env):
        CUR["step"] = step + 1
        CUR["farms"] = state[0].observation.farms
    def pre(step, state, env): pass
    # need farms available before first interpreter call -> set via wrapper
    import copy
    r = harness.run_episode(a, b, seed=seed, on_step=on_step)
    return r

if __name__ == "__main__":
    a = sys.argv[1] if len(sys.argv) > 1 else BL
    b = sys.argv[2] if len(sys.argv) > 2 else BL
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    # bootstrap farms ref
    import harness as H
    _orig_interp = K.interpreter
    def interp(state, env):
        CUR["farms"] = state[0].observation.get("farms") if "farms" in state[0].observation else None
        r = _orig_interp(state, env)
        CUR["farms"] = state[0].observation["farms"]
        return r
    K.interpreter = interp
    r = run(a, b, seed)
    print("final", r["reward"], r["status"])
    items = sorted(set(list(REV[0]) + list(REV[1])))
    print(f"{'item':<12}{'p0$':>9}{'p0n':>6}{'p0avg':>7}{'p1$':>9}{'p1n':>6}{'p1avg':>7}")
    for it in items:
        r0, n0 = REV[0][it], QTY[0][it]
        r1, n1 = REV[1][it], QTY[1][it]
        print(f"{it:<12}{r0:>9}{n0:>6}{r0/max(1,n0):>7.0f}{r1:>9}{n1:>6}{r1/max(1,n1):>7.0f}")
    print(f"{'TOTAL':<12}{sum(REV[0].values()):>9}{sum(QTY[0].values()):>6}{'':>7}{sum(REV[1].values()):>9}{sum(QTY[1].values()):>6}")
    print("p0 spend:", dict(BUY[0]))
    # strawberry sale timeline
    import itertools
    for it in ("STRAWBERRY", "MILK", "WOOL", "WHEAT"):
        buckets = collections.defaultdict(lambda: [0,0])
        for (s, p, i, pr) in TIME:
            if i != it or p != 0: continue
            b = s // 48
            buckets[b][0] += 1; buckets[b][1] += pr
        print(it, " ".join(f"{b*48}:{v[0]}@{v[1]//max(1,v[0])}" for b, v in sorted(buckets.items())))
