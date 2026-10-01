"""Resumable, hash-keyed closed-loop study; errors are failures, never PASSes.

Usage: .venv/bin/python moe/r6/resume_study.py MANIFEST OUTPUT [WORKERS]
Manifest: list of {a: path, b: path, seed: int, sw: 0 or 1}. Bootstrap by seed.
Uses the historical RR's 719 transitions for comparability, not 720 duplicated seats.
"""
import collections
import hashlib
import inspect
import json
import os
from pathlib import Path
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'moe/r3/build/opus'))
from run import load, tele
import kagsim


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def key(row):
    return row['sha_a'], row['sha_b'], row['seed'], row.get('sw', 0)


def call(fn, obs, two_args):
    action = fn(obs, None) if two_args else fn(obs)
    if not isinstance(action, dict):
        raise TypeError('Agent returned ' + type(action).__name__)
    return action


def job(spec):
    started = time.monotonic()
    row = dict(spec, sw=spec.get('sw', 0))
    try:
        assert digest(spec['a']) == spec['sha_a']
        assert digest(spec['b']) == spec['sha_b']
        a, ma = load(spec['a'], 'resume_a')
        b, mb = load(spec['b'], 'resume_b')
        internal_errors = []
        # V8 catches failures one level above _act. Observe them while preserving
        # its exact action/fallback behavior; exclude such games from evidence.
        if spec['a'].endswith('r34l-rudr44_kaggriculture/agents_v8.py'):
            original_act = ma._act
            def counted_act(*args, **kwargs):
                try:
                    return original_act(*args, **kwargs)
                except Exception as exc:
                    internal_errors.append(repr(exc))
                    raise
            ma._act = counted_act
        two = [len(inspect.signature(f).parameters) >= 2 for f in (a, b)]
        game = kagsim.Game(seed=int(spec['seed']))
        for step in range(719):
            row['step'] = step
            if row['sw']:
                game.step(call(b, game.observe(0), two[1]), call(a, game.observe(1), two[0]))
            else:
                game.step(call(a, game.observe(0), two[0]), call(b, game.observe(1), two[1]))
        row.update(ra=float(game.reward(row['sw'])), rb=float(game.reward(1-row['sw'])),
                   telemetry_a=tele(ma), telemetry_b=tele(mb))
        censor = getattr(ma, '_RESUME_CENSOR_REPORT', None)
        if censor is not None:
            row['censor'] = dict(censor)
        if spec['a'].endswith('r34l-rudr44_kaggriculture/agents_v8.py'):
            row['internal_exception_count'] = len(internal_errors)
            if internal_errors:
                row['err'] = 'Internal agent exceptions: ' + repr(internal_errors[:3])
    except Exception as exc:
        row['err'] = repr(exc)
    finally:
        # Imported agents can hold megabytes of decoded tapes. Drop their module
        # registry entries between jobs without recycling executor workers.
        for name in list(sys.modules):
            if name.startswith(('O_resume_a_', 'O_resume_b_')):
                del sys.modules[name]
    row['seconds'] = round(time.monotonic() - started, 3)
    return row


def summarize(rows):
    groups = collections.defaultdict(list)
    for row in rows:
        groups[(row['a'], row['b'])].append(row)
    for (a, b), group in sorted(groups.items()):
        ok = [r for r in group if 'err' not in r]
        w = sum(r['ra'] > r['rb'] for r in ok)
        loss = sum(r['ra'] < r['rb'] for r in ok)
        margin = sum(r['ra'] - r['rb'] for r in ok) / max(1, len(ok))
        print(json.dumps(dict(a=a, b=b, n=len(group), wins=w, losses=loss,
                              ties=len(ok)-w-loss, errors=len(group)-len(ok),
                              margin=round(margin, 2))), flush=True)


def main():
    os.chdir(ROOT)
    os.nice(10)
    manifest, out = map(Path, sys.argv[1:3])
    workers = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    specs = json.loads(manifest.read_text())
    hashes = {p: digest(p) for s in specs for p in (s['a'], s['b'])}
    for spec in specs:
        spec.update(sha_a=hashes[spec['a']], sha_b=hashes[spec['b']])
    rows = [json.loads(line) for line in out.read_text().splitlines()] if out.exists() else []
    done = {key(r) for r in rows}
    pending = {key(s): s for s in specs if key(s) not in done}
    print(f'{len(pending)} pending unique games; {len(done)} stored; workers={workers}', flush=True)
    with ProcessPoolExecutor(max_workers=workers) as pool, out.open('a') as f:
        futures = [pool.submit(job, s) for s in pending.values()]
        for i, future in enumerate(as_completed(futures), 1):
            row = future.result()
            f.write(json.dumps(row) + '\n')
            f.flush()
            rows.append(row)
            if i % 10 == 0 or 'err' in row:
                print(f'{i}/{len(pending)}' + (f" ERROR {row['a']} {row['err']}" if 'err' in row else ''), flush=True)
    wanted = {key(s) for s in specs}
    summarize([r for r in rows if key(r) in wanted])


if __name__ == '__main__':
    main()
