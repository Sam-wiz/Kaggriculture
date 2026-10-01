"""Where the money comes from and goes, per phase."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness
from kaggle_environments.envs.kaggriculture import kaggriculture as K

def run(path, opp="starter", seed=1, bands=((0,6),(6,12),(12,20),(20,30))):
    inner = harness.load_agent(path)
    rev = [collections.Counter() for _ in bands]
    spend = [collections.Counter() for _ in bands]
    prev = {}
    state = {}
    def wrapped(obs):
        a = inner(obs)
        d = obs["day"]
        bi = next((i for i,(lo,hi) in enumerate(bands) if lo <= d < hi), None)
        state['obs'] = obs
        state['bi'] = bi
        state['orders'] = a.get("market", [])
        return a
    # we can't see fills directly; approximate using price x qty at order time
    def on_step(step, st, env):
        bi = state.get('bi')
        if bi is None: return
        obs = state['obs']; pr = obs["market"]["prices"]
        shed_before = state.get('shed_before')
        for o in state['orders'][:10]:
            if not o: continue
            if o[0] == "SELL" and len(o) > 2:
                rev[bi][o[1]] += 0  # filled amount unknown here
            elif o[0] == "BUY_SEED" and len(o) > 2:
                spend[bi]["seed:"+o[1]] += K.CROPS[o[1]]["seed"] * int(o[2])
            elif o[0] == "BUY_ANIMAL" and len(o) > 2:
                spend[bi]["animal:"+o[1]] += K.ANIMALS[o[1]]["cost"] * int(o[2])
            elif o[0] == "BUY_PRODUCT" and len(o) > 2:
                spend[bi]["buy:"+o[1]] += pr[o[1]] * int(o[2])
            elif o[0] == "BUY_LAND":
                spend[bi]["land"] += 1
            elif o[0] == "HIRE":
                spend[bi]["hire"] += 1
    # track revenue by differencing market inventory attributable to our sells is
    # unreliable with two sellers, so instead track shed decrements x price
    log = []
    prev_shed = {}
    prev_money = [None]
    def on_step2(step, st, env):
        on_step(step, st, env)
        bi = state.get('bi')
        obs = state['obs']
        me = obs["player"]
        priv = st[me].observation.private
        shed = priv["shed"]
        pr = obs["market"]["prices"]
        if bi is not None and prev_shed:
            for k, v in prev_shed.items():
                d = v - shed.get(k, 0)
                if d > 0 and k in pr:
                    rev[bi][k] += d * pr[k]
        prev_shed.clear(); prev_shed.update(shed)
    r = harness.run_episode(wrapped, opp, seed=seed, on_step=on_step2, catch_errors=False)
    print(f"{path} vs {opp} seed={seed} final={r['reward']}")
    for i,(lo,hi) in enumerate(bands):
        print(f"\n== days {lo}-{hi}")
        print("  revenue (shed outflow x price, approx):",
              {k:int(v) for k,v in rev[i].most_common() if v>50})
        print("  spend:", {k:int(v) for k,v in spend[i].most_common()})

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else "starter",
        int(sys.argv[3]) if len(sys.argv)>3 else 1)
