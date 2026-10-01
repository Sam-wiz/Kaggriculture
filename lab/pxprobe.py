import importlib.util,collections
import kaggle_environments.envs.kaggriculture.kaggriculture as ENG
from kaggle_environments import make
def loadm(p):
    spec=importlib.util.spec_from_file_location('m'+str(abs(hash(p))%99999),p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
px=collections.defaultdict(list)
_ob=ENG.Market if hasattr(ENG,'Market') else None
env=make('kaggriculture',configuration={'episodeSteps':720,'seed':700},debug=False)
# wrap step to record prices
steps=[]
_orig=env.step
def rec(actions,logs=None):
    r=_orig(actions,logs)
    st=env.steps[-1][0]['observation']
    for it in ('STRAWBERRY','MELON','MILK','WOOL','EGG','CARROT','WHEAT','FERTILIZER'):
        px[it].append((st['step'],st['market']['prices'][it]))
    return r
env.step=rec
env.run([loadm('subV_sirxP.py').agent,loadm('subV_sirxP.py').agent])
for it in ('STRAWBERRY','MELON','MILK','WOOL'):
    ser=px[it]
    for lo in (480,576,600,648,672,696):
        hi=lo+24
        vals=[p for s,p in ser if lo<=s<hi]
        print(f"{it:11s} steps {lo}-{hi}: avg {sum(vals)/len(vals):6.1f} (n={len(vals)})")
    print()
