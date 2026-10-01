"""Shared helpers for the r4 FABLE build. kagsim runners; tape agents; hybrid (unit-forced) agents.
Convention (BRIEF): actions[t] PRODUCED step t; the reply to obs t is actions[t+1].
"""
import gzip, json, os, sys, importlib.util, glob
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
HERE = os.path.join(ROOT, "moe/r4/build/fable")
os.chdir(ROOT)
for p in (ROOT, ROOT + "/kaggriculture-cppsim"):
    if p not in sys.path: sys.path.insert(0, p)
import kagsim
try: os.nice(10)
except Exception: pass

PASS = {"farmer": ["PASS"], "hands": [], "market": []}
PRODUCTS7 = ("MILK", "WOOL", "STRAWBERRY", "EGG", "MELON", "TOMATO", "CARROT")   # sell-all scope (never WHEAT/FERT: farm inputs)
INPUTS = ("WHEAT", "FERTILIZER")
MAX_ORDERS = 10
C1 = "subY_C1_predict2.py"; SHEP = "subW_shepherd.py"; HYB = "subX_hyb2965.py"
_N = [0]

def load_agent(path, tag="a"):
    """Fresh module per game (layer state is module-level). Returns (callable, module)."""
    _N[0] += 1; name = "F_%s_%d_%d" % (tag, os.getpid(), _N[0])
    ap = os.path.join(ROOT, path); cwd = os.getcwd(); os.chdir(os.path.dirname(ap))
    try:
        spec = importlib.util.spec_from_file_location(name, ap); m = importlib.util.module_from_spec(spec)
        sys.modules[name] = m; spec.loader.exec_module(m)
    finally: os.chdir(cwd)
    f = None
    for k, v in list(vars(m).items()):
        if callable(v) and not isinstance(v, type) and getattr(v, "__module__", None) == m.__name__: f = v
    return (getattr(m, "agent", None) or f), m

def act(fn, o):
    try:
        a = fn(o)
        return a if isinstance(a, dict) else PASS
    except Exception:
        return PASS

def load_ep(path):
    return json.load(gzip.open(path, "rt"))

def top10_files():
    return sorted(glob.glob(os.path.join(ROOT, "mine/top10/*.json.gz")))

def rec_action(acts, t, seat):
    a = acts[t + 1][seat] if t + 1 < len(acts) else None
    return a if isinstance(a, dict) else PASS

def tape_agent(acts, seat, fix_hands=False):
    """Open-loop replay of one recorded seat. fix_hands: trim/pad the hands list to the hands we actually have."""
    def ag(obs):
        a = rec_action(acts, obs["step"], seat)
        if not fix_hands: return a
        hands = list(a.get("hands") or []); have = len(obs["farms"][obs["player"]].get("hands") or [])
        if len(hands) > have: hands = hands[:have]
        elif len(hands) < have: hands += [["PASS"]] * (have - len(hands))
        return {"farmer": a.get("farmer") or ["PASS"], "hands": hands, "market": list(a.get("market") or [])[:MAX_ORDERS]}
    return ag

def is_sell_of(o, items):
    return isinstance(o, (list, tuple)) and len(o) >= 3 and o[0] == "SELL" and o[1] in items

def sell_all_orders(obs, items=PRODUCTS7):
    shed = obs["private"]["shed"]
    return [["SELL", p, int(shed[p])] for p in items if shed.get(p, 0) > 0]

def hybrid_agent(acts, seat, market_fn, fix_hands=True):
    """Unit ops + non-product-SELL market orders from the recorded tape; product SELL orders from market_fn(obs)
    (a callable returning a list of orders; only its SELL orders on PRODUCTS7 are used)."""
    base = tape_agent(acts, seat, fix_hands=fix_hands)
    def ag(obs):
        a = base(obs)
        keep = [o for o in (a.get("market") or []) if not is_sell_of(o, PRODUCTS7)]
        try: mine = [o for o in (market_fn(obs) or []) if is_sell_of(o, PRODUCTS7)]
        except Exception: mine = []
        return {"farmer": a.get("farmer") or ["PASS"], "hands": a.get("hands") or [], "market": (keep + mine)[:MAX_ORDERS]}
    return ag

def agent_market_fn(fn):
    """Wrap a full agent so it yields only its market list."""
    def mf(obs):
        return act(fn, obs).get("market") or []
    return mf

def run_game(a0, a1, seed, trace_days=False):
    g = kagsim.Game(seed=int(seed)); money = [[], []]
    for t in range(720):
        o0, o1 = g.observe(0), g.observe(1)
        if trace_days and t % 24 == 0:
            for s in (0, 1): money[s].append(o0["farms"][s]["money"])
        g.step(act(a0, o0), act(a1, o1))
    o0 = g.observe(0)
    r = [float(g.reward(0)), float(g.reward(1))]
    return dict(r=r, shops=list(o0["town"]["unlocked_shops"]), money=money, tele=[dict(g.telemetry(0)), dict(g.telemetry(1))])

def pool(fn, jobs, out, workers=2):
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=workers) as ex, open(out, "a") as f:
        for res in ex.map(fn, jobs, chunksize=1):
            f.write(json.dumps(res) + "\n"); f.flush()
