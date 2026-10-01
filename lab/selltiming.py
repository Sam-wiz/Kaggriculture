"""Cumulative units sold per day, us vs the opponent, inferred from market inventory."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness
from kaggle_environments.envs.kaggriculture import kaggriculture as K

def run(me, opp, seed=1):
    prev_inv = {}
    prev_shed = {}
    ours = collections.Counter(); theirs = collections.Counter()
    per_day = []
    st = {}
    def on_step(step, state, env):
        obs0 = state[0].observation
        inv = obs0.market["inventory"]
        shed = state[0].observation.private["shed"]
        drain = collections.Counter()
        if step % 4 == 0:
            for s in obs0.town["unlocked_shops"]:
                prods = K.SHOPS[s]; m = 2 if len(prods) == 1 else 1
                for p in prods: drain[p] += m
        if step % 24 == 0:
            for p in K.TOWN_CENTER_PRODUCTS: drain[p] += 1
        if prev_inv:
            for p in K.PRODUCTS:
                d_inv = inv[p] - prev_inv[p]          # net change
                our_sold = max(0, prev_shed.get(p, 0) - shed.get(p, 0))
                total_sold = d_inv + drain[p]
                ours[p] += our_sold
                theirs[p] += max(0, total_sold - our_sold)
        prev_inv.clear(); prev_inv.update(inv)
        prev_shed.clear(); prev_shed.update(shed)
        if (step + 1) % 24 == 0:
            per_day.append((obs0.day, sum(ours.values()), sum(theirs.values()),
                            obs0.farms[0]["money"], obs0.farms[1]["money"]))
    r = harness.run_episode(me, opp, seed=seed, on_step=on_step, catch_errors=False)
    print(f"{me}  vs  {opp}   final={r['reward']}")
    print(f"{'day':>4}{'ourUnitsSold':>14}{'theirUnitsSold':>16}{'ourMoney':>10}{'theirMoney':>12}")
    for d, a, b, m1, m2 in per_day:
        print(f"{d:>4}{a:>14}{b:>16}{m1:>10.0f}{m2:>12.0f}")
    print("\nby product  ours / theirs:")
    for p in K.PRODUCTS:
        if ours[p] or theirs[p]:
            print(f"  {p:<12}{ours[p]:>6} /{theirs[p]:>6}")

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 1)
