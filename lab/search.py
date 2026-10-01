"""Coordinate-descent parameter search.

Cycles over one parameter at a time, keeping any change that improves the score
by more than the noise floor. Scores against a mixed opponent set so we tune for
the ladder rather than for one bot.
"""

import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tune  # noqa: E402

# name -> candidate values
GRID = {
    "sell_bias_tight":  [1.3, 2.0, 3.0],
    "sell_bias_glut":   [1.1, 1.35, 1.7],
    "fert_value":       [1.1, 1.4, 1.9],
    "hinge_meter":      [0.6, 0.75, 1.0],
    "disc_rate":        [0.035, 0.055, 0.08],
    "crop_horizon":     [0.45, 0.6, 0.75],
    "animal_horizon":   [0.35, 0.5, 0.65],
    "mine_w":           [0.5, 0.7, 0.9],
    "opp_weight":       [0.5, 0.85, 1.15],
    "opp_mirror":       [0.4, 0.7, 1.0],
    "animal_hurdle":    [1.0, 1.25, 1.6],
    "animal_price_floor": [0.4, 0.55, 0.7],
    "animal_batch":     [2, 4, 6],
    "tile_cap":         [{"MELON": 8}, {"MELON": 12}, {"MELON": 16}],
    "zone_reach":       [3, 4, 6],
    "work_per_unit":    [16.0, 20.0, 25.0],
    "hand_floor":       [[[3, 4], [6, 8], [10, 11]], [[2, 5], [5, 9], [9, 12]]],
    "shed_target":      [80, 88, 95],
    "plan_lookahead":   [4, 10, 16],
    "plant_min_score":  [1.0, 3.0, 7.0],
    "drop_load":        [8, 14, 22],
    "wheat_spare":      [3, 5, 8],
    "herd_tight":       [1.0, 3.0, 6.0],
    "animal_spend_frac":[0.45, 0.6, 0.8],
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agent")
    ap.add_argument("--opps", default="starter")
    ap.add_argument("-n", type=int, default=8)
    ap.add_argument("--seed0", type=int, default=1)
    ap.add_argument("-w", type=int, default=9)
    ap.add_argument("--rounds", type=int, default=3)
    ap.add_argument("--out", default="best_params.json")
    ap.add_argument("--noswap", action="store_true")
    ap.add_argument("--start", default=None)
    args = ap.parse_args()

    opps = args.opps.split(",")
    seeds = list(range(args.seed0, args.seed0 + args.n))
    best = json.load(open(args.start)) if args.start and os.path.exists(args.start) else {}

    def evaluate(params):
        tot = 0.0
        for opp in opps:
            r = tune.score(args.agent, params, opp, seeds, args.w, not args.noswap)
            tot += r["bank"]
        return tot / len(opps)

    cur = evaluate(dict(best))
    print(f"start score={cur:.0f} params={best}", flush=True)
    t0 = time.time()
    for rnd in range(args.rounds):
        improved = False
        for key, vals in GRID.items():
            if key.endswith("_ignored"):
                continue
            base_val = best.get(key, "<default>")
            for v in vals:
                if v == base_val:
                    continue
                p = dict(best)
                p[key] = v
                sc = evaluate(p)
                mark = ""
                if sc > cur * 1.012:      # ~1.2% margin to beat seed noise
                    best[key] = v
                    cur = sc
                    improved = True
                    mark = "  <-- keep"
                    json.dump(best, open(args.out, "w"), indent=1)
                print(f"[r{rnd}] {key}={v!r:<34} {sc:>9.0f}{mark}", flush=True)
        print(f"== round {rnd} done, score={cur:.0f}, {time.time()-t0:.0f}s, "
              f"params={json.dumps(best)}", flush=True)
        if not improved:
            break
    json.dump(best, open(args.out, "w"), indent=1)
    print("FINAL", cur, json.dumps(best), flush=True)


if __name__ == "__main__":
    main()
