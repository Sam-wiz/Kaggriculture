"""Replay cached live episodes through the pinned engine with hooks and record an exact ledger.

Per player, per step: market FILLS (op, item, price), hire cost, land cost, harvested units by product
(inventory diff on HARVEST), fertilizer collected, animals placed, end-of-day discards, and the herd
alive at each dawn. Verifies the replay reproduces the recorded rewards.

usage: python moe/opus/ledger_eps.py --rmin 2400 --rmax 2900 --workers 2 --out moe/opus/ledger_band.json
"""
import argparse, gzip, json, os, sys
from concurrent.futures import ProcessPoolExecutor
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT); sys.path.insert(0, ROOT)
import harness
K = harness.K

G = {"state": None, "step": 0, "rec": None}


def _pl(farm):
    fs = G["state"][0].observation.farms
    return 0 if fs[0] is farm else 1


def _install_hooks():
    if getattr(K, "_opus_hooked", False):
        return
    oc, oh, ol, oa, od, oi = (K._commit_unit, K._do_hire, K._do_buy_land, K._apply_unit_action,
                              K._drop_inventories_to_shed, K.interpreter)

    def interp(state, env):
        G["state"] = state
        G["step"] = int(getattr(state[0].observation, "step", 0) or 0)
        return oi(state, env)

    def commit(op, item, price, farm, private, market, shed_capacity=100):
        ok = oc(op, item, price, farm, private, market, shed_capacity)
        if ok and G["rec"] is not None:
            G["rec"]["fills"].append((G["step"], _pl(farm), op, item, price))
        return ok

    def hire(farm, private, board_size, mult=1):
        m0 = farm["money"]; oh(farm, private, board_size, mult)
        if G["rec"] is not None and m0 != farm["money"]:
            G["rec"]["fills"].append((G["step"], _pl(farm), "HIRE", "", m0 - farm["money"]))

    def land(farm, board_size):
        m0 = farm["money"]; ol(farm, board_size)
        if G["rec"] is not None and m0 != farm["money"]:
            G["rec"]["fills"].append((G["step"], _pl(farm), "BUY_LAND", "", m0 - farm["money"]))

    def apply(farm, private, idx, action, board_size, day, tpd, shed_capacity=100):
        op = action[0] if isinstance(action, list) and action else None
        if G["rec"] is None or op not in ("HARVEST", "COLLECT_FERTILIZER", "PLACE"):
            return oa(farm, private, idx, action, board_size, day, tpd, shed_capacity)
        invs = private["inventories"]
        before = dict(invs[idx]) if idx < len(invs) else {}
        pos = K._farmer_position(farm, idx)
        t0 = farm["tiles"][pos[1]][pos[0]] if pos else None
        had_animal = isinstance(t0, dict) and "animal" in t0
        oa(farm, private, idx, action, board_size, day, tpd, shed_capacity)
        after = dict(invs[idx]) if idx < len(invs) else {}
        p = _pl(farm)
        if op in ("HARVEST", "COLLECT_FERTILIZER"):
            for k, v in after.items():
                d = v - before.get(k, 0)
                if d > 0:
                    G["rec"]["prod"].append((G["step"], p, k, d))
        elif op == "PLACE" and pos:
            t1 = farm["tiles"][pos[1]][pos[0]]
            if not had_animal and isinstance(t1, dict) and "animal" in t1:
                G["rec"]["placed"].append((G["step"], p, t1["animal"]))

    def drop(private, capacity):
        n_in = sum(v for inv in private["inventories"] for v in inv.values() if v > 0)
        s0 = sum(private["shed"].values())
        od(private, capacity)
        lost = n_in - (sum(private["shed"].values()) - s0)
        if lost > 0 and G["rec"] is not None:
            p = 0 if G["state"][0].observation.private is private else 1
            G["rec"]["discard"].append((G["step"], p, lost))

    K._commit_unit, K._do_hire, K._do_buy_land = commit, hire, land
    K._apply_unit_action, K._drop_inventories_to_shed, K.interpreter = apply, drop, interp
    K._opus_hooked = True


def load_actions(row):
    if row["kind"] == "full":
        d = json.load(open(row["path"]))
        acts = [[s[0].get("action"), s[1].get("action")] for s in d["steps"]]
        seed = d["info"]["seed"]; rew = d["rewards"]
    else:
        d = json.load(gzip.open(row["path"], "rt"))
        acts = d["actions"]; seed = d["seed"]; rew = d["rewards"]
    return acts, seed, rew


def job(row):
    _install_hooks()
    try:
        acts, seed, rew = load_actions(row)
    except Exception as e:
        return dict(ep=row["ep"], err=repr(e))
    PASS = {"farmer": ["PASS"], "hands": [], "market": []}

    def mk(seat):
        def ag(obs):
            t = obs["step"] + 1
            a = acts[t][seat] if t < len(acts) else None
            return a if isinstance(a, dict) else PASS
        return ag

    rec = dict(fills=[], prod=[], placed=[], discard=[], herd=[], shops=None)
    G["rec"] = rec

    def on_step(step, state, env):
        if (step + 1) % 24 == 0:  # dawn snapshot after end-of-day
            fs = state[0].observation.farms
            h = []
            for f in fs:
                c = {}
                for row_ in f["tiles"]:
                    for t in row_:
                        if isinstance(t, dict):
                            if "animal" in t:
                                c[t["animal"]] = c.get(t["animal"], 0) + 1
                            elif t.get("kind") == "PLANT":
                                c["P_" + t["crop"]] = c.get("P_" + t["crop"], 0) + 1
                c["hands"] = 0
                h.append(c)
            rec["herd"].append(((step + 1) // 24, h))

    r = harness.run_episode(mk(0), mk(1), seed=seed, copy_obs=False, on_step=on_step)
    G["rec"] = None
    rec["shops"] = list(r["state"][0].observation.town["unlocked_shops"])
    rec["replayed"] = r["reward"]
    rec["recorded"] = rew
    rec["match"] = [abs(a - b) < 0.5 for a, b in zip(r["reward"], rew)]
    rec.update({k: row[k] for k in ("ep", "build", "seat", "opp", "R", "ours", "theirs", "seed")})
    return rec


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--rmin", type=float, default=2400)
    ap.add_argument("--rmax", type=float, default=2900)
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--out", default="moe/opus/ledger_band.json")
    a = ap.parse_args()
    idx = json.load(open("moe/opus/eps_index.json"))
    rows = [r for r in idx if r["R"] and a.rmin <= r["R"] < a.rmax and r["ours"] is not None]
    if a.limit:
        rows = rows[:a.limit]
    print(len(rows), "episodes", flush=True)
    out = []
    with ProcessPoolExecutor(max_workers=a.workers) as ex:
        for i, rec in enumerate(ex.map(job, rows)):
            out.append(rec)
            if "err" in rec:
                print("ERR", rec["ep"], rec["err"], flush=True)
            elif not all(rec["match"]):
                print("DIVERGED", rec["ep"], rec["replayed"], rec["recorded"], flush=True)
            if (i + 1) % 20 == 0:
                print(i + 1, "done", flush=True)
    json.dump(out, open(a.out, "w"))
    print("wrote", a.out, "match:", sum(all(r.get("match", [0])) for r in out), "/", len(out))
