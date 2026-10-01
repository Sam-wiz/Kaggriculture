"""
r5 sonnet — real-engine vs kagsim speed, for Architecture B (runtime planning) feasibility.

Measures the ONE number that decides whether "simulate candidate plans forward with the engine
and pick the best" (BRIEF architecture B) can run inside an actual Kaggle submission:
- kagsim (kaggriculture-cppsim/*.so) is what every RR/gate/ceiling script in this repo uses for
  speed, but it is a compiled macOS arm64 pybind11 extension. It cannot be embedded in a
  single-file (or tar.gz) Kaggle submission: wrong OS/arch for the judge host, and there is no
  guarantee the judge sandbox permits loading an arbitrary .so at all.
- The real interpreter (kaggle_environments.envs.kaggriculture.kaggriculture, pure Python, what
  the Kaggle judge actually runs) is therefore the *only* honest reference for what an in-submission
  forward simulator could achieve, since a bespoke pure-Python reimplementation would run at
  roughly this order of magnitude, not kagsim's.

Run: .venv/bin/python moe/r5/build/sonnet/bench_realengine.py
"""
import sys
import time

sys.path.insert(0, "kaggriculture-cppsim")


def bench_real_engine():
    import kaggle_environments as ke

    # trivial policy (lower bound on interpreter+harness overhead)
    env = ke.make("kaggriculture", configuration={"episodeSteps": 720}, debug=False)
    t0 = time.perf_counter()
    env.run(["pass", "pass"])
    t1 = time.perf_counter()
    trivial_ms_per_frame = (t1 - t0) / 720 * 1000
    print(f"[real engine, pure python] pass/pass   : {t1-t0:.3f}s / 720 steps = {trivial_ms_per_frame:.3f} ms/frame")

    # realistic policy complexity (two actual candidate agents from this repo)
    env = ke.make("kaggriculture", configuration={"episodeSteps": 720}, debug=False)
    t0 = time.perf_counter()
    env.run(["subX_hyb2965.py", "subY_C1_predict2.py"])
    t1 = time.perf_counter()
    real_ms_per_frame = (t1 - t0) / 720 * 1000
    print(f"[real engine, pure python] hyb2965/C1  : {t1-t0:.3f}s / 720 steps = {real_ms_per_frame:.3f} ms/frame")
    return trivial_ms_per_frame, real_ms_per_frame


def bench_kagsim():
    import kagsim

    n_games = 20
    t0 = time.perf_counter()
    for i in range(n_games):
        g = kagsim.Game(9100000 + i, 720)
        while not g.done:
            g.step({"farmer": ["PASS"], "hands": [], "market": []},
                    {"farmer": ["PASS"], "hands": [], "market": []})
    t1 = time.perf_counter()
    dt = t1 - t0
    us_per_frame = dt / n_games / 720 * 1e6
    print(f"[kagsim, compiled C++]    pass/pass   : {n_games} games in {dt:.3f}s = {us_per_frame:.2f} us/frame")
    return us_per_frame


if __name__ == "__main__":
    print("platform check: kaggriculture-cppsim/kagsim.cpython-314-darwin.so is a macOS arm64")
    print("Mach-O bundle (checked with `file`). Kaggle's judge host is linux/x86_64. This binary")
    print("cannot run there; a from-scratch pure-Python reimplementation is the only embeddable option.")
    print()
    trivial_ms, real_ms = bench_real_engine()
    us_frame = bench_kagsim()
    print()
    print(f"Speed ratio real-engine(trivial)/kagsim  : {trivial_ms*1000/us_frame:.0f}x slower")
    print(f"Speed ratio real-engine(real agents)/kagsim: {real_ms*1000/us_frame:.0f}x slower")
    print()
    print("Conclusion: any embeddable forward simulator for architecture B must be judged against")
    print(f"the {real_ms:.1f} ms/frame (realistic policy cost) to {trivial_ms:.2f} ms/frame (best case,")
    print("near-trivial surrogate policies) real-engine numbers above, not kagsim's. See budget_calc.py")
    print("for what that implies about how much lookahead fits in the 60s remainingOverageTime pool.")
