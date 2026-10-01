"""Load an agent exactly the way Kaggle does: exec the source with NO __file__.

kaggle_environments/agent.py does `exec(code_object, env)` on the raw file and then
picks the last callable out of `env`. Nothing sets __file__, so any path-based
bootstrap raises NameError before the agent is ever called -- which is invisible to
a harness that imports by file path.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def load_like_kaggle(path):
    """Mirror kaggle_environments.agent.get_last_callable EXACTLY.

    It returns `[v for v in env.values() if callable(v)][-1]` -- the LAST callable by
    dict insertion order, with NO preference for the name `agent`. Redefining `agent`
    keeps its original insertion position, so ANY helper function defined after the
    first `def agent` silently becomes the submitted agent. Preferring the name here
    gave a false pass and cost a submission slot.
    """
    src = open(path).read()
    env = {}
    exec(compile(src, path, "exec"), env)   # noqa: S102 - mirrors the platform loader
    callables = [v for v in env.values() if callable(v)]
    if not callables:
        raise RuntimeError("no callable found in %s" % path)
    chosen = callables[-1]
    named = env.get("agent")
    if callable(named) and chosen is not named:
        raise RuntimeError(
            "Kaggle would run %r, NOT your `agent` -- it takes the last callable by "
            "insertion order. Re-insert agent last (`del agent; agent = _my_agent`)."
            % getattr(chosen, "__name__", chosen))
    return chosen


def real_env_check(path, opp="starter", seed=1):
    """The definitive test: run it through kaggle_environments exactly as Kaggle does."""
    from kaggle_environments import make
    env = make("kaggriculture", configuration={"episodeSteps": 720})
    env.run([path, opp])
    last = env.steps[-1]
    return [s.reward for s in last], [s.status for s in last]


if __name__ == "__main__":
    import harness
    path = sys.argv[1]
    opp = sys.argv[2] if len(sys.argv) > 2 else path
    fn = load_like_kaggle(path)
    print("loaded OK (no __file__):", fn)
    oppfn = load_like_kaggle(opp) if opp.endswith(".py") else opp
    for seed in (7, 1, 42):
        r = harness.run_episode(fn, oppfn, seed=seed, catch_errors=True)
        ok = r["errors"] == [None, None] and r["reward"][0] != 3000.0
        print(f"  seed {seed}: {r['reward']} {r['status']} err={r['errors']} -> {'OK' if ok else 'FAIL'}")
    rew, st = real_env_check(path)
    ok = st == ["DONE", "DONE"] and rew[0] not in (None, 3000.0)
    print(f"  real kaggle_environments run: rewards={rew} status={st} -> {'OK' if ok else 'FAIL'}")
