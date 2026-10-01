"""Prove the micro-farm exists before measuring what it earns.

Every failed production change in this project looked like a working null result because the thing
it was supposed to create never came into being: the herd swap bought sheep that never became
animals, and a ported overlay raised NameError on 714 of 719 turns. So this counts the entity, not
its downstream traces -- land unlocked, pastures built, sheep standing on them, the extra hand
existing and acting, wool produced -- and only then reports the bank.
"""
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

PLOT = [(6, 5), (5, 6), (6, 6), (7, 5), (5, 7), (7, 6), (6, 7), (7, 7)]
OPP = "rivals/leoprovorov_kaggriculture-v65/main.py"


def probe(agent, seed):
    st = dict(land_day=None, pastures=0, sheep_on_plot=0, extra_hand_turns=0,
              acts=collections.Counter(), wool_sold=0, hires=0, wheat_bought=0,
              max_hands=0, sheep_bought=0)

    def on_step(step, state, env):
        farm = state[0].observation.farms[0]
        a = state[0].action or {}
        tape_hands = len(a.get("hands") or [])
        st["max_hands"] = max(st["max_hands"], len(farm["hands"]))
        for o in (a.get("market") or []):
            if not o:
                continue
            if o[0] == "BUY_LAND" and st["land_day"] is None:
                st["land_day"] = step // 24
            elif o[0] == "HIRE":
                st["hires"] += 1
            elif o[0] == "BUY_PRODUCT" and len(o) > 1 and o[1] == "WHEAT":
                st["wheat_bought"] += int(o[2]) if len(o) > 2 else 1
            elif o[0] == "BUY_ANIMAL" and len(o) > 1 and o[1] == "SHEEP":
                st["sheep_bought"] += int(o[2]) if len(o) > 2 else 1
            elif o[0] == "SELL" and len(o) > 2 and o[1] == "WOOL":
                st["wool_sold"] += int(o[2])
        if step > 700:
            p = s = 0
            for (x, y) in PLOT:
                try:
                    t = farm["tiles"][y][x]
                except Exception:
                    continue
                if isinstance(t, dict) and t.get("kind") == "PASTURE":
                    p += 1
                    if "animal" in t:
                        s += 1
            st["pastures"], st["sheep_on_plot"] = p, s

    r = harness.run_episode(agent, OPP, seed=seed, copy_obs=False, on_step=on_step,
                            catch_errors=True)
    st["bank"] = r["reward"][0]
    st["opp"] = r["reward"][1]
    return st


if __name__ == "__main__":
    cand = sys.argv[1] if len(sys.argv) > 1 else "bench_frozen/MF_s4y2.py"
    base = sys.argv[2] if len(sys.argv) > 2 else "sub_herd.py"
    idx = json.load(open("data/seedindex_900000_1400.json"))
    hi = [r["seed"] for r in idx if r["yarn"] >= 3][:4]
    lo = [r["seed"] for r in idx if r["yarn"] == 0][:2]
    print(f"candidate: {cand}\n")
    print(f"{'seed':>8}{'yarn':>5}  {'agent':<6}{'landDay':>8}{'past':>6}{'sheep':>6}"
          f"{'hires':>7}{'wheat':>7}{'woolSold':>10}{'maxHands':>10}{'bank':>10}")
    for tag, seeds in (("HIGH", hi), ("ZERO", lo)):
        for sd in seeds:
            y = next(r["yarn"] for r in idx if r["seed"] == sd)
            for nm, p in (("base", base), ("micro", cand)):
                st = probe(p, sd)
                ld = st["land_day"] if st["land_day"] is not None else -1
                print(f"{sd:>8}{y:>5}  {nm:<6}{ld:>8}{st['pastures']:>6}{st['sheep_on_plot']:>6}"
                      f"{st['hires']:>7}{st['wheat_bought']:>7}{st['wool_sold']:>10}"
                      f"{st['max_hands']:>10}{st['bank']:>10,.0f}")
            print()
