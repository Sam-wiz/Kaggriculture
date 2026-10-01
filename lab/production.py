"""Units actually sold, inferred from market inventory (vs a near-silent opponent)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness
from kaggle_environments.envs.kaggriculture import kaggriculture as K

def run(path, opp="pass", seed=1):
    st = {}
    def on_step(step, state, env):
        obs0 = state[0].observation
        st['inv'] = dict(obs0.market["inventory"])
        st['shops'] = list(obs0.town["unlocked_shops"])
        st['step'] = step
        st.setdefault('drain', {p: 0 for p in K.PRODUCTS})
        if step % 4 == 0:
            for shop in st['shops']:
                prods = K.SHOPS[shop]; m = 2 if len(prods) == 1 else 1
                for p in prods: st['drain'][p] += m
        if step % 24 == 0:
            for p in K.TOWN_CENTER_PRODUCTS: st['drain'][p] += 1
    r = harness.run_episode(path, opp, seed=seed, on_step=on_step, catch_errors=False)
    print(f"{path} vs {opp} seed={seed} bank={r['reward'][0]:.0f}")
    print(f"{'product':<12}{'sold':>7}{'endPrice':>10}{'gross~':>10}")
    tot = 0
    for p in K.PRODUCTS:
        sold = st['inv'][p] - 10000 + st['drain'][p]
        pr = K.market_price(p, st['inv'][p])
        g = K.sale_revenue if False else None
        # approximate gross: integrate price from I0-drain up to final inventory
        inv = 10000 - st['drain'][p]
        gross = 0
        for _ in range(max(0, int(sold))):
            v = K.market_price(p, inv); gross += v
            if v > 1: inv += 1
        tot += gross
        print(f"{p:<12}{sold:>7.0f}{pr:>10}{gross:>10.0f}")
    print(f"{'TOTAL':<12}{'':>7}{'':>10}{tot:>10.0f}")

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else "pass",
        int(sys.argv[3]) if len(sys.argv)>3 else 1)
