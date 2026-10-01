"""Report complete candidate matrices. Historical RR map is not private-rank evidence."""
import collections
import hashlib
import json
from pathlib import Path
import random
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'moe/r6/build/resume'
sys.path.insert(0, str(ROOT / 'moe/r4/build/opus'))
import rr

ANCHORS = {'subW_shepherd.py':'shep', 'subX_hyb2965.py':'hyb',
           'subV2_f55rec.py':'f55V2', 'subV_sir2.py':'sirV1',
           'subK2_pipe16.py':'pipe16', 'subY_C1_predict2.py':'C1'}
LIVE = dict(shep=2100, hyb=1974, f55V2=1930, sirV1=1897, pipe16=1800)


def read(name):
    path = OUT / name
    return [json.loads(s) for s in path.read_text().splitlines()] if path.exists() else []


def complete(name):
    specs = json.loads((OUT/(name+'_manifest.json')).read_text())
    rows = read(name+'.jsonl')
    key = lambda r: (r['a'],r['b'],r['seed'],r.get('sw',0))
    required = {key(r) for r in specs}
    found = [key(r) for r in rows]
    assert len(found)==len(set(found)), 'duplicate games in '+name
    assert set(found)<=required, 'unexpected games in '+name
    print(name, len(rows), '/', len(required), flush=True)
    if set(found)!=required:
        return None
    assert all('err' not in r for r in rows), 'errors in '+name
    hashes = {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for r in rows for p in (r['a'],r['b'])}
    assert all(r['sha_a']==hashes[r['a']] and r['sha_b']==hashes[r['b']] for r in rows)
    assert all(r.get('internal_exception_count')==0 for r in rows), 'missing internal exception audit'
    return rows


def summary(rows):
    groups=collections.defaultdict(list)
    for row in rows:
        groups[(row['a'],row['b'])].append(row)
    result=[]
    for (a,b),group in sorted(groups.items()):
        good=[r for r in group if 'err' not in r]
        w=sum(r['ra']>r['rb'] for r in good)
        loss=sum(r['ra']<r['rb'] for r in good)
        result.append(dict(a=a,b=b,games=len(group),seeds=len({r['seed'] for r in group}),
                           wins=w,losses=loss,ties=len(good)-w-loss,errors=len(group)-len(good),
                           mean_margin=sum(r['ra']-r['rb'] for r in good)/max(1,len(good))))
    return result


def fit_batch(weights):
    """Same 2000 MM iterations and prior as rr.fit, vectorized over bootstraps."""
    n=weights.shape[-1]
    scores=np.zeros(weights.shape[:-1])
    games=weights+weights.swapaxes(-1,-2)+1
    idx=np.arange(n)
    games[:,idx,idx]=0
    numerator=weights.sum(axis=-1)+.5
    for _ in range(2000):
        strength=np.exp(scores)
        denom=(games/(strength[:,:,None]+strength[:,None,:])).sum(axis=-1)
        scores=np.log(numerator/denom)
        scores-=scores.mean(axis=-1,keepdims=True)
    return scores*400/np.log(10)


def rr_map(candidate):
    base=[json.loads(l) for l in (ROOT/'moe/r4/build/opus/rr_retro.jsonl').read_text().splitlines()]
    assert all('err' not in r for r in base)
    rows=base+[dict(r,a='V8',b=ANCHORS[r['b']]) for r in candidate]
    names=sorted({r['a'] for r in rows}|{r['b'] for r in rows})
    ni={n:i for i,n in enumerate(names)}
    seeds=list(range(9100001,9100021))
    by_seed=np.zeros((len(seeds),len(names),len(names)))
    for r in rows:
        i,j=ni[r['a']],ni[r['b']]
        outcome=float(r['ra']>r['rb'])+.5*float(r['ra']==r['rb'])
        by_seed[r['seed']-seeds[0],i,j]+=outcome
        by_seed[r['seed']-seeds[0],j,i]+=1-outcome
    rng=random.Random(7)
    weights=[by_seed.sum(axis=0)]
    for _ in range(200):
        weights.append(by_seed[[rng.randrange(len(seeds)) for _ in seeds]].sum(axis=0))
    fitted=fit_batch(np.array(weights))
    # Independently check the vectorized point against the original implementation.
    import contextlib,io
    tmp=OUT/'r34_rr_fit_input.jsonl'
    tmp.write_text(''.join(json.dumps(r)+'\n' for r in rows))
    with contextlib.redirect_stdout(io.StringIO()): original=rr.fit(str(tmp))
    assert max(abs(original[n]-fitted[0,ni[n]]) for n in names)<1e-7
    xs=fitted[:,[ni[n] for n in LIVE]]
    ys=np.array(list(LIVE.values()))
    mx=xs.mean(axis=1)
    slope=((xs-mx[:,None])*(ys-ys.mean())).sum(axis=1)/((xs-mx[:,None])**2).sum(axis=1)
    mapped=ys.mean()+slope*(fitted[:,ni['V8']]-mx)
    bootstrap=sorted(mapped[1:].tolist())
    lo,hi=bootstrap[10],bootstrap[189]
    return dict(point=float(mapped[0]),lower90=lo,upper90=hi,unique_seeds=20,
                games=len(candidate),method='historical fixed-anchor map, seed bootstrap n=200',
                passes_old_gate=bool(mapped[0]>2329 and lo>2152),
                limitations='Extrapolates from older weaker lineage anchors; not calibrated for an adaptive agent or a top-10 private prediction.',
                submission_hold=True,vectorized_fit_verified=True)


def holdout_report(rows):
    results=[]
    for opponent in sorted({r['b'] for r in rows}):
        group=[r for r in rows if r['b']==opponent]
        scores=collections.defaultdict(list)
        for r in group:
            scores[r['seed']].append(float(r['ra']>r['rb'])+.5*float(r['ra']==r['rb']))
        assert len(scores)==40 and all(len(v)==2 for v in scores.values())
        vals=np.array([np.mean(scores[s]) for s in sorted(scores)])
        rng=np.random.default_rng(20260927)
        bs=vals[rng.integers(0,40,size=(20000,40))].mean(axis=1)
        result=summary(group)[0]
        result.update(win_rate=float(vals.mean()),win_rate_95_seed_bootstrap=np.quantile(bs,[.025,.975]).tolist(),
                      seats={str(sw):summary([r for r in group if r['sw']==sw])[0] for sw in (0,1)})
        results.append(result)
    return results


def main():
    report={'submission_hold':'No uploads until BOTH C1R2 and Harvest converge.'}
    forecast=read('forecast.jsonl')
    report['forecast']=summary(forecast)
    report['github_screen']=summary(read('github.jsonl'))
    cand=complete('r34_rr')
    if cand is not None:
        report['rr']=rr_map(cand)
        report['rr_matches']=summary(cand)
    held=complete('r34_holdout')
    if held is not None:
        report['holdout']=holdout_report(held)
    report['complete']=cand is not None and held is not None and len(forecast)==80
    (OUT/'RESULTS.json').write_text(json.dumps(report,indent=2))
    print(json.dumps({k:v for k,v in report.items() if k not in ('github_screen','rr_matches')},indent=2))


if __name__=='__main__':
    main()
