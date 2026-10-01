"""Shared kagsim runners for arm W1 / R (Opus r3 build). All scratch stays in moe/r3/build/opus/."""
import sys, os, json, gzip, importlib.util, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT); sys.path.insert(0, ROOT)
sys.path.insert(0, ROOT + "/kaggriculture-cppsim")
import kagsim
PASS = {"farmer": ["PASS"], "hands": [], "market": []}
_N = [0]
def load(path, tag):
    _N[0] += 1; name = "O_%s_%d_%d" % (tag, os.getpid(), _N[0])
    ap = os.path.join(ROOT, path); cwd = os.getcwd(); os.chdir(os.path.dirname(ap))
    try:
        spec = importlib.util.spec_from_file_location(name, ap); m = importlib.util.module_from_spec(spec)
        sys.modules[name] = m; spec.loader.exec_module(m)
    finally: os.chdir(cwd)
    f = None
    for k, v in list(vars(m).items()):
        if callable(v) and not isinstance(v, type) and getattr(v, '__module__', None) == m.__name__: f = v
    return (getattr(m, 'agent', None) or f), m
def act(fn, o):
    try:
        a = fn(o)
        return a if isinstance(a, dict) else PASS
    except Exception:
        return PASS
def tele(m):
    return dict(P=dict(getattr(m, '_V92_P_REPORT', {}) or {}), Q=dict(getattr(m, '_V92_Q_REPORT', {}) or {}))
def selfplay(job):
    """job=(name, path, seed): same agent both seats; returns the rival stream each seat recovered (_v92_p_update)."""
    name, path, seed = job
    a, ma = load(path, "a"); b, mb = load(path, "b")
    g = kagsim.Game(seed=int(seed)); pair = None
    for t in range(720):
        o0, o1 = g.observe(0), g.observe(1)
        if t == 150: pair = tuple(o0["town"]["unlocked_shops"][:2])
        g.step(act(a, o0), act(b, o1))
    r = [float(g.reward(0)), float(g.reward(1))]
    s_of_1 = {"%d,%d" % k: v for k, v in ma._V92_P[0]["obs"].items()}   # seat-1 sales as seen by seat 0
    s_of_0 = {"%d,%d" % k: v for k, v in mb._V92_P[1]["obs"].items()}
    return dict(name=name, seed=int(seed), pair=pair, r=r, streams=[s_of_0, s_of_1])
def closed(job):
    """job=(xname, xpath, oname, opath, seed, us): x plays seat `us`; returns x's margin + both telemetries."""
    xn, xp, on, op, seed, us = job
    a, ma = load(xp, "x"); b, mb = load(op, "o")
    g = kagsim.Game(seed=int(seed))
    for t in range(720):
        o0, o1 = g.observe(0), g.observe(1)
        A, B = (a, b) if us == 0 else (b, a)
        g.step(act(A, o0), act(B, o1))
    r = [float(g.reward(0)), float(g.reward(1))]
    return dict(x=xn, o=on, seed=int(seed), us=us, m=r[us] - r[1 - us], r=r, tx=tele(ma), to=tele(mb))
def pool(fn, jobs, out, workers=2):
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=workers) as ex, open(out, "a") as f:
        for res in ex.map(fn, jobs, chunksize=1):
            f.write(json.dumps(res) + "\n"); f.flush()
if __name__ == "__main__":
    t0 = time.time(); r = selfplay(("shep", "subW_shepherd.py", 12345))
    print(r["pair"], r["r"], [len(s) for s in r["streams"]], round(time.time() - t0, 1), "s")
