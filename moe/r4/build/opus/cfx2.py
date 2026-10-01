"""Fill-accurate counterfactual: net one seat's same-turn round trips on FILLED units, replay, check invariance.

1. Exact replay with fill hooks -> per step, seat S: filled SELL units s_t and BUY_PRODUCT units b_t of ITEM.
2. Edited seat: at every step with s_t>0 and b_t>0, ITEM orders replaced by one order for the net filled
   quantity (SELL s-b or BUY b-s) at the first ITEM slot; other ITEM slots -> NOOP (slot positions kept).
   Steps without a round trip are untouched (orders that did not fill stay as they were).
3. Replay edited + recorded opponent. Report bank deltas, shops equal?, herd/plant counts at dawn equal?
usage: cfx2.py OUT.jsonl TEAM ITEM[,ITEM] [GLOB]
"""
import glob, gzip, json, os, sys, copy
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT); sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/opus")
import harness, ledger_eps as L
PASS = {"farmer": ["PASS"], "hands": [], "market": []}


def run(acts, seed):
    L._install_hooks()
    rec = dict(fills=[], prod=[], placed=[], discard=[], herd=[], shops=None); L.G["rec"] = rec
    herd = []

    def mk(seat):
        def ag(obs):
            t = obs["step"] + 1
            a = acts[t][seat] if t < len(acts) else None
            return a if isinstance(a, dict) else PASS
        return ag

    def on_step(step, state, env):
        if (step + 1) % 24 == 0:
            h = []
            for f in state[0].observation.farms:
                c = {}
                for row in f["tiles"]:
                    for t in row:
                        if isinstance(t, dict):
                            k = t.get("animal") or (t.get("crop") if t.get("kind") == "PLANT" else t.get("kind"))
                            c[k] = c.get(k, 0) + 1
                h.append(c)
            herd.append(h)
    r = harness.run_episode(mk(0), mk(1), seed=seed, copy_obs=False, on_step=on_step)
    L.G["rec"] = None
    return r["reward"], rec["fills"], herd, list(r["state"][0].observation.town["unlocked_shops"])


def main():
    out, team, items = sys.argv[1], sys.argv[2], sys.argv[3].split(",")
    g = sys.argv[4] if len(sys.argv) > 4 else "mine/top10/*.json.gz"
    with open(out, "a") as f:
        for p in sorted(glob.glob(g)):
            d = json.load(gzip.open(p, "rt"))
            if team not in d["teams"]: continue
            s = d["teams"].index(team)
            rw, fills, herd, shops = run(d["actions"], d["seed"])
            per = {}
            for st, pl, op, it, pr in fills:
                if pl == s and it in items and op in ("SELL", "BUY_PRODUCT"):
                    k = per.setdefault((st, it), [0, 0, 0, 0]); i = 0 if op == "SELL" else 1
                    k[i] += 1; k[2 + i] += pr
            a2 = copy.deepcopy(d["actions"]); nrt = 0; rt_pnl = 0
            for (st, it), (sv, bv, rs, cb) in per.items():
                if sv == 0 or bv == 0: continue
                # fills at step st were produced by action acts[st+1]
                a = a2[st + 1][s]; m = list(a.get("market") or []); newm = []; first = True
                for o in m:
                    if isinstance(o, list) and len(o) >= 3 and o[1] == it and o[0] in ("SELL", "BUY_PRODUCT"):
                        if first and sv != bv: newm.append(["SELL", it, sv - bv] if sv > bv else ["BUY_PRODUCT", it, bv - sv])
                        else: newm.append(["NOOP"])
                        first = False
                    else: newm.append(o)
                a["market"] = newm; nrt += min(sv, bv)
                rt_pnl += rs - cb - (sv - bv) * ((rs / sv) if sv > bv else (cb / bv))
            rw2, fills2, herd2, shops2 = run(a2, d["seed"])
            hs = sum(1 for x, y in zip(herd, herd2) if x[s] != y[s]); ho = sum(1 for x, y in zip(herd, herd2) if x[1 - s] != y[1 - s])
            r = dict(ep=d["episode_id"], team=team, opp=d["teams"][1 - s], items=items, rt_units=nrt,
                     rt_pnl_naive=round(rt_pnl), ok=[abs(rw[i] - d["rewards"][i]) < .5 for i in range(2)],
                     d_self=rw2[s] - rw[s], d_opp=rw2[1 - s] - rw[1 - s],
                     d_margin=(rw2[s] - rw2[1 - s]) - (rw[s] - rw[1 - s]), shops_same=shops == shops2,
                     herd_days_diff_self=hs, herd_days_diff_opp=ho)
            f.write(json.dumps(r, ensure_ascii=False) + "\n"); f.flush()
            print(json.dumps(r, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
