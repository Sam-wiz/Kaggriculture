"""Dump the planner's internal crop/animal valuations during a live episode."""
import sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import harness, importlib.util

def load(path):
    spec = importlib.util.spec_from_file_location("probe_agent", path)
    m = importlib.util.module_from_spec(spec); sys.modules["probe_agent"]=m
    spec.loader.exec_module(m); return m

def run(path, opp="starter", seed=1, days=(0,2,4,6,8,10,12,14,18,22)):
    m = load(path)
    A = m._AGENT
    inner = m.agent
    seen = set()
    def wrapped(obs):
        a = inner(obs)
        d = obs["day"]
        if d in days and d not in seen and obs["hour"] == 3:
            seen.add(d)
            scores = {}
            for c in m.CROPS:
                r = A.crop_value(c, d, A.supply(c) if hasattr(A,'supply') else A.pipeline[c]*0.7)
                scores[c] = None if r is None else round(r[0], 1)
            plan = collections.Counter(A.plan)
            best = A.best_animal(A.money)
            anim = {}
            for name, an in m.ANIMALS.items():
                pd = A.day_left - an["first"]
                if pd < 3: anim[name]="-"; continue
                per = min(1+an["interval"], an["held"])/an["interval"]
                u = per*pd
                pr = A.forecast(an["product"], pd*0.5,
                                extra=(A.supply(an["product"]) if hasattr(A,'supply') else 0)+u*0.5)
                anim[name] = f"{pr}x{u:.0f}"
            print(f"d{d:>2} $={A.money:>7.0f} tight={getattr(A,'cash_tight','-')} "
                  f"empty={len(A.empty):>2} anim={A.n_animals:>2} hands={A.hands_target:>2} "
                  f"| scores {scores} | plan {dict(plan)} | pick={best} {anim}")
        return a
    r = harness.run_episode(wrapped, opp, seed=seed, catch_errors=False)
    print("final", r["reward"])

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else "starter",
        int(sys.argv[3]) if len(sys.argv)>3 else 1)
