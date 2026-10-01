"""Decode top-10 replays: per-agent action profile vs shop draw.

Usage: decode_top.py <shard.parquet> [max_eps] -> prints per-episode profiles
"""
import collections
import json
import sys

import pyarrow.parquet as pq


def profile_episode(replay_json):
    r = json.loads(replay_json)
    teams = r["info"]["TeamNames"]
    rewards = r["rewards"]
    steps = r["steps"]
    shops_seen = None
    profs = []
    for seat in (0, 1):
        p = collections.Counter()
        sells = collections.Counter()
        buys = collections.Counter()
        for st in steps:
            a = st[seat].get("action") or {}
            for op in ([a.get("farmer")] + list(a.get("hands") or [])):
                if op:
                    p[op[0]] += 1
                    if op[0] == "PLANT" and len(op) > 1:
                        p["PLANT_" + op[1]] += 1
                    if op[0] == "BUILD_PASTURE":
                        p["PASTURE"] += 1
                    if op[0] == "BUILD_COOP":
                        p["COOP"] += 1
            for o in (a.get("market") or []):
                if not o:
                    continue
                if o[0] == "SELL":
                    sells[o[1]] += o[2]
                elif o[0] == "BUY_ANIMAL":
                    buys[o[1]] += o[2]
                elif o[0] == "BUY_SEED":
                    p["SEED_" + o[1]] += o[2]
                elif o[0] in ("HIRE", "BUY_LAND"):
                    p[o[0]] += 1
        profs.append((p, sells, buys))
    shops_final = list(steps[-1][0]["observation"]["town"]["unlocked_shops"])
    return teams, rewards, collections.Counter(shops_final), profs


if __name__ == "__main__":
    path = sys.argv[1]
    max_eps = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    pf = pq.ParquetFile(path)
    # episode index for team names
    ep = pq.read_table("data/top10/episodes.parquet",
                       columns=["team_name", "episode_id", "opponent", "date"])
    byid = {r["episode_id"]: r for r in ep.to_pylist()}
    n = 0
    for i in range(pf.metadata.num_row_groups):
        if n >= max_eps:
            break
        row = pf.read_row_group(i).to_pylist()[0]
        eid = row["episode_id"]
        meta = byid.get(eid, {})
        teams, rewards, shops, profs = profile_episode(row["replay_json"])
        n += 1
        print("=" * 80)
        print("ep %d  %s vs %s  rewards %s" % (eid, teams[0], teams[1], rewards))
        print("shops:", dict(shops))
        for seat in (0, 1):
            p, sells, buys = profs[seat]
            plants = {k[6:]: v for k, v in p.items() if k.startswith("PLANT_")}
            print("  %-14s plants=%s animals=%s hires=%d land=%d | sells=%s"
                  % (teams[seat], plants, dict(buys), p["HIRE"], p["BUY_LAND"], dict(sells)))
