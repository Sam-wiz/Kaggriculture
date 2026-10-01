"""Coordinate descent on head-to-head MARGIN vs a reference opponent.

Pool win rate is saturated for h_over (NOTES), so the only usable signal for a
challenger is the margin against it. Writes the running best to a JSON file
after every accepted move so a long run survives an interruption.
"""
import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import tune  # noqa: E402

GRID = {
    "care_val":        [0.0, 0.15, 0.3, 0.5, 0.8],
    "feed_val":        [0.35, 0.55, 0.8, 1.1],
    "collect_val":     [0.3, 0.5, 0.8, 1.1],
    "fert_use_disc":   [0.4, 0.55, 0.8],
    "fert_keep_mult":  [0.5, 1.0, 1.5],
    "labour_travel":   [2.0, 2.3, 2.6, 3.0],
    "labour_animal":   [2.6, 3.4, 4.2],
    "labour_slack":    [0.85, 1.0, 1.15],
    "water_prod_val":  [0.0, 0.35, 0.7],
    "animal_hurdle":   [0.9, 1.25, 1.7],
    "animal_price_floor": [0.35, 0.55, 0.75],
    "animal_batch":    [2, 4, 6],
    "animal_last_buy": [16, 19, 22],
    "opp_weight":      [0.0, 0.4, 0.85],
    "mine_w":          [0.5, 0.7, 0.9],
    "crop_horizon":    [0.4, 0.6, 0.9],
    "unlock_trust":    [0.5, 1.0, 1.4],
    "hinge_meter":     [0.3, 0.5, 0.8, 1.2],
    "sell_bias_glut":  [1.6, 2.2, 3.0],
    "sell_bias_tight": [1.4, 2.0, 2.8],
    "shed_target":     [80, 88, 96],
    "drop_load":       [8, 14, 20],
    "plant_min_score": [1.0, 3.0, 6.0],
    "dist_pow":        [0.85, 1.0, 1.2],
    "reach_override":  [50.0, 200.0, 600.0],
    "zone_reach":      [4, 7, 10],
    "stick":           [1.0, 1.15],
    "feed_carry":      [1.5, 2.5],
    "feed_carry_min":  [3, 6],
    "tile_cap":        [{"MELON": 12}, {"MELON": 12, "CARROT": 8},
                        {"MELON": 12, "WHEAT": 14}, {"MELON": 16}],
    "animal_cap":      [{"GOOSE": 3}, {"GOOSE": 0}, {"GOOSE": 3, "SHEEP": 4},
                        {"GOOSE": 6}],
    "max_quads":       [3, 2],
    "land_days":       [[], [5, 8]],
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agent")
    ap.add_argument("--opp", default="port2/h_over.py")
    ap.add_argument("-n", type=int, default=24)
    ap.add_argument("--seed0", type=int, default=3000)
    ap.add_argument("-w", type=int, default=8)
    ap.add_argument("--rounds", type=int, default=3)
    ap.add_argument("--out", default="adaptive/best_a1.json")
    ap.add_argument("--start", default=None)
    args = ap.parse_args()

    seeds = list(range(args.seed0, args.seed0 + args.n))
    cur = {}
    if args.start and os.path.exists(args.start):
        cur = json.load(open(args.start))

    def sc(p):
        r = tune.score(args.agent, p, args.opp, seeds, args.w, True)
        return r["margin"], r

    best_m, r0 = sc(cur)
    print("start margin=%.0f bank=%.0f" % (best_m, r0["bank"]), flush=True)
    t0 = time.time()
    for rnd in range(args.rounds):
        improved = False
        for k, vals in GRID.items():
            base = cur.get(k, None)
            for v in vals:
                if v == base:
                    continue
                p = dict(cur)
                p[k] = v
                m, r = sc(p)
                mark = ""
                if m > best_m + 250:      # ignore sub-noise wiggles
                    best_m, cur, improved = m, p, True
                    mark = "  <-- ACCEPT"
                    json.dump(cur, open(args.out, "w"), indent=1)
                print("r%d %-20s=%-28s margin=%9.0f bank=%8.0f wr=%.3f%s"
                      % (rnd, k, str(v)[:28], m, r["bank"], r["wr"], mark), flush=True)
        print("== round %d done, best margin %.0f, %.0fs\n%s\n"
              % (rnd, best_m, time.time() - t0, json.dumps(cur)), flush=True)
        if not improved:
            break
    json.dump(cur, open(args.out, "w"), indent=1)
    print("BEST", json.dumps(cur), "margin", best_m)


if __name__ == "__main__":
    main()
