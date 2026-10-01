"""Build the pre-registered Harvest forecaster ablation and screening manifests."""
import ast
import collections
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'moe/r6/build/resume'
OUT.mkdir(exist_ok=True)
base = ROOT / 'moe/r6/build/opus/hv/harvest_q.py'
source = base.read_text()
tree = ast.parse(source)
node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == '_v92_q_update')
old = ast.get_source_segment(source, node)
new = old.replace('    seen = st["obs"]', '    seen = st["obs"]\n    observed = st.setdefault("observable", set())')
new = new.replace('            sold = inv[item]', '            observed.add((step - 1, i))\n            sold = inv[item]')
new = new.replace('                else:\n                    f[c] += 1',
                  '                elif all((t, i) in observed for t in (tau - 1, tau, tau + 1)):\n                    f[c] += 1')
new = new.replace('            if (tau, i) in seen:',
                  '            if not hit and not all((t, i) in observed for t in (tau - 1, tau, tau + 1)):\n'
                  '                _RESUME_CENSOR_REPORT["penalties_skipped"] += len(index.get((tau, i), ()))\n'
                  '            if (tau, i) in seen:')
assert new != old and new.count('elif all(') == 1
candidate = source.replace(old, '_RESUME_CENSOR_REPORT = {"penalties_skipped": 0}\n\n' + new, 1)
candidate += '\n# Explicit Kaggle last-callable selection.\n_resume_selected = agent\nglobals().pop("agent", None)\nagent = _resume_selected\n'
dest = OUT / 'harvest_q_censor.py'
dest.write_text(candidate)

# Mechanism regression: all three ticks observed -> negative evidence; any unknown -> no penalty.
isolated = ast.Module(body=[ast.parse(new).body[0]], type_ignores=[])
probe = []
for observable, hit, expected in [(set(), False, 0), ({149,150,151}, False, -1), ({150,151}, False, 0), (set(), True, 1.5)]:
    scope = {'_V92_Q_ITEMS': ('MILK','WOOL','STRAWBERRY'), '_V92_Q_PF': 1., '_V92_Q_PM': .5,
             '_V9_RACE': {}, '_RESUME_CENSOR_REPORT': {'penalties_skipped':0}}
    exec(compile(isolated, '<censor probe>', 'exec'), scope)
    st = dict(obs={(150,0):8} if hit else {}, observable={(t,0) for t in observable},
              evs=[{(150,0):8},{}], index={(150,0):[0]}, m=[0,0], f=[0,0], near=[0,0],
              score=[0.,0.], best=0, done=150)
    scope['_v92_q_update']({'player':0, 'step':152},st)
    assert st['score'][0] == expected, (observable, hit, st)
    probe.append(dict(observable=sorted(observable), hit=hit, score=st['score']))
(OUT / 'censor_probe.json').write_text(json.dumps(probe, indent=2))

H = 'subAA_harvest.py'
HQ = str(base.relative_to(ROOT))
HQC = str(dest.relative_to(ROOT))
jobs = [dict(a=a,b=b,seed=s) for a in (HQ,HQC) for s in range(9201001,9201021)
        for b in (H,'subZ_C1R2.py')]
(OUT / 'forecast_manifest.json').write_text(json.dumps(jobs,indent=2))

cs = json.loads((ROOT/'moe/r6/screen_candsGH.json').read_text())
rs = [json.loads(l) for l in (ROOT/'moe/r6/screenGH5.jsonl').read_text().splitlines()]
names = collections.Counter(n for n,p in cs)
survivors = {n for n,p in cs if names[n] == 1 and sum('err' not in r and r['ra']>r['rb'] for r in rs if r['a']==n)>=3}
# Every member of the one ambiguous group with any wins is re-screened by path.
paths = [p for n,p in cs if n in survivors or n == 'mooman0222/main.py']
jobs = [dict(a=p,b=H,seed=s) for p in paths for s in range(9202001,9202006)]
(OUT / 'github_manifest.json').write_text(json.dumps(jobs,indent=2))
metadata = {'base':str(base.relative_to(ROOT)), 'candidate':HQC,
            'sha256':hashlib.sha256(candidate.encode()).hexdigest(),
            'forecast_games':80, 'github_candidates':len(paths), 'github_games':len(jobs),
            'old_labels':len(names), 'old_files':len(cs), 'old_rows':len(rs)}
(OUT / 'build.json').write_text(json.dumps(metadata,indent=2))
print(json.dumps(metadata,indent=2))
