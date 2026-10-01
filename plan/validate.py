"""Prove the forward model is exact: replay a real episode and diff every field."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import harness
from plan.fastsim import Farm, apply_market
from kaggle_environments.envs.kaggriculture import kaggriculture as K


def tile_sig(t):
    if t is None or t == "LOCKED":
        return t
    if t.get("kind") == "PLANT":
        return ("P", t["crop"], t["planted_day"], t["watered_today"],
                t["consecutive_unwatered"], t["yield_units"], t["max_lifespan_step"],
                t["fertilized_until_day"])
    if "animal" in t:
        return ("A", t["animal"], t["placed_day"], t["yield_units"], t["fed_today"],
                t["consecutive_unfed"], t["cared_today"], t["fertilizer_available"],
                t.get("pending_care_bonus", 0))
    return (t.get("kind"),)


def run(agent_path, opp, seed):
    inner = harness.load_agent(agent_path)
    state = {"sim": None, "diffs": [], "checked": 0}

    def wrapped(obs):
        me = obs["player"]
        sim = state["sim"]
        if sim is not None:
            # compare our prediction of THIS turn against reality, before acting
            real = obs["farms"][me]
            state["checked"] += 1
            got = [[tile_sig(t) for t in row] for row in sim.tiles]
            want = [[tile_sig(t) for t in row] for row in real["tiles"]]
            if got != want:
                for y in range(len(want)):
                    for x in range(len(want[y])):
                        if got[y][x] != want[y][x]:
                            state["diffs"].append(
                                ("tile", obs["step"], x, y, got[y][x], want[y][x]))
                            break
                    if state["diffs"]:
                        break
            if dict(sim.seeds) != dict(obs["private"]["seeds"]):
                state["diffs"].append(("seeds", obs["step"], dict(sim.seeds),
                                       dict(obs["private"]["seeds"])))
            err = sim.money - real["money"]
            state.setdefault("merr", []).append(abs(err))
            if abs(err) > 0.5:
                state["diffs"].append(("money", obs["step"], sim.money, real["money"]))
            shed_a = {k: v for k, v in sim.shed.items() if v}
            shed_b = {k: v for k, v in obs["private"]["shed"].items() if v}
            if shed_a != shed_b:
                state["diffs"].append(("shed", obs["step"], shed_a, shed_b))
        # resync from truth, then predict forward from this turn's action
        sim = Farm(obs, me)
        act = inner(obs)
        units = [act.get("farmer") or ["PASS"]] + list(act.get("hands") or [])
        # engine drops ALL plantings of a crop when the turn's demand exceeds seeds
        demand = {}
        for a in units:
            if a and len(a) > 1 and a[0] == "PLANT":
                demand[a[1]] = demand.get(a[1], 0) + 1
        blocked = {c for c, k in demand.items() if k > sim.seeds.get(c, 0)}
        for i, a in enumerate(units):
            if a and len(a) > 1 and a[0] == "PLANT" and a[1] in blocked:
                continue
            sim.apply_unit(i, a)
        apply_market(sim, act.get("market"), obs["market"]["prices"],
                     obs["market"]["inventory"],
                     lambda it, iv: K.market_price(it, int(iv)))
        sim.decay(obs["step"])
        if (obs["step"] + 1) % 24 == 0:
            sim.end_of_day()
            sim.day += 1
        state["sim"] = sim
        return act

    r = harness.run_episode(wrapped, opp, seed=seed, catch_errors=False)
    return r, state


if __name__ == "__main__":
    agent = sys.argv[1] if len(sys.argv) > 1 else "port2/h_over.py"
    for seed in (1, 4, 42):
        r, st = run(agent, "port/main.py", seed)
        d = st["diffs"]
        import collections
        by = collections.Counter(x[0] for x in d)
        print(f"seed {seed}: bank {r['reward'][0]:>9,.0f}  turns {st['checked']}  "
              f"divergences {len(d)} {dict(by)}"
              + ("" if d else "   EXACT"))
        me_ = st.get("merr") or [0]
        import statistics
        print(f"    money forecast error: mean ${statistics.mean(me_):,.0f}  "
              f"median ${statistics.median(me_):,.0f}  max ${max(me_):,.0f}  "
              f"(bank ${r['reward'][0]:,.0f})")
