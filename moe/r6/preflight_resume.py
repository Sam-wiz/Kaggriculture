"""Offline-only preflight: loader, official engine, strict exception diagnostic.

No submission or network calls. Output is saved after each game.
"""
import contextlib
import io
import json
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / 'moe/r3/build/opus'))
from kaggle_load_check import load_like_kaggle
from run import load
import kagsim


def main():
    out = ROOT / 'moe/r6/build/resume'
    original = ROOT / 'rivalsGH/r34l-rudr44_kaggriculture/agents_v8.py'
    source = original.read_text()
    caught = '        except Exception:\n            return {"farmer": ["PASS"], "hands": [], "market": []}'
    assert source.count(caught) == 1
    strict = out / 'r34_v8_strict.py'
    strict.write_text(source.replace(caught, '        except Exception:\n            raise', 1))
    results = []

    def save(row):
        results.append(row)
        (out / 'r34_preflight.json').write_text(json.dumps(results, indent=2))
        print(json.dumps(row), flush=True)

    for path in (original, strict):
        fn = load_like_kaggle(str(path))
        save(dict(check='loader', path=str(path.relative_to(ROOT)), callable=fn.__name__, ok=True))

    for seed in (9203001, 9203002, 9203003):
        a, _ = load(str(strict), 'strict')
        b, _ = load('subAA_harvest.py', 'baseline')
        game = kagsim.Game(seed=seed)
        max_time = 0
        started = time.monotonic()
        for step in range(719):
            start = time.monotonic()
            action = a(game.observe(0))
            max_time = max(max_time, time.monotonic()-start)
            game.step(action, b(game.observe(1)))
        save(dict(check='strict_closed_loop', seed=seed, rewards=[game.reward(i) for i in (0,1)],
                  seconds=time.monotonic()-started, max_action_seconds=max_time, errors=0))

    # Use the official environment and its real file loader, both seats. Strict
    # version differs only by re-raising the public agent's catch-all exception.
    with contextlib.redirect_stdout(io.StringIO()):
        from kaggle_environments import make
    for seat in (0,1):
        paths = [str(strict), str(ROOT/'subAA_harvest.py')]
        if seat:
            paths.reverse()
        env = make('kaggriculture', configuration={'episodeSteps':720, 'seed':9203001}, debug=True)
        started = time.monotonic()
        env.run(paths)
        final = env.steps[-1]
        save(dict(check='official_env', seed=9203001, candidate_seat=seat,
                  rewards=[s.reward for s in final], statuses=[s.status for s in final],
                  seconds=time.monotonic()-started, steps=len(env.steps)))
        assert all(s.status == 'DONE' for s in final)


if __name__ == '__main__':
    main()
