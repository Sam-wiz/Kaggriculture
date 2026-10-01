import sys, collections
sys.path.insert(0, '.')
import harness

CLONE = sys.argv[2] if len(sys.argv) > 2 else 'moe/r7/build/devin/clone_dsm_bc.py'
V8X = 'agents/v8x.py'

def snap(state, i):
    obs = state[i].observation
    f = obs.farms[i]
    priv = obs.private or {}
    shed = priv.get('shed') or {}
    seeds = priv.get('seeds') or {}
    crops = collections.Counter(); animals = collections.Counter(); weeds = 0
    structs = collections.Counter()
    for row in f['tiles']:
        for t in row:
            if not isinstance(t, dict): continue
            k = t.get('kind')
            if k == 'PLANT': crops[t.get('crop')] += 1
            elif k == 'WEED': weeds += 1
            elif k in ('COOP', 'PASTURE'):
                structs[k] += 1
                a = t.get('animal')
                if a: animals[a if isinstance(a, str) else a.get('kind')] += 1
    return dict(money=f['money'], hands=len(f.get('hands') or []),
                crops=dict(crops), animals=dict(animals), weeds=weeds,
                structs=dict(structs), shed=dict(shed), seeds=dict(seeds),
                shed_tot=sum(shed.values()))

def main(seed=8001):
    days = {0: {}, 1: {}}
    last = {}
    def cb(step, state, env):
        d = int(state[0].observation.day)
        for i in (0, 1):
            last[i] = (d, snap(state, i))
        days[0][d] = last[0][1]
        days[1][d] = last[1][1]
    r = harness.run_episode(CLONE, V8X, seed=seed, on_step=cb)
    print('reward', r['reward'], 'status', r['status'], 'errors', r['errors'])
    for d in range(30):
        a, b = days[0].get(d), days[1].get(d)
        if not a or not b: continue
        print(f"d{d:2d} | clone ${a['money']:6.0f} h{a['hands']:2d} an{a['animals']} sh{a['shed_tot']:3d} "
              f"cr{ {k:v for k,v in a['crops'].items()} } w{a['weeds']} | "
              f"v8x ${b['money']:6.0f} h{b['hands']:2d} an{b['animals']} sh{b['shed_tot']:3d} "
              f"cr{ {k:v for k,v in b['crops'].items()} } w{b['weeds']}")
    print('clone final shed:', days[0].get(29, {}).get('shed'))
    print('v8x  final shed:', days[1].get(29, {}).get('shed'))
    print('clone seeds:', days[0].get(29, {}).get('seeds'))
    print('clone structs:', days[0].get(29, {}).get('structs'), 'v8x structs:', days[1].get(29, {}).get('structs'))

if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 8001)
