"""Per-episode diagnostics: money curve, land, hands, tile usage, sales by product."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness
from kaggle_environments.envs.kaggriculture import kaggriculture as K


def run(a, b, seed=1, player=0, verbose=True):
    log = []
    def on_step(step, state, env):
        obs0 = state[0].observation
        if (step + 1) % 24 == 0 or step == 0:
            f = obs0.farms
            priv = [s.observation.private for s in state]
            log.append(dict(step=step, day=obs0.day,
                            money=[f[0]["money"], f[1]["money"]],
                            quads=[len(f[i]["unlocked_quadrants"]) for i in (0, 1)],
                            prices=dict(obs0.market["prices"]),
                            inv={k: v - 10000 for k, v in obs0.market["inventory"].items()},
                            shops=list(obs0.town["unlocked_shops"]),
                            shed=[dict(priv[i]["shed"]) for i in (0, 1)],
                            tiles=[tile_counts(f[i]["tiles"]) for i in (0, 1)]))
    r = harness.run_episode(a, b, seed=seed, on_step=on_step, catch_errors=False)
    if verbose:
        print(f"seed={seed}  {a} vs {b}  final={r['reward']}")
        print(f"{'day':>4}{'moneyA':>9}{'moneyB':>9}{'qA':>3}{'qB':>3}  tilesA")
        for e in log:
            tc = e["tiles"][player]
            s = " ".join(f"{k}:{v}" for k, v in sorted(tc.items()) if v)
            print(f"{e['day']:>4}{e['money'][0]:>9.0f}{e['money'][1]:>9.0f}"
                  f"{e['quads'][0]:>3}{e['quads'][1]:>3}  {s}")
        last = log[-1]
        print("\nshops:", collections.Counter(last["shops"]))
        print(f"{'product':<12}{'price':>7}{'net inv':>9}{'shedA':>7}{'shedB':>7}")
        for p in K.PRODUCTS:
            print(f"{p:<12}{last['prices'][p]:>7}{last['inv'][p]:>9}"
                  f"{last['shed'][0].get(p,0):>7}{last['shed'][1].get(p,0):>7}")
    return r, log


def tile_counts(tiles):
    c = collections.Counter()
    for row in tiles:
        for t in row:
            if t is None: c["empty"] += 1
            elif t == "LOCKED": c["locked"] += 1
            elif t["kind"] == "WEED": c["weed"] += 1
            elif t["kind"] == "PLANT": c[t["crop"][:4].lower()] += 1
            elif "animal" in t: c[t["animal"][:3]] += 1
            else: c[t["kind"][:4]] += 1
    return dict(c)


if __name__ == "__main__":
    a = sys.argv[1]; b = sys.argv[2] if len(sys.argv) > 2 else "starter"
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    run(a, b, seed)
