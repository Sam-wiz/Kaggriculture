"""Summarise oracle_O1.jsonl: fires, paired deltas, oracle vs placebo floor, LOCKED forecast vs realised, and the
payoff of the rollout-selected choice (luna). Forecasts are read from oracle_O1_locks.jsonl (written before outcomes)."""
import json, math, statistics as st
B = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/moe/r5/build/opusb"
recs = {r["seed"]: r for r in map(json.loads, open(B + "/oracle_O1.jsonl"))}
locks = {r["seed"]: r for r in map(json.loads, open(B + "/oracle_O1_locks.jsonl"))}
seeds = sorted(recs)
assert set(seeds) == set(locks) and len(seeds) == 40
for s in seeds:   # the record's forecast must be the locked one
    assert recs[s]["fc_delta"] == locks[s]["fc_delta"], s


def fib(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def m_se(xs):
    return st.mean(xs), (st.stdev(xs) / math.sqrt(len(xs)) if len(xs) > 1 else 0.0)


def hire_cost(h):
    return sum(sum(fib(n) for n in range(k)) for k in h.values())


out = []
P = lambda *a: out.append(" ".join(str(x) for x in a))
P("# O1 oracle summary: %d paired fresh seeds %d-%d, seats alternate (seed %% 2), opponent pristine C1, kag_dc" %
  (len(seeds), seeds[0], seeds[-1]))
P("prefix mismatches S-vs-C namespaces through step 263:", sum(recs[s]["prefix_mismatch"] for s in seeds))
errs = [(s, a) for s in seeds for a, v in recs[s]["real"].items() if any(v.get("errors") or []) or "err" in v]
P("errors in real continuations:", errs or 0)

# ---- fires ----
P("\n## fires (arm committed its SE project; off = native C1)")
for a in ("off", "S", "C"):
    com = [s for s in seeds if recs[s]["real"][a]["tel"]["committed"]]
    se6 = [s for s in seeds if recs[s]["real"][a]["tel"]["se_animals"] >= 6]
    P("%-3s committed %2d/40, 6 SE animals at end %2d/40, product harvested mean %.0f, fert collected mean %.0f" % (
        a, len(com), len(se6), st.mean(recs[s]["real"][a]["tel"].get("sheep_wool_harvested", 0) for s in seeds),
        st.mean(recs[s]["real"][a]["tel"].get("sheep_fert_collected", 0) for s in seeds)))
native = [s for s in seeds if recs[s]["real"]["off"]["tel"]["committed"]]
fired = {a: [s for s in seeds if recs[s]["real"][a]["tel"]["committed"] and s not in native] for a in ("S", "C")}
P("native V233 (YARN world) already fires in off arm:", native)
P("O1 fires where native does not: S %d/40, C %d/40; SE land step (S arm) median %s" % (
    len(fired["S"]), len(fired["C"]),
    st.median([next(x for x in recs[s]["real"]["S"]["land"] if x >= 264) for s in fired["S"]])))
nofire = [s for s in seeds if s not in native and s not in fired["S"]]
P("S does not fire and native does not either:", nofire,
  [(recs[s]["real"]["S"]["tel"].get("sheep_budget_declines"), recs[s]["dawn_cash"]) for s in nofire])

# ---- paired deltas ----
P("\n## paired realised deltas vs off (our bank; margin = ours - opp)")
for a in ("S", "C", "P1", "P2"):
    d = [recs[s]["delta"][a] for s in seeds]; dm = [recs[s]["delta_margin"][a] for s in seeds]
    m, se = m_se(d); mm, sem = m_se(dm)
    wins = sum(1 for s in seeds if recs[s]["real"][a]["bank"] > recs[s]["real"][a]["opp"])
    loss = sum(1 for s in seeds if recs[s]["real"][a]["bank"] < recs[s]["real"][a]["opp"])
    P("%-2s bank %+8.0f (SE %5.0f)  margin %+8.0f (SE %5.0f)  >0 in %2d/40  W/L/T vs C1 %d/%d/%d" % (
        a, m, se, mm, sem, sum(x > 0 for x in d), wins, loss, 40 - wins - loss))
off_w = sum(1 for s in seeds if recs[s]["real"]["off"]["bank"] > recs[s]["real"]["off"]["opp"])
P("off arm (C1 vs C1) W/L/T: %d/%d/%d" % (off_w, sum(1 for s in seeds if recs[s]["real"]["off"]["bank"] < recs[s]["real"]["off"]["opp"]),
                                        sum(1 for s in seeds if recs[s]["real"]["off"]["bank"] == recs[s]["real"]["off"]["opp"])))

# ---- oracle vs placebo floor ----
P("\n## per-world oracle ceiling (mean of max(0, delta)); bar +$1,000/g")
g = lambda s, a: recs[s]["delta"][a]
for name, arms in (("S", ("S",)), ("C", ("C",)), ("S|C", ("S", "C")), ("placebo P1", ("P1",)), ("placebo P2", ("P2",)),
                   ("placebo P1|P2", ("P1", "P2"))):
    P("%-14s %+7.0f" % (name, st.mean(max([0] + [g(s, a) for a in arms]) for s in seeds)))
P("worlds with any arm > 0:", [(s, {a: g(s, a) for a in ("S", "C") if g(s, a) > 0}) for s in seeds if max(g(s, "S"), g(s, "C")) > 0])

# ---- mechanism: labour ----
P("\n## mechanism (fired S worlds): extra hires and their fib cost")
xs = fired["S"]
eh = [sum(recs[s]["real"]["S"]["hires"].values()) - sum(recs[s]["real"]["off"]["hires"].values()) for s in xs]
ec = [hire_cost(recs[s]["real"]["S"]["hires"]) - hire_cost(recs[s]["real"]["off"]["hires"]) for s in xs]
hd = [st.mean(recs[s]["real"]["off"]["hires"][str(d)] for s in xs) for d in range(11, 29)]
P("off-arm hires/day d11-28 (mean over fired worlds):", [round(v, 1) for v in hd])
P("S arm: extra hires/game %.1f, extra hire cost/game $%.0f (median $%.0f)" % (st.mean(eh), st.mean(ec), st.median(ec)))
lost_v219 = [s for s in seeds if recs[s]["real"]["off"]["tel"]["se_unlocked"] and not recs[s]["real"]["off"]["tel"]["committed"]]
P("worlds where off arm bought SE natively later (V219 day-18 tomato) and O1 pre-empts it: %d/40" % len(lost_v219))

# ---- locked forecast vs realised ----
for pn in ("top", "c1"):
    P("\n## LOCKED forecast vs realised, profile=%s (%s)" % (pn, "pre-registered runtime model" if pn == "top" else "matched-opponent sensitivity"))
    pairs = [(locks[s]["fc_delta"][pn][a], g(s, a), s, a) for s in seeds for a in ("S", "C")]
    live = [p for p in pairs if p[1] != 0]
    agree = sum(1 for f, r, *_ in live if (f > 0) == (r > 0))
    big = [p for p in live if abs(p[1]) > 1000]
    agree_big = sum(1 for f, r, *_ in big if (f > 0) == (r > 0))
    fs = [p[0] for p in live]; rs = [p[1] for p in live]
    mf, mr = st.mean(fs), st.mean(rs)
    cov = sum((f - mf) * (r - mr) for f, r in zip(fs, rs))
    corr = cov / math.sqrt(sum((f - mf) ** 2 for f in fs) * sum((r - mr) ** 2 for r in rs))
    P("sign agreement, all option-worlds with realised != 0: %d/%d; |realised| > $1k: %d/%d; Pearson r %.2f; "
      "mean forecast %+.0f vs mean realised %+.0f; MAE %.0f" % (agree, len(live), agree_big, len(big), corr, mf, mr,
                                                                 st.mean(abs(f - r) for f, r in zip(fs, rs))))
    pos = [(s, a, round(f), r) for f, r, s, a in pairs if f > 0]
    P("forecast > 0 cases (seed, arm, forecast, realised):", pos)
    sel = []
    for s in seeds:
        fc = locks[s]["fc_delta"][pn]
        best = max(("off", 0.0), ("S", fc["S"]), ("C", fc["C"]), key=lambda t: t[1])
        sel.append((s, best[0], 0 if best[0] == "off" else g(s, best[0])))
    pay = [x[2] for x in sel]
    m, se = m_se(pay)
    P("rollout-SELECTED payoff (argmax over off/S/C at margin 0): %+.0f/g (SE %.0f); chose S %d, C %d, off %d; "
      "vs oracle ceiling %+.0f" % (m, se, sum(x[1] == "S" for x in sel), sum(x[1] == "C" for x in sel),
                                   sum(x[1] == "off" for x in sel), st.mean(max(0, g(s, "S"), g(s, "C")) for s in seeds)))
    for a in ("S", "C"):
        pa = [g(s, a) if locks[s]["fc_delta"][pn][a] > 0 else 0 for s in seeds]
        P("  binary %s-only selection payoff %+.0f/g, fired in %d worlds" % (a, st.mean(pa), sum(locks[s]["fc_delta"][pn][a] > 0 for s in seeds)))

P("\n## per-seed table (bank deltas; fc = locked forecast, top profile)")
P("seed me dawn_cash shops_d11 | fcS fcC | realS realC | P1 P2")
for s in seeds:
    r = recs[s]; f = locks[s]["fc_delta"]["top"]
    P("%d %d %6.0f %-45s | %+7.0f %+7.0f | %+7.0f %+7.0f | %+4.0f %+4.0f" % (
        s, r["me"], r["dawn_cash"], ",".join(x.split("_")[0][:5] for x in r["shops_d11"]), f["S"], f["C"],
        g(s, "S"), g(s, "C"), g(s, "P1"), g(s, "P2")))
P("\nrollout wall time per rollout (M1): median %.2f s; real continuation median %.2f s" % (
    st.median(x["sec"] for s in seeds for pn in recs[s]["forecast"] for a in recs[s]["forecast"][pn] for x in recs[s]["forecast"][pn][a]),
    st.median(recs[s]["real"][a]["sec"] for s in seeds for a in recs[s]["real"])))
print("\n".join(out))
