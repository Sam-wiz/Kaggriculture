"""Mine executable tapes from top-10 episodes, now that replay is exact.

Replaying a recorded episode reproduces its final banks to the dollar once the actions are read at
the right offset (`steps[t]["action"]` produced step t, so the tape must be read from steps[1:]).
That makes every archived top-10 game an executable strategy rather than a picture of one.

For each episode this keeps the WINNER's action stream plus the metadata a router needs to choose
between tapes later: the seed, the shop draw in unlock order, and both final banks.

Memory: each row holds a whole ~30 MB replay JSON, so rows are streamed one at a time. Materialising
a 570-row shard silently gets the process OOM-killed.
"""
import gzip
import json
import os
import sys

import pyarrow.parquet as pq

OUT = "data/tapes"


def shard_rows(path, limit=None):
    f = pq.ParquetFile(path)
    n = 0
    for batch in f.iter_batches(batch_size=1, columns=["episode_id", "replay_json"]):
        d = batch.to_pydict()
        yield d["episode_id"][0], d["replay_json"][0]
        n += 1
        if limit and n >= limit:
            return


def extract(blob):
    d = json.loads(blob)
    info = d.get("info", {})
    teams = info.get("TeamNames") or []
    seed = info.get("seed")
    rewards = d.get("rewards")
    steps = d.get("steps") or []
    if len(teams) != 2 or seed is None or not rewards or len(steps) < 2:
        return None
    if rewards[0] is None or rewards[1] is None:
        return None
    win = 0 if rewards[0] >= rewards[1] else 1
    # Actions live one step later than the state they act on.
    tape = [s[win].get("action") for s in steps[1:]]
    shops = []
    for s in steps:
        o = s[0].get("observation") or {}
        cur = (o.get("town") or {}).get("unlocked_shops")
        if cur is not None and len(cur) > len(shops):
            shops = list(cur)
    return dict(seed=seed, team=teams[win], opponent=teams[1 - win],
                bank=rewards[win], opp_bank=rewards[1 - win], shops=shops,
                turns=len(tape), tape=tape)


def main(days, limit_per_day=None):
    os.makedirs(OUT, exist_ok=True)
    total = 0
    for day in days:
        path = "data/top10/replays_%s.parquet" % day
        if not os.path.exists(path):
            print("missing", path, flush=True)
            continue
        out = os.path.join(OUT, "tapes_%s.jsonl.gz" % day)
        n = 0
        with gzip.open(out, "wt") as fh:
            for ep, blob in shard_rows(path, limit_per_day):
                try:
                    rec = extract(blob)
                except Exception:
                    rec = None
                if not rec or rec["turns"] < 700:
                    continue
                rec["episode_id"] = ep
                fh.write(json.dumps(rec) + "\n")
                n += 1
                if n % 25 == 0:
                    print(f"  {day}: {n} tapes", flush=True)
        total += n
        print(f"{day}: wrote {n} tapes -> {out} ({os.path.getsize(out)/1e6:.1f} MB)", flush=True)
    print(f"\nTOTAL {total} tapes", flush=True)


if __name__ == "__main__":
    days = sys.argv[1:] or ["2026-09-08"]
    lim = int(os.environ.get("LIMIT", "0")) or None
    main(days, lim)
