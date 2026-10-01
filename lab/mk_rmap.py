"""Emit subV_sirxL96_rmap.py: L96 + fitted progressive route filter.

Appends a wrapper that (a) keeps the shipped router's bookkeeping, (b) at every
new shop unlock re-picks argmax predicted margin among prefix-feasible routes,
(c) never overrides the V93 rival-signature route, (d) never switches past the
route's own prefix-class boundary.
"""
import json, sys

MODEL = json.load(open('route_models.json'))['models']
MIN_GAIN = float(sys.argv[1]) if len(sys.argv) > 1 else 400.0
SRC = sys.argv[2] if len(sys.argv) > 2 else 'subV_sirxL96.py'
OUT = sys.argv[3] if len(sys.argv) > 3 else 'subV_sirxL96_rmap.py'

src = open(SRC).read()
block = '''

# ==== RMAP: fitted progressive route filter (r5) ====
# Per-route ridge margins over shop-count features measured on the
# shop-decoupled engine (clean draws). At each newly-unlocked shop, re-picks
# the argmax-margin route among routes whose tape still matches the played
# prefix. V93 rival-signature route is never overridden.
import collections as _rm_col
_RM_PARENT_ROUTER = _router
_RM_COEF = %r
_RM_SHOPS = ['BAKERY', 'BRUNCH_SPOT', 'FARMERS_MARKET', 'ICE_CREAM_SHOP', 'PET_CAFE', 'PIZZA_SHOP', 'SMOOTHIE_SHOP', 'YARN_STORE']
_RM_MIN_GAIN = %r
_RM_PKEY = {}
_RM_RIDS = sorted(r for r in _ROUTES if r != 1)


def _rm_pkey(r, t):
    k = (r, t)
    if k not in _RM_PKEY:
        _RM_PKEY[k] = json.dumps(_ROUTES[r][:t], sort_keys=True)
    return _RM_PKEY[k]


def _rm_pred(r, counts, k_seen):
    c = _RM_COEF.get(r) or _RM_COEF.get(str(r))
    if c is None:
        return None
    rem = (8 - k_seen) / 8.0
    v = c[0]
    for i, s in enumerate(_RM_SHOPS):
        v += c[i + 1] * (counts.get(s, 0) + rem)
    return v


def _router(observation, step, state):
    r = _RM_PARENT_ROUTER(observation, step, state)
    cur = state.get('route', r)
    if cur not in _ROUTES:
        cur = r
    shops = tuple((_get(_get(observation, 'town', {}), 'unlocked_shops', []) or []))
    if shops == state.get('_rm_shops'):
        return state.get('route', r)
    state['_rm_shops'] = shops
    if step < 144 or state.get('day27'):
        return state.get('route', r)
    if 'YARN_STORE' in shops and state.get('rkey') in _V93_ROUTE_BY_RIVAL:
        return state.get('route', r)
    ck = _rm_pkey(cur, step)
    feas = [x for x in _RM_RIDS if _rm_pkey(x, step) == ck]
    if len(feas) < 2:
        return state.get('route', r)
    counts = dict(_rm_col.Counter(shops))
    k_seen = len(shops)
    best, best_v = cur, _rm_pred(cur, counts, k_seen)
    for x in feas:
        v = _rm_pred(x, counts, k_seen)
        if v is not None and (best_v is None or v > best_v):
            best, best_v = x, v
    if best != cur and best_v is not None:
        base_v = _rm_pred(cur, counts, k_seen)
        if base_v is None or best_v - base_v > _RM_MIN_GAIN:
            state['route'] = best
            state['_rm_switches'] = state.get('_rm_switches', 0) + 1
            return best
    return state.get('route', r)


# chassis bound the original _router at construction — rebind to the filter
_IMPL.chassis.router = _router
''' % (MODEL, MIN_GAIN)

open(OUT, 'w').write(src + block)
print("wrote", OUT, "| routes with models:", len(MODEL), "| min_gain:", MIN_GAIN)
