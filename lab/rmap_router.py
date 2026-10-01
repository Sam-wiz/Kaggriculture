"""Progressive route filter: re-pick best route among prefix-feasible set as shops reveal.

Contract with the fit: _RMAP_MODEL = {'intercept': {r: a}, 'beta': {r: {shop: b}},
'default': {class_or_pair: route}} — predicted margin = a_r + sum_s b_{r,s}*count_s.
Feasible(r, t): routes[r][:t] identical to current route's tape[:t].
Only switches when predicted gain > _RMAP_MIN_GAIN and the candidate differs.
"""
import ast, json, zlib, base64, collections

def build_rmap_agent(src_path, model, min_gain=400.0):
    """Return (agent, internals) — loads src agent, wraps router with the filter."""
    env = {}
    exec(compile(open(src_path).read(), src_path, 'exec'), env)
    impl = env['_IMPL']
    routes = impl.chassis.routes
    rids = sorted(r for r in routes if r != 1)
    # precompute prefix keys at every step lazily via bisect-free memo
    import json as _j
    _pkey_cache = {}
    def pkey(r, t):
        k = (r, t)
        if k not in _pkey_cache:
            _pkey_cache[k] = _j.dumps(routes[r][:t], sort_keys=True)
        return _pkey_cache[k]
    def feasible(cur, t):
        ck = pkey(cur, t)
        return [r for r in rids if pkey(r, t) == ck]
    def pred_margin(r, counts):
        return model['intercept'].get(str(r), model['intercept'].get(r, 0.0)) + sum(
            model['beta'].get(str(r), model['beta'].get(r, {})).get(s, 0.0) * c
            for s, c in counts.items())
    orig_router = env['_router']
    def rmap_router(observation, step, state):
        r = orig_router(observation, step, state)
        cur = state.get('route', r)
        if cur not in routes:
            cur = r
        shops = tuple((_get(_get(observation, 'town', {}), 'unlocked_shops', []) or []))
        if shops != state.get('_rmap_shops'):
            state['_rmap_shops'] = shops
            if step >= 144 and not state.get('day27'):
                counts = dict(collections.Counter(shops))
                cand = feasible(cur, step)
                if len(cand) > 1:
                    best = max(cand, key=lambda x: pred_margin(x, counts))
                    if pred_margin(best, counts) - pred_margin(cur, counts) > min_gain:
                        state['route'] = best
                        state['_rmap_switches'] = state.get('_rmap_switches', 0) + 1
                        return best
        return state.get('route', r)
    impl.chassis.router = rmap_router
    return env['agent'], env
