"""T3 — top-team ROUTER: fixed recorded prefix for steps 0..143, then at the dawn of day 6 (obs step 144, units
respawn so the splice is positionally safe) switch to a recorded continuation chosen by the first two shops.
Closed-loop vs a live agent on fresh seeds (both seats). kagsim.

Router spec (JSON): {"prefix": [path, seat], "routes": {"SHOP1|SHOP2": [path, seat]}, "default": [path, seat],
                     "switch": 144}
Job: {spec: file, seed, pos (router seat), live: path, tag}
usage: t3.py OUT.jsonl JOBS.json WORKERS
"""
import gzip, json, os, sys, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT); sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r3/build/opus")
sys.path.insert(0, ROOT + "/moe/r4/build/opusb")
from run import load, act, PASS
from t1 import TELE
import kagsim

_EP = {}


def seat_actions(path, seat):
    k = (path, seat)
    if k not in _EP:
        d = json.load(gzip.open(os.path.join(ROOT, path), "rt"))
        _EP[k] = [a[seat] if isinstance(a[seat], dict) else None for a in d["actions"]]
    return _EP[k]


class Router:
    def __init__(self, spec):
        self.spec = spec; self.sw = int(spec.get("switch", 144))
        self.prefix = seat_actions(*spec["prefix"]); self.cur = None; self.route = None

    def __call__(self, obs):
        t = int(obs["step"])
        if t < self.sw:
            tape = self.prefix
        else:
            if self.cur is None:
                key = "|".join(obs["town"]["unlocked_shops"][:2])
                r = self.spec["routes"].get(key) or self.spec["default"]
                self.route = key if key in self.spec["routes"] else "default"
                self.cur = seat_actions(*r)
            tape = self.cur
        a = tape[t + 1] if t + 1 < len(tape) else None
        return a if isinstance(a, dict) else PASS


def job(j):
    t0 = time.time()
    try:
        R = Router(json.load(open(os.path.join(ROOT, j["spec"]))))
        fn, m = load(j["live"], "lv"); O = lambda o: act(fn, o)
        p = j["pos"]; g = kagsim.Game(seed=int(j["seed"]))
        for t in range(720):
            o0, o1 = g.observe(0), g.observe(1)
            g.step(R(o0) if p == 0 else O(o0), O(o1) if p == 0 else R(o1))
        r = [float(g.reward(0)), float(g.reward(1))]
        o = g.observe(0)
        return dict(j, me=r[p], opp=r[1 - p], route=R.route, shops=list(o["town"]["unlocked_shops"]),
                    tele={k: g.telemetry(p).get(k) for k in TELE}, s=round(time.time() - t0, 1))
    except Exception as e:
        import traceback
        return dict(j, err=traceback.format_exc()[-300:])


if __name__ == "__main__":
    out, jobs, W = sys.argv[1], json.load(open(sys.argv[2])), int(sys.argv[3])
    key = lambda r: (r["spec"], r["seed"], r["pos"], r["live"])
    done = set()
    if os.path.exists(out):
        for line in open(out):
            done.add(key(json.loads(line)))
    jobs = [j for j in jobs if key(j) not in done]
    print(len(jobs), "jobs", flush=True)
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=W) as ex, open(out, "a") as f:
        for i, r in enumerate(ex.map(job, jobs, chunksize=1), 1):
            f.write(json.dumps(r, ensure_ascii=False) + "\n"); f.flush()
            if i % 10 == 0: print(i, flush=True)
