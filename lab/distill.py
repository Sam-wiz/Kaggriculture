"""Distill a replayed winner's action stream into a forced-route submission.

Usage: python distill.py <replay.json.gz> <winner_idx> <out.py> [route_id]

Copies subV_a.py, injects `_ROUTES[<id>] = <action stream>` before make_agent,
and forces the router to always return that route (disables day-6 shop routing
and the day-27 route-2 endgame override). Layers stay active: clamp_sells,
weed_repair, sell_lead, hand_align all still guard the foreign tape.
"""
import gzip
import json
import re
import sys
import zlib
import base64

BASE = "subV_a.py"


def main():
    replay_path, winner_idx, out_path = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    route_id = int(sys.argv[4]) if len(sys.argv) > 4 else 200
    d = json.load(gzip.open(replay_path))
    stream = [a[winner_idx] for a in d["actions"]]
    # normalize: ensure dict shape
    tape = []
    for a in stream:
        if not isinstance(a, dict):
            a = {}
        tape.append({
            "farmer": a.get("farmer") or ["PASS"],
            "hands": [h for h in (a.get("hands") or [])],
            "market": [list(o) for o in (a.get("market") or [])],
        })
    while len(tape) < 719:
        tape.append({"farmer": ["PASS"], "hands": [], "market": []})

    blob = base64.b85encode(zlib.compress(
        json.dumps(tape, separators=(",", ":")).encode())).decode()

    src = open(BASE).read()

    inject = (
        f"\n_ROUTES[{route_id}]=json.loads(zlib.decompress("
        f"base64.b85decode('{blob}')))\n"
    )
    # inject right before _SETTINGS line (after _ROUTES built)
    src = src.replace("_SETTINGS={'hand_align':", inject + "_SETTINGS={'hand_align':", 1)

    # force route: replace router body — keep signature/state
    src = re.sub(
        r"def _router\(observation,step,state\):.*?\n    return state\.get\('route',0\)",
        "def _router(observation,step,state):\n"
        "    state['route']=%d\n"
        "    return %d" % (route_id, route_id),
        src, count=1, flags=re.S)

    open(out_path, "w").write(src)
    print("wrote", out_path, "| tape steps:", len(tape), "| team:",
          d["teams"][winner_idx], "| bank:", d["rewards"][winner_idx])


if __name__ == "__main__":
    main()
