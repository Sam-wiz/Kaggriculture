"""Exact-replay every >=2200 post-lock rival tape (both seats open-loop), verify the recorded banks reproduce,
and extract (a) the rival's premium-sale stream in PREDICT2 format and (b) its premium SELL lots with the
price it saw at issue (for the price-reactive rival). Writes streams_all.json, lots.json, extract.jsonl."""
import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common
common.setup()
from concurrent.futures import ProcessPoolExecutor


def job(row):
    import harness
    from kaggle_environments.envs.kaggriculture import kaggriculture as K
    t0 = time.time()
    try:
        acts, seed, rew = common.load_tape(row["path"], row["kind"])
        us, them = row["seat"], 1 - row["seat"]
        rt = common.RecordingTape(acts, them)
        pair = [None, None]
        pair[us] = common.tape_agent(acts, us)
        pair[them] = rt
        # Exact fills: hook the engine's per-unit commit (unit ops run before the market inside a step, so a
        # same-tick DROP lands before the SELL; sales at $1 do not move inventory and are invisible to the layer).
        LOG, fills = [], {}
        orig = K._commit_unit
        def _cu(op, item, price, farm, private, market, shed_capacity=100):
            ok = orig(op, item, price, farm, private, market, shed_capacity)
            if ok and op == "SELL" and price > 1:
                LOG.append((item, id(farm)))
            return ok
        def on_step(step, state, env):
            ids = {id(state[0].observation.farms[i]): i for i in range(2)}
            for item, fid in LOG:
                if ids.get(fid) == them:
                    fills[(step, item)] = fills.get((step, item), 0) + 1
            LOG.clear()
        K._commit_unit = _cu
        try:
            r = harness.run_episode(pair[0], pair[1], seed=seed, copy_obs=True, on_step=on_step)
        finally:
            K._commit_unit = orig
        exact = [round(x) for x in r["reward"]] == [round(x) for x in rew]
        lots = common.rival_lots(acts, them, rt.prices, rt.shed)
        ev = [[t, common.Q_ITEMS.index(item), min(100, q)] for (t, item), q in sorted(fills.items())
              if item in common.Q_ITEMS and q >= 2]
        units = {it: sum(q for (t, i), q in fills.items() if i == it) for it in common.PREM}
        return dict(row, exact=exact, rew=r["reward"], rec=rew, n_ev=len(ev), n_lots=len(lots), units=units,
                    ev=ev, lots=lots, secs=round(time.time() - t0, 1), err=None)
    except Exception as e:
        return dict(row, exact=False, err=repr(e), ev=[], lots=[], secs=round(time.time() - t0, 1))


if __name__ == "__main__":
    rows = common.tape_universe()
    print(len(rows), "tapes:", {s: sum(1 for r in rows if r["src"] == s) for s in ("idx", "live", "wlv")}, flush=True)
    streams, lots, log = [], {}, open(os.path.join(common.HERE, "extract.jsonl"), "w")
    n_exact = 0
    with ProcessPoolExecutor(max_workers=2) as ex:
        for i, res in enumerate(ex.map(job, rows, chunksize=1)):
            log.write(json.dumps({k: v for k, v in res.items() if k not in ("ev", "lots")}) + "\n"); log.flush()
            if res["exact"]:
                n_exact += 1
                streams.append(dict(ep=res["ep"], src=res["src"], opp=res["opp"], R=res["R"], rseat=1 - res["seat"], ev=res["ev"]))
                lots[str(res["ep"])] = res["lots"]
            if i % 25 == 0 or not res["exact"]:
                print(i, res["ep"], res["src"], res["opp"][:14], "exact" if res["exact"] else f"NOT EXACT {res.get('err')} {res.get('rew')} vs {res.get('rec')}",
                      "ev", res.get("n_ev"), f"{res['secs']}s", flush=True)
    json.dump(streams, open(os.path.join(common.HERE, "streams_all.json"), "w"))
    json.dump(lots, open(os.path.join(common.HERE, "lots.json"), "w"))
    print(f"DONE exact {n_exact}/{len(rows)}; streams {len(streams)}; events/stream mean "
          f"{sum(len(s['ev']) for s in streams) / max(1, len(streams)):.1f}", flush=True)
