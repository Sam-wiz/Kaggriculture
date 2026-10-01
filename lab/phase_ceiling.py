import importlib.util,collections
import kaggle_environments.envs.kaggriculture.kaggriculture as ENG
from kaggle_environments import make
def loadm(p):
    spec=importlib.util.spec_from_file_location('m'+str(abs(hash(p))%99999),p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
FILLS=[];PX=collections.defaultdict(dict)
_sb=[None]
_oc=ENG._commit_unit;_opm=ENG._process_market
def _pm(state,env):_sb[0]=state;return _opm(state,env)
def _c(op,item,price,farm,private,market,shed_capacity=100):
    ok=_oc(op,item,price,farm,private,market,shed_capacity)
    if ok and op=='SELL':
        st=_sb[0][0].observation
        pl=0 if st.farms[0] is farm else 1
        FILLS.append((st.step,pl,item,price))
    return ok
ENG._commit_unit=_c;ENG._process_market=_pm
us=loadm('subV_sirxP.py').agent
env=make('kaggriculture',configuration={'episodeSteps':720,'seed':960},debug=False)
orig=env.step
def rec(a,logs=None):
    r=orig(a,logs);o=env.steps[-1][0]['observation']
    for it,v in o['market']['prices'].items():PX[it][o['step']]=v
    return r
env.step=rec
env.run([us,us])
# counterfactual: each sell at s (phase!=1) delayed to next s' with s'%4==1 (<=715)
gain=0;by_item=collections.Counter()
for s,pl,it,pr in FILLS:
    if pl!=0 or s<576:continue
    off=(1-s)%4
    if off==0:continue
    s2=s+off
    if s2>715:continue
    p2=PX[it].get(s2,pr)
    d=p2-pr
    gain+=d;by_item[it]+=d
print('phase-1-shift counterfactual gain (upper bound, ignores self-impact): $%.0f'%gain)
print(dict(by_item))
