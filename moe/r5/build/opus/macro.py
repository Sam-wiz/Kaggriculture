"""r5 opus — macro-policy extraction from the top dump (exact replay).
Per episode, per seat, per day d: dawn state (hour 0 obs of that seat, incl. private) and the day's
macro decisions (fills from ledger hooks).  One JSON line per episode.
  state:  money, quads, shops (list), herd {COW,SHEEP,GOOSE}, plants {crop:n}, young {crop:n planted d-1},
          empty (unlocked empty tiles), weeds, pastures/coops empty, shed {item:n}, seeds {crop:n},
          prices {item:p}, map (100-char tile string)
  dec:    seed {crop:n}, animal {kind:n}, land (#), hire (#), buyp {item:n}, sell {item:[u,rev]}
usage: macro.py OUT.jsonl [GLOB] [WORKERS] [LIMIT]   (resumable; skips done eps)
"""
import glob, gzip, json, os, sys
from concurrent.futures import ProcessPoolExecutor
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
os.chdir(ROOT); sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + "/moe/opus")
import harness
import ledger_eps as L
PASS = {"farmer": ["PASS"], "hands": [], "market": []}
CH = {"WHEAT": "W", "CARROT": "C", "TOMATO": "T", "STRAWBERRY": "S", "MELON": "M", "COW": "c", "SHEEP": "s", "GOOSE": "g"}


def tmap(tiles):
    s = []
    for row in tiles:
        for t in row:
            if t is None: s.append(".")
            elif t == "LOCKED": s.append("#")
            elif isinstance(t, dict):
                k = t.get("kind")
                if k == "WEED": s.append("w")
                elif k == "PLANT": s.append(CH.get(t.get("crop"), "?"))
                elif k in ("COOP", "PASTURE"):
                    s.append(CH.get(t.get("animal"), "O" if k == "COOP" else "P") if t.get("animal") else ("O" if k == "COOP" else "P"))
                else: s.append("?")
            else: s.append("?")
    return "".join(s)


def job(path):
    L._install_hooks()
    d = json.load(gzip.open(path, "rt"))
    acts, seed, rew = d["actions"], d["seed"], d["rewards"]
    dawn = [[], []]

    def mk(seat):
        def ag(obs):
            if obs["hour"] == 0:
                f = obs["farms"][seat]; tiles = f["tiles"]; day = obs["day"]
                herd, plants, young = {}, {}, {}; weeds = empty = ep = ec = 0
                for row in tiles:
                    for t in row:
                        if t is None: empty += 1
                        elif isinstance(t, dict):
                            k = t.get("kind")
                            if k == "WEED": weeds += 1
                            elif k == "PLANT":
                                c = t["crop"]; plants[c] = plants.get(c, 0) + 1
                                if t.get("planted_day") == day - 1: young[c] = young.get(c, 0) + 1
                            elif t.get("animal"): herd[t["animal"]] = herd.get(t["animal"], 0) + 1
                            elif k == "PASTURE": ep += 1
                            elif k == "COOP": ec += 1
                pv = obs["private"]
                dawn[seat].append(dict(day=day, money=f["money"], quads=len(f.get("unlocked_quadrants") or []),
                                       shops=list(obs["town"]["unlocked_shops"]), herd=herd, plants=plants, young=young,
                                       empty=empty, weeds=weeds, epast=ep, ecoop=ec,
                                       shed={k: v for k, v in (pv.get("shed") or {}).items() if v},
                                       seeds={k: v for k, v in (pv.get("seeds") or {}).items() if v},
                                       prices=dict(obs["market"]["prices"]), inv=dict(obs["market"]["inventory"]),
                                       map=tmap(tiles)))
            t = obs["step"] + 1
            a = acts[t][seat] if t < len(acts) else None
            return a if isinstance(a, dict) else PASS
        return ag

    rec = dict(fills=[], prod=[], placed=[], discard=[], herd=[], shops=None)
    L.G["rec"] = rec
    try:
        r = harness.run_episode(mk(0), mk(1), seed=seed, copy_obs=False)
    except Exception as e:
        L.G["rec"] = None
        return dict(ep=d["episode_id"], err=repr(e)[:200])
    L.G["rec"] = None
    rp = r["reward"]
    out = dict(ep=d["episode_id"], date=d.get("date"), seed=seed, teams=d["teams"], rewards=rew, replayed=rp,
               match=[abs(a - b) < 0.5 for a, b in zip(rp, rew)],
               shops=list(r["state"][0].observation.town["unlocked_shops"]),
               op1=[(acts[1][s].get("market") if isinstance(acts[1][s], dict) else None) for s in range(2)], seats=[])
    for s in range(2):
        dec = [dict(seed={}, animal={}, land=0, hire=0, hcost=0, buyp={}, sell={}) for _ in range(30)]
        for st, p, op, it, pr in rec["fills"]:
            if p != s: continue
            x = dec[min(st // 24, 29)]
            if op == "BUY_SEED": x["seed"][it] = x["seed"].get(it, 0) + 1
            elif op == "BUY_ANIMAL": x["animal"][it] = x["animal"].get(it, 0) + 1
            elif op == "BUY_LAND": x["land"] += 1; x.setdefault("land_step", []).append(st)
            elif op == "HIRE": x["hire"] += 1; x["hcost"] += pr
            elif op == "BUY_PRODUCT": x["buyp"][it] = x["buyp"].get(it, 0) + 1
            elif op == "SELL":
                q = x["sell"].setdefault(it, [0, 0]); q[0] += 1; q[1] += pr
        prod = [dict() for _ in range(30)]
        for st, p, k, n in rec["prod"]:
            if p == s: prod[min(st // 24, 29)][k] = prod[min(st // 24, 29)].get(k, 0) + n
        out["seats"].append(dict(team=d["teams"][s], bank=rew[s], dawn=dawn[s], dec=dec, prod=prod,
                                 discard=sum(n for st, p, n in rec["discard"] if p == s)))
    return out


if __name__ == "__main__":
    out = sys.argv[1]; g = sys.argv[2] if len(sys.argv) > 2 else "mine/top10/*.json.gz"
    W = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    lim = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    done = set()
    if os.path.exists(out):
        for line in open(out):
            try: done.add(json.loads(line)["ep"])
            except Exception: pass
    paths = [p for p in sorted(glob.glob(g)) if int(os.path.basename(p).split(".")[0]) not in done]
    if lim: paths = paths[:lim]
    print(len(paths), "to decode", flush=True)
    with ProcessPoolExecutor(max_workers=W) as ex, open(out, "a") as f:
        for i, res in enumerate(ex.map(job, paths, chunksize=2), 1):
            f.write(json.dumps(res, separators=(",", ":")) + "\n"); f.flush()
            if "err" in res or not all(res.get("match", [0])): print("BAD", res.get("ep"), res.get("err"), res.get("replayed"), res.get("rewards"), flush=True)
            if i % 100 == 0: print(i, "done", flush=True)
