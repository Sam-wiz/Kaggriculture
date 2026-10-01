# pipe16 variant factory: rebuild _IMPL with different layer flags / opponent_plan
import sys, os, importlib.util, copy, collections

def loadmod(name, path):
    d = os.path.dirname(os.path.abspath(path))
    if d not in sys.path: sys.path.insert(0, d)
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

P16 = 'rivals/kaggriculture-pipe16-idle-workers/_entry.py'

def make_variant(flags=None, plan_mode=None, name='v'):
    """plan_mode: None | 'self' (own route's sells) | 'union' (all routes' sell union)"""
    m = loadmod('p16_' + name, P16)
    st = {'hand_align': True, 'weed_repair': True, 'sell_lead': True,
          'budget_guard': False, 'room_guard': False, 'clamp_sells': False,
          'dead_stock': False, 'terminal_liquidation': False, 'front_run': False}
    st.update(flags or {})
    plan = None
    if plan_mode == 'union':
        # union of all routes' market orders per step (superset of any rival tape)
        routes = list(m._ROUTES.values())
        plan = []
        for t in range(720):
            agg = {}
            for r in routes:
                a = r[t] if t < len(r) and isinstance(r[t], dict) else {}
                for o in a.get('market') or []:
                    if o and o[0] == 'SELL' and len(o) >= 3:
                        agg[o[1]] = max(agg.get(o[1], 0), o[2])
            plan.append({'market': [['SELL', k, v] for k, v in agg.items()]})
    m._IMPL = m.make_agent(m._ROUTES, router=m._router, opponent_plan=plan, **st)
    # wrappers increment diagnostics keys added post-build on the original chassis;
    # a defaultdict keeps those counters working on the rebuilt chassis
    m._IMPL.chassis.diagnostics = collections.defaultdict(int,
        m._IMPL.chassis.diagnostics)
    return m

if __name__ == '__main__':
    # smoke: each variant loads and answers an obs
    import kagsim
    for flags, pm, nm in [({}, None, 'base'),
                          ({'budget_guard': True, 'room_guard': True, 'clamp_sells': True,
                            'dead_stock': True, 'terminal_liquidation': True}, None, 'allon'),
                          ({'front_run': True}, 'union', 'fr_union')]:
        v = make_variant(flags, pm, nm)
        g = kagsim.Game(seed=1)
        a = v.agent(g.observe(0))
        print(nm, 'ok', list(a.keys()), len(a.get('market') or []))
