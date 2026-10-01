import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import harness
from kaggle_environments.envs.kaggriculture import kaggriculture as K

BL = "rivals/boatlee_v29-r1-adaptive-market-hysteresis/main.py"
orig = K._drop_inventories_to_shed
LOG = []

def patched(private, capacity):
    before = dict(private["shed"])
    carried = {}
    for inv in private["inventories"]:
        for k, v in inv.items():
            carried[k] = carried.get(k, 0) + v
    orig(private, capacity)
    after = dict(private["shed"])
    kept = {k: after.get(k, 0) - before.get(k, 0) for k in carried}
    lost = {k: carried[k] - kept.get(k, 0) for k in carried if carried[k] - kept.get(k, 0) > 0}
    LOG.append(dict(shed_before=sum(before.values()), carried=carried, lost=lost))

K._drop_inventories_to_shed = patched

def run(a, b, seed=1):
    LOG.clear()
    r = harness.run_episode(a, b, seed=seed)
    return r, list(LOG)

if __name__ == "__main__":
    a = sys.argv[1] if len(sys.argv) > 1 else BL
    b = sys.argv[2] if len(sys.argv) > 2 else BL
    r, log = run(a, b, seed=int(sys.argv[3]) if len(sys.argv) > 3 else 1)
    print("final", r["reward"], r["status"])
    # log alternates player0, player1 per day
    tot = [{}, {}]
    for i, e in enumerate(log):
        p = i % 2
        for k, v in e["lost"].items():
            tot[p][k] = tot[p].get(k, 0) + v
        if e["lost"]:
            print(f"day~{i//2:2d} p{p} shed_before={e['shed_before']:3d} lost={e['lost']}")
    print("TOTAL LOST p0:", tot[0])
    print("TOTAL LOST p1:", tot[1])
