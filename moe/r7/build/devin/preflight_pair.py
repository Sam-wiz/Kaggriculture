"""Preflight the staged pair: Kaggle loader, strict exceptions (v8), official env BOTH seats."""
import sys, os
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"; os.chdir(ROOT)
sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/r3/build/opus")
from kaggle_load_check import load_like_kaggle
from run import load, act
import kagsim

for path in ("subAB_m30b.py", "subAC_v8.py"):
    fn = load_like_kaggle(path)
    print(path, "last-callable:", fn.__name__)
    if "v8" in path:
        src = open(path).read()
        caught = '        except Exception:\n            return {"farmer": ["PASS"], "hands": [], "market": []}'
        assert src.count(caught) == 1, src.count(caught)
        open("/tmp/v8_strict.py", "w").write(src.replace(caught, '        except Exception:\n            raise', 1))
        a, _ = load("/tmp/v8_strict.py", "s")
        for seat in (0, 1):
            for seed in (9900001, 9900002):
                g = kagsim.Game(seed=seed)
                for t in range(719):
                    if seat == 0: g.step(act(a, g.observe(0)), ["PASS"])
                    else:         g.step(["PASS"], act(a, g.observe(1)))
                print(f"  strict seat{seat} seed{seed}: reward {g.reward(seat):.0f} (no exceptions)")
    from kaggle_environments import make
    for seat in (0, 1):
        env = make("kaggriculture", configuration={"episodeSteps": 720})
        env.run([path, "starter"] if seat == 0 else ["starter", path])
        st = [s.status for s in env.steps[-1]]; rw = [s.reward for s in env.steps[-1]]
        print(f"  official env seat{seat}: {st} rewards={[round(r) if isinstance(r,float) else r for r in rw]} -> {'OK' if st[seat]=='DONE' else 'FAIL'}")
