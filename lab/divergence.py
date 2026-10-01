"""Where does a replayed episode first diverge from its recording?

Feeding both players' recorded actions back into the engine on the recorded seed should reproduce
the episode exactly, and it does not: 0 of 10 top-10 episodes reproduce, median final-bank error
39,194. Since both action streams are given, the fault is mechanical, and the replay carries the
engine's own per-step observation -- so the first mismatching field can be located precisely rather
than guessed at.

Compares, at every step: each farm's money, hand count, and the shared market inventory.
"""
import json
import os
import sys

import pyarrow.parquet as pq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness
from tapefidelity import load, tape_agent


def diverge(blob):
    d = json.loads(blob)
    info = d.get("info", {})
    seed = info.get("seed")
    steps = d.get("steps") or []
    acts = [[s[0].get("action"), s[1].get("action")] for s in steps]
    recorded = []
    for s in steps:
        o = s[0].get("observation") or {}
        farms = o.get("farms")
        if not farms:
            recorded.append(None)
            continue
        recorded.append(dict(
            money=[farms[0].get("money"), farms[1].get("money")],
            hands=[len(farms[0].get("hands") or []), len(farms[1].get("hands") or [])],
            wheat=(o.get("market", {}).get("inventory") or {}).get("WHEAT"),
        ))

    seen = []

    def on_step(step, state, env):
        o = state[0].observation
        farms = o.farms
        seen.append(dict(
            money=[farms[0]["money"], farms[1]["money"]],
            hands=[len(farms[0]["hands"]), len(farms[1]["hands"])],
            wheat=(o.market.get("inventory") or {}).get("WHEAT"),
        ))

    harness.run_episode(tape_agent(acts, 0), tape_agent(acts, 1), seed=seed,
                        copy_obs=False, on_step=on_step, catch_errors=True)

    # The recorded observation at step t is PRE-action; on_step fires POST-action, so our
    # seen[t] corresponds to recorded[t+1].
    for t in range(min(len(seen), len(recorded) - 1)):
        r, g = recorded[t + 1], seen[t]
        if r is None:
            continue
        for k in ("money", "hands", "wheat"):
            if r[k] != g[k]:
                return dict(step=t + 1, field=k, recorded=r, replayed=g,
                            teams=info.get("TeamNames"), seed=seed,
                            act0=acts[t][0], act1=acts[t][1])
    return None


if __name__ == "__main__":
    day = sys.argv[1] if len(sys.argv) > 1 else "2026-09-08"
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    for ep, blob in load(day, n):
        r = diverge(blob)
        print(f"\n=== episode {ep} ===", flush=True)
        if not r:
            print("   reproduces exactly", flush=True)
            continue
        print(f"   first divergence at step {r['step']} (day {r['step']//24}) in '{r['field']}'")
        print(f"     recorded: {r['recorded']}")
        print(f"     replayed: {r['replayed']}")
        for i, a in ((0, r["act0"]), (1, r["act1"])):
            if isinstance(a, dict):
                print(f"     seat {i} action at step {r['step']-1}: "
                      f"farmer={a.get('farmer')} nhands={len(a.get('hands') or [])} "
                      f"market={(a.get('market') or [])[:4]}")
