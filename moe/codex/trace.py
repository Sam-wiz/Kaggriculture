"""Exact-engine fill ledger. All outputs stay in moe/codex; no engine edits."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import argparse
import copy
import importlib.util
import json
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
import harness

K = harness.K
SIR = "subV_sir2.py"
V2 = "subV2_f55rec.py"
KOSH = "rivals/koshinm_kaggriculture-local-best-2026-09-21/main.py"


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def trace_game(job):
    base, opp, seed, seat, outdir = job
    paths = [base, opp] if seat == 0 else [opp, base]
    mods = [load(p, "trace_player_" + str(i)) for i, p in enumerate(paths)]
    for mod in mods:
        if hasattr(mod, '_EC_STRICT'):
            mod._EC_STRICT = True
    records = {}
    cash = [0, 0]
    sales = [Counter(), Counter()]
    amounts = [Counter(), Counter()]
    pre = {}
    context = {}
    originals = {n: getattr(K, n) for n in
                 ("_process_market", "_commit_unit", "_do_hire", "_do_buy_land", "_apply_unit_action")}

    def wrapped_agent(i):
        def run(obs):
            step = int(obs["step"])
            before = {"money": obs["farms"][i]["money"],
                      "shed": dict(obs["private"]["shed"]),
                      "inventory": dict(obs["market"]["inventory"]),
                      "prices": dict(obs["market"]["prices"])}
            action = mods[i].agent(obs)
            before["action"] = copy.deepcopy(action)
            mod = mods[i]
            if hasattr(mod, "projected_shed"):
                before["projected"] = dict(mod.projected_shed(action, mod.FarmView(obs)))
            ns = vars(mod)
            if "_mod" in ns:
                ns = vars(ns["_mod"])
            while "_BASE_NS" in ns:
                ns = ns["_BASE_NS"]
            if "_IMPL" in ns:
                before["route"] = ns["_IMPL"].chassis.players.get(i, {}).get("route")
            pre[i] = before
            return action
        return run

    def player(farm):
        farms = context["state"][0].observation.farms
        assert farm is farms[0] or farm is farms[1]
        return 0 if farm is farms[0] else 1

    def market(state, env):
        context["state"] = state
        step = state[0].observation.step
        context["step"] = step
        rec = {"step": step, "before": copy.deepcopy(pre), "fills": [],
               "market_shed": [dict(s.observation.private["shed"]) for s in state]}
        records[step] = rec
        for i in (0, 1):
            projection = pre[i].get("projected")
            if projection is not None:
                actual = rec["market_shed"][i]
                assert all(projection.get(k, 0) == actual.get(k, 0)
                           for k in set(projection) | set(actual)), (step, i, projection, actual)
        return originals["_process_market"](state, env)

    def commit(op, item, price, farm, private, market, shed_capacity=100):
        ok = originals["_commit_unit"](op, item, price, farm, private, market, shed_capacity)
        if ok:
            i = player(farm)
            sign = 1 if op == "SELL" else -1
            cash[i] += sign * price
            frame = sys._getframe(1)
            index = frame.f_locals["i"]
            records[context["step"]]["fills"].append([i, index, op, item, price])
            if op == "SELL":
                sales[i][item] += price
                amounts[i][item] += 1
        return ok

    def hire(farm, *args, **kwargs):
        before = farm["money"]
        result = originals["_do_hire"](farm, *args, **kwargs)
        cash[player(farm)] += farm["money"] - before
        return result

    def land(farm, *args, **kwargs):
        before = farm["money"]
        result = originals["_do_buy_land"](farm, *args, **kwargs)
        cash[player(farm)] += farm["money"] - before
        return result

    def unit(farm, private, *args, **kwargs):
        before = farm["money"]
        result = originals["_apply_unit_action"](farm, private, *args, **kwargs)
        # _process_market has not run yet at step zero. Infer identity from
        # the shared farm object captured by a temporary interpreter wrapper.
        i = 0 if farm is context["farms"][0] else 1
        cash[i] += farm["money"] - before
        return result

    interpreter = K.interpreter
    def interp(state, env):
        if hasattr(state[0].observation, "farms"):
            context["farms"] = state[0].observation.farms
        return interpreter(state, env)

    def after(step, state, env):
        money = [s.observation.farms[i]["money"] for i, s in enumerate(state)]
        assert money == [3000 + c for c in cash], (step, money, cash)
        records[step]["after_money"] = money
        records[step]["after_shed"] = [dict(s.observation.private["shed"]) for s in state]
        records[step]["shops"] = list(state[0].observation.town["unlocked_shops"])

    K._process_market = market
    K._commit_unit = commit
    K._do_hire = hire
    K._do_buy_land = land
    K._apply_unit_action = unit
    K.interpreter = interp
    try:
        result = harness.run_episode(wrapped_agent(0), wrapped_agent(1), seed=seed,
                                     on_step=after, catch_errors=False)
    finally:
        for name, fn in originals.items():
            setattr(K, name, fn)
        K.interpreter = interpreter
    path = Path(outdir) / (Path(base).stem + "__" + Path(opp).parent.name + "_" + Path(opp).stem
                           + "__" + str(seed) + "_s" + str(seat) + ".json")
    summary = {"base": base, "opponent": opp, "seed": seed, "seat": seat,
               "reward": result["reward"], "status": result["status"], "errors": result["errors"],
               "margin": result["reward"][seat] - result["reward"][1-seat],
               "revenue": sales, "units": amounts,
               "telemetry": [getattr(m, "_EC_REPORT", {}) for m in mods],
               "path": str(path)}
    assert all(t.get('errors', 0) == 0 for t in summary['telemetry']), summary
    path.write_text(json.dumps({"summary": summary, "steps": list(records.values())}))
    return summary


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default=SIR)
    ap.add_argument("--opps", nargs="*", default=[KOSH, V2])
    ap.add_argument("--seeds", nargs=2, type=int, default=[900, 6])
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--outdir", default="moe/codex/traces")
    args = ap.parse_args()
    assert 1 <= args.workers <= 2
    Path(args.outdir).mkdir(parents=True, exist_ok=True)
    index = json.loads((ROOT / "data/seedindex_900000_1400.json").read_text())
    seeds = [x["seed"] for x in index][args.seeds[0]:sum(args.seeds)]
    jobs = [(args.base, opp, seed, seat, args.outdir) for opp in args.opps
            for seed in seeds for seat in (0, 1)]
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        for summary in pool.map(trace_game, jobs):
            print(json.dumps(summary), flush=True)
