"""Can a top player's recorded tape be replayed faithfully? Everything else depends on this.

"Cloning the #1 agent's tapes" sits in our falsified table on the strength of a single number --
their tapes scored 24-44k against our own ~93k -- but that test replayed their actions on ARBITRARY
seeds, so the shop draw their plan was built around was gone. The draw-matched version has never
been run, and a reviewer correctly pointed out the table's evidence against tape reuse therefore
does not exist.

This is the foundational check: take a real top-10 episode, feed BOTH players' recorded actions back
into the engine on that episode's own seed, and compare the final banks to the recorded ones. If
they reproduce, tapes are faithful and a mined tape library is buildable. If they do not, the fault
is in our replay harness -- which is worth knowing before mining 20,000 episodes.

An earlier attempt at this on our own games produced mismatches, but it padded and truncated the
hands list by guesswork; here the hand count comes from the observation the engine actually presents.
"""
import json
import os
import statistics
import sys

import pyarrow.parquet as pq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness

PASS = {"farmer": ["PASS"], "hands": [], "market": []}


def tape_agent(actions, seat):
    """Replay one seat's recorded actions, fitting the hands list to the live hand count."""
    n = len(actions)

    def agent(obs):
        s = obs.get("step")
        if s is None:
            s = int(obs.get("day", 0)) * 24 + int(obs.get("hour", 0))
        if s < 0 or s >= n:
            return dict(PASS)
        a = actions[s][seat]
        if not isinstance(a, dict):
            return dict(PASS)
        have = len(obs["farms"][obs["player"]].get("hands") or [])
        hands = list(a.get("hands") or [])[:have]
        hands += [["PASS"]] * (have - len(hands))
        return {"farmer": a.get("farmer", ["PASS"]), "hands": hands,
                "market": list(a.get("market") or [])[:10]}
    return agent


def load(day, limit=None):
    """Stream one replay at a time.

    Each row holds a whole ~30 MB replay JSON, so `read_table().to_pydict()` on a 570-row shard
    tries to materialise tens of gigabytes and the process is killed with no traceback.
    """
    f = pq.ParquetFile("data/top10/replays_%s.parquet" % day)
    n = 0
    for batch in f.iter_batches(batch_size=1, columns=["episode_id", "replay_json"]):
        d = batch.to_pydict()
        yield d["episode_id"][0], d["replay_json"][0]
        n += 1
        if limit and n >= limit:
            return


def check(ep, blob, shift=1):
    d = json.loads(blob)
    info = d.get("info", {})
    teams = info.get("TeamNames") or []
    seed = info.get("seed")
    rewards = d.get("rewards")
    steps = d.get("steps") or []
    if len(teams) != 2 or seed is None or not rewards or not steps:
        return None
    # steps[t]["action"] is the action that PRODUCED step t's observation, not the action taken
    # from it: at t=0 it is PASS while the t=1 observation already shows 3000 -> 570 spent and four
    # hands hired. Replaying acts[t] at turn t is therefore off by one, which is why every tape
    # experiment in this project -- including "the #1 player's tapes only score 24-44k" -- failed.
    acts = [[s[0].get("action"), s[1].get("action")] for s in steps[shift:]]
    r = harness.run_episode(tape_agent(acts, 0), tape_agent(acts, 1), seed=seed,
                            catch_errors=True)
    got = r["reward"]
    err = [abs((got[i] or 0) - (rewards[i] or 0)) for i in range(2)]
    return dict(ep=ep, teams=teams, seed=seed, recorded=rewards, replayed=got,
                err=err, exact=max(err) < 1.0)


if __name__ == "__main__":
    day = sys.argv[1] if len(sys.argv) > 1 else "2026-09-08"
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    rows = list(load(day, n))
    print(f"{len(rows)} episodes from {day}\n", flush=True)
    print(f"{'episode':<11}{'teams':<34}{'recorded':>20}{'replayed':>20}{'ok':>5}")
    ok = 0
    errs = []
    for ep, blob in rows:
        c = check(ep, blob)
        if not c:
            continue
        ok += c["exact"]
        errs.append(max(c["err"]))
        tm = (c["teams"][0][:15] + " v " + c["teams"][1][:15])
        rec = "%.0f/%.0f" % tuple(c["recorded"])
        rep = "%.0f/%.0f" % tuple(c["replayed"])
        print(f"{ep:<11}{tm:<34}{rec:>20}{rep:>20}{'YES' if c['exact'] else 'no':>5}", flush=True)
    print(f"\nexact reproductions: {ok}/{len(errs)}")
    if errs:
        print(f"median absolute bank error: {statistics.median(errs):,.0f}")
