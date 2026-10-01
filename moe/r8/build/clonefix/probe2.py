import sys, collections
sys.path.insert(0, '.')
import harness

def main(agent_path, seed=8001, seat=0):
    ops = collections.Counter()          # day -> op counts
    dmoney = collections.Counter()
    last_money = [None, None]
    sells = collections.Counter()        # day -> qty sold (sum of SELL n)
    def cb(step, state, env):
        d = int(state[0].observation.day)
        act = state[seat].action or {}
        for op in [act.get('farmer')] + (act.get('hands') or []):
            if op: ops[d] += 1; ops[(d, op[0])] += 1
        for o in (act.get('market') or []):
            if o[0] == 'SELL': sells[d] += o[2]
        m = state[seat].observation.farms[seat]['money']
        if last_money[seat] is not None:
            dmoney[d] += m - last_money[seat]
        last_money[seat] = m
    r = harness.run_episode(agent_path, 'agents/v8x.py', seed=seed, on_step=cb)
    print('reward', r['reward'], 'errors', r['errors'])
    for d in range(30):
        opstr = {k[1]: v for k, v in ops.items() if isinstance(k, tuple) and k[0] == d}
        print(f"d{d:2d} dmoney={dmoney[d]:+7.0f} sells_n={sells[d]:4d} ops={opstr}")

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'moe/r8/build/clonefix/clone_dsm_bc2.py',
         int(sys.argv[2]) if len(sys.argv) > 2 else 8001)
