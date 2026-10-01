"""Parity of kagsim Game.from_obs (r5 opus patch): run a recorded top game on the OFFICIAL Python engine
(harness) to step t, capture both seats' observations (incl. private), build kagsim from seat 0's obs
(+ seat 1's private), pin the recorded shop list, then step both recorded tapes to the end in kagsim.
Pass = final banks equal the recorded rewards to the dollar.  Also: speed of from_obs + full rollout.
usage: fo_parity.py N_GAMES STEPS(comma)"""
import sys, os, glob, gzip, json, copy, time
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT + "/moe/r5/build/opus/kagsim_src"); sys.path.insert(0, ROOT)
import kagsim, harness
assert hasattr(kagsim.Game, "from_obs")
PASS = {"farmer": ["PASS"], "hands": [], "market": []}
N = int(sys.argv[1]); STEPS = [int(x) for x in sys.argv[2].split(",")]
ok = tot = 0; tb = []; fails = []
for p in sorted(glob.glob("mine/top10/*.json.gz"))[:N]:
    d = json.load(gzip.open(p, "rt")); acts = d["actions"]
    A = lambda t, s: acts[t + 1][s] if t + 1 < len(acts) and isinstance(acts[t + 1][s], dict) else PASS
    snaps = {}
    class Stop(Exception): pass
    def mk(seat):
        def ag(obs):
            if obs["step"] in STEPS: snaps.setdefault(obs["step"], {})[seat] = copy.deepcopy(dict(obs))
            if obs["step"] > max(STEPS): raise Stop()
            return A(obs["step"], seat)
        return ag
    try: harness.run_episode(mk(0), mk(1), seed=d["seed"], copy_obs=False, catch_errors=False)
    except Stop: pass
    for t in STEPS:
        o0, o1 = snaps[t][0], snaps[t][1]
        def plain(x):
            if isinstance(x, dict): return {k: plain(v) for k, v in x.items()}
            if isinstance(x, list): return [plain(v) for v in x]
            return x
        o0 = plain(o0); pv1 = plain(o1)["private"]
        t0 = time.perf_counter()
        g = kagsim.Game.from_obs(o0, d["seed"], d["shops"], pv1)
        for s in range(t, 720): g.step(A(s, 0), A(s, 1))
        tb.append(time.perf_counter() - t0)
        r = [g.reward(0), g.reward(1)]; tot += 1
        good = all(abs(a - b) < 0.5 for a, b in zip(r, d["rewards"]))
        ok += good
        if not good: fails.append((os.path.basename(p), t, r, d["rewards"]))
print(f"from_obs parity: {ok}/{tot} exact  (steps {STEPS}); mean from_obs+rollout(py-dict actions) {1000*sum(tb)/len(tb):.1f} ms")
for f in fails[:8]: print("  FAIL", f)
