"""Watch the live pair every 30 min; on convergence submit [M30B, v8] in that order.
Converged = for EACH member, max-min publicScore over the last 3 snapshots (1h) <= 12.
Guards: abort if the tracked refs aren't {56612454, 56611551} (user intervened).
Hard stop 2026-09-30 16:00 UTC: stop submitting, keep logging.
"""
import csv, io, json, subprocess, sys, time
from datetime import datetime, timezone
ROOT = "/Users/samrudh/Documents/Projects/kaggle/Kaggriculture"
KA = ROOT + "/.venv/bin/kaggle"
LOG = ROOT + "/moe/r7/build/devin/pair_watch.log"
EXPECTED = {"56612454": "Harvest", "56611551": "C1R2"}
EPS = 12.0
WINDOW = 3
DEADLINE = datetime(2026, 9, 30, 16, 0, tzinfo=timezone.utc)

M30B = ("subAB_m30b.py", "SLOT 2: Harvest Ledger V78 + _CA_MARGIN -30 + BRX2 sell-order permutation layer "
        "(learned native-vs-SIR rival-order model, online log-odds). RR-mapped 2402 [2192,2562] on opus "
        "lineage anchors vs Harvest 2329 / C1R2 2152 -> PASS pre-registered gate (moe/r6/THREAD.md). "
        "Held-out 17-3 vs m30, 19-1 vs Harvest; fires 367 permutations, 0 err. "
        "Credit: haodou092, guruprasaathas111 + Apache-2.0 chain. kaggle_load_check + official env DONE both seats.")
V8 = ("subAC_v8.py", "SLOT B hedge (team scores by better of two): r34l-rudr44 agents_v8 verbatim, "
      "different-class market-book agent (per-product books, town-demand forecasts, herd race-ordering). "
      "RR-mapped 2150 [2047,2229]; ~71% vs our chassis family; 0 overlapping failure seeds vs M30B = "
      "only measured cross-class decorrelation (moe/r7/THREAD.md). Public code permitted (#737788/#738837 "
      "host statements). Credit: r34l-rudr44. kaggle_load_check + official env DONE both seats.")

def log(msg):
    line = f"{datetime.now(timezone.utc).strftime('%H:%M:%S')} {msg}"
    print(line, flush=True)
    with open(LOG, "a") as f: f.write(line + "\n")

def subs():
    out = subprocess.run([KA, "competitions", "submissions", "kaggriculture", "-v"],
                         capture_output=True, text=True, timeout=180, cwd=ROOT, check=True).stdout
    rows = list(csv.DictReader(io.StringIO(out)))
    return [(r["ref"], float(r["publicScore"] or 0)) for r in rows[:2]]

def submit(path, msg):
    r = subprocess.run([KA, "competitions", "submit", "kaggriculture", "-f", path, "-m", msg],
                       capture_output=True, text=True, timeout=300, cwd=ROOT)
    log(f"submit {path}: rc={r.returncode} out={r.stdout.strip()[:200]} err={r.stderr.strip()[:200]}")
    return r.returncode == 0

def main():
    hist = []
    done = False
    while True:
        try:
            pair = subs()
        except Exception as e:
            log(f"fetch error {e!r}"); time.sleep(1800); continue
        refs = {r for r, _ in pair}
        if not done and refs != set(EXPECTED):
            log(f"ABORT: live refs {refs} != expected {set(EXPECTED)} — user intervened; watcher exits")
            return
        hist.append(pair); log(f"pair: {pair}")
        if not done and len(hist) >= WINDOW:
            last3 = hist[-WINDOW:]
            conv = True
            for member in range(2):
                scores = [s[member][1] for s in last3]
                if max(scores) - min(scores) > EPS: conv = False
            if conv:
                if datetime.now(timezone.utc) > DEADLINE:
                    log("converged but past deadline guard; not submitting"); done = True
                else:
                    log("CONVERGED — submitting M30B then v8")
                    ok1 = submit(*M30B); time.sleep(120)
                    try: log(f"mid pair: {subs()}")
                    except Exception as e: log(f"mid fetch err {e!r}")
                    if not ok1:
                        log("M30B submit failed — NOT submitting v8 (would leave [harvest, v8]); watcher exits")
                        return
                    ok2 = submit(*V8); time.sleep(120)
                    try: log(f"final pair: {subs()}")
                    except Exception as e: log(f"final fetch err {e!r}")
                    log(f"SUBMITTED: m30b={'ok' if ok1 else 'FAIL'} v8={'ok' if ok2 else 'FAIL'}")
                    return
        if datetime.now(timezone.utc) > DEADLINE and not done:
            log("DEADLINE GUARD passed without convergence — submissions held per user rule"); done = True
        time.sleep(1800)

if __name__ == "__main__":
    main()
