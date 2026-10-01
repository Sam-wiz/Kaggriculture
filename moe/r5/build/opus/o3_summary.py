"""Summarise oracle_O3.jsonl (written BEFORE the 60-seed run; this is the pre-registration).
Option  : O3 = C1's own d18 SE-tomato executor (V219) with its CXTB revenue gate forced on vs forced off.
Primary : Pearson r(LOCKED forecast delta on-off, top profile, R=4; realised delta on-off) over worlds where the
          option is structurally feasible (struct True; else on == off and delta == 0). Bar r >= 0.5 (opusb/claude-code).
Second. : sign agreement; r for the c1 profile; CXTB's own analytic feature (rev - 9000) as baseline r;
          luna's rule: payoff of the rollout-SELECTED choice (on iff forecast > 0) vs native C1 (= CXTB's choice),
          per game over all seeds; oracle ceiling mean max(0, best arm - native).
Checks  : nat equals on or off to the dollar in every world (fires); on arm commits in every struct world; errors 0;
          P2 chaos floor."""
import json, math, statistics as st, sys
OP = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r5/build/opus"
REC = sys.argv[1] if len(sys.argv) > 1 else OP + "/oracle_O3.jsonl"
LOCK = sys.argv[2] if len(sys.argv) > 2 else OP + "/oracle_O3_locks.jsonl"
recs = {r["seed"]: r for r in map(json.loads, open(REC))}
locks = {}
for r in map(json.loads, open(LOCK)):
    locks.setdefault(r["seed"], r)          # first lock per seed is the binding one
seeds = sorted(recs)
for s in seeds:
    assert recs[s]["fc_delta"] == locks[s]["fc_delta"], s
    assert locks[s]["t"] < 1e10


def m_se(xs):
    return st.mean(xs), (st.stdev(xs) / math.sqrt(len(xs)) if len(xs) > 1 else 0.0)


def pearson(a, b):
    ma, mb = st.mean(a), st.mean(b)
    c = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    return c / math.sqrt(sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b))


def spearman(a, b):
    rk = lambda v: {i: r for r, i in enumerate(sorted(range(len(v)), key=lambda i: v[i]))}
    ra, rb = rk(a), rk(b)
    return pearson([ra[i] for i in range(len(a))], [rb[i] for i in range(len(b))])


out = []
P = lambda *a: out.append(" ".join(str(x) for x in a))
tel = lambda s: recs[s]["real"]["on"]["tel"]
P("# O3 selector check: %d paired fresh seeds %d-%d, seats alternate, opponent pristine C1, kag_dc, fork step 432"
  % (len(seeds), seeds[0], seeds[-1]))
errs = [(s, a) for s in seeds for a, v in recs[s]["real"].items() if "err" in v or any(v.get("errors") or [])]
P("errors in real continuations:", errs or 0)
P("nat == on|off to the dollar:", sum(bool(recs[s]["nat_is"]) for s in seeds), "/", len(seeds))
struct = [s for s in seeds if tel(s)["struct"]]
native = [s for s in seeds if tel(s)["native"]]
P("struct-feasible %d/%d; CXTB native-open %d/%d %s" % (len(struct), len(seeds), len(native), len(seeds), native))
P("on arm committed in struct worlds: %d/%d; confirmed plants mean %.1f; harvest units mean %.1f" % (
    sum(recs[s]["real"]["on"]["tel"]["committed"] for s in struct), len(struct),
    st.mean(recs[s]["real"]["on"]["tel"].get("confirmed_plants", 0) for s in struct),
    st.mean(recs[s]["real"]["on"]["tel"].get("confirmed_harvest_units", 0) for s in struct)))
P("off arm committed anywhere:", sum(recs[s]["real"]["off"]["tel"]["committed"] for s in seeds))
p2 = [recs[s]["p2"] for s in seeds]
P("P2 chaos floor: mean %+.0f, max |.| %.0f, nonzero %d" % (st.mean(p2), max(abs(x) for x in p2), sum(x != 0 for x in p2)))

d = {s: recs[s]["delta"] for s in seeds}
P("\n## realised delta on - off (our bank), struct worlds")
for name, grp in (("all struct", struct), ("native-open", [s for s in struct if s in native]),
                  ("native-closed", [s for s in struct if s not in native])):
    if grp:
        m, se = m_se([d[s] for s in grp])
        P("%-14s n=%2d  mean %+7.0f (SE %5.0f)  >0 in %d" % (name, len(grp), m, se, sum(d[s] > 0 for s in grp)))

P("\n## LOCKED forecast vs realised (primary: top profile)")
for pn in ("top", "c1"):
    f = [locks[s]["fc_delta"][pn] for s in struct]; r = [d[s] for s in struct]
    agree = sum((a > 0) == (b > 0) for a, b in zip(f, r))
    P("%-3s r %.3f  spearman %.3f  sign %d/%d  mean fc %+.0f vs real %+.0f  MAE %.0f" % (
        pn, pearson(f, r), spearman(f, r), agree, len(r), st.mean(f), st.mean(r), st.mean(abs(a - b) for a, b in zip(f, r))))
    for name, grp in (("native-open", [s for s in struct if s in native]), ("native-closed", [s for s in struct if s not in native])):
        if len(grp) > 2:
            P("    within %-13s n=%2d r %.3f" % (name, len(grp), pearson([locks[s]["fc_delta"][pn] for s in grp], [d[s] for s in grp])))
cx = [tel(s)["rev"] - 9000 for s in struct]
P("CXTB baseline (rev - 9000) r %.3f spearman %.3f" % (pearson(cx, [d[s] for s in struct]), spearman(cx, [d[s] for s in struct])))

P("\n## policy value vs native C1 (per game, all %d seeds)" % len(seeds))
nat_bank = lambda s: recs[s]["real"]["nat"]["bank"]
arm_bank = lambda s, a: recs[s]["real"][a]["bank"]
for pn in ("top", "c1"):
    for margin in (0, 500, 1000):
        pay = [arm_bank(s, "on" if locks[s]["fc_delta"][pn] > margin else "off") - nat_bank(s) for s in seeds]
        m, se = m_se(pay)
        flips = sum(((locks[s]["fc_delta"][pn] > margin) != (s in native)) for s in struct)
        P("%-3s select on iff fc > %4d: %+6.0f/g (SE %4.0f), flips vs native %d, flips that lose %d" % (
            pn, margin, m, se, flips, sum(1 for x in pay if x < 0)))
orc = [max(arm_bank(s, "on"), arm_bank(s, "off")) - nat_bank(s) for s in seeds]
P("oracle ceiling vs native: %+.0f/g; worlds where native is wrong: %d" % (st.mean(orc), sum(x > 0 for x in orc)))

P("\n## per-seed (struct worlds): seed me cash shops | native rev | fc_top fc_c1 | real | opp_committed")
for s in struct:
    r = recs[s]
    P("%d %d %6.0f %-40s | %d %5d | %+6.0f %+6.0f | %+6.0f | %s" % (
        s, r["me"], r["dawn_cash"], ",".join(x.split("_")[0][:5] for x in r["shops"]), tel(s)["native"], tel(s)["rev"],
        locks[s]["fc_delta"]["top"], locks[s]["fc_delta"]["c1"], d[s], r["real"]["on"]["opp_committed"]))
print("\n".join(out))
