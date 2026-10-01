"""Does the mirror overlay starve pipe16's hiring?

The original overlay scored 0.225 vs bare pipe16 and was filed as "price-impact slot ordering does
not work". Before accepting that, check the mechanism: the overlay returns `sells + rest` and then
truncates to 10 slots, which pushes every HIRE behind every SELL and can drop orders off the end.

This counts, per seat, the HIRE orders actually submitted and the total market orders submitted,
with the variant in seat 0 and bare pipe16 in seat 1. Bare-vs-bare is the control: both seats must
match exactly. Any variant whose seat-0 hire count falls below seat 1 is broken, not refuted.
"""
import collections
import json
import sys

import harness

BASE = "subK_pipe16.py"
VARIANTS = [("bare (control)", BASE),
            ("passthru", "bench_frozen/pipe16_passthru.py"),
            ("broken", "bench_frozen/pipe16_broken.py"),
            ("posfix", "bench_frozen/pipe16_posfix.py")]


def counts_for(path, seed):
    c = [collections.Counter(), collections.Counter()]

    def on_step(step, state, env):
        for i in (0, 1):
            a = state[i].action
            if not isinstance(a, dict):
                continue
            for o in (a.get("market") or []):
                if not o:
                    continue
                c[i][o[0]] += 1
                c[i]["_orders"] += 1
            c[i]["_maxslots"] = max(c[i]["_maxslots"], len(a.get("market") or []))

    r = harness.run_episode(path, BASE, seed=seed, on_step=on_step, catch_errors=True)
    return c, r


if __name__ == "__main__":
    seeds = [r["seed"] for r in json.load(open("data/seedindex_900000_1400.json"))][:3]
    print(f"variant in seat 0, bare pipe16 in seat 1; seeds {seeds}\n")
    print(f"{'variant':<16}{'seat0 HIRE':>12}{'seat1 HIRE':>12}{'s0 orders':>11}"
          f"{'s1 orders':>11}{'s0 maxslot':>12}{'money s0':>12}{'money s1':>12}{'status':>10}")
    for lab, path in VARIANTS:
        H0 = H1 = O0 = O1 = MS = 0
        m0 = m1 = 0.0
        st = "OK"
        for s in seeds:
            c, r = counts_for(path, s)
            H0 += c[0]["HIRE"]; H1 += c[1]["HIRE"]
            O0 += c[0]["_orders"]; O1 += c[1]["_orders"]
            MS = max(MS, c[0]["_maxslots"])
            m0 += r["reward"][0]; m1 += r["reward"][1]
            if r["status"][0] != "DONE" or r["errors"][0]:
                st = "ERR:" + str(r["errors"][0])[:24]
        n = len(seeds)
        flag = "  <-- HIRES LOST" if H0 < H1 * 0.95 else ""
        print(f"{lab:<16}{H0/n:>12.0f}{H1/n:>12.0f}{O0/n:>11.0f}{O1/n:>11.0f}"
              f"{MS:>12}{m0/n:>12,.0f}{m1/n:>12,.0f}{st:>10}{flag}")
