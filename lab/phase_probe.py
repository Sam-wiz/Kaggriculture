import importlib.util,collections,sys
import kaggle_environments.envs.kaggriculture.kaggriculture as ENG
from kaggle_environments import make
def loadm(p):
    spec=importlib.util.spec_from_file_location('m'+str(abs(hash(p))%99999),p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
FILLS=[]
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
kosh=loadm('rivals/koshinm_kaggriculture-local-best-2026-09-21/_entry.py').agent
us=loadm('subV_sirxP.py').agent
env=make('kaggriculture',configuration={'episodeSteps':720,'seed':960},debug=False)
env.run([us,kosh])
print('rewards:',[s.reward for s in env.steps[-1]])
# premium sells days 24-29 (steps 576+), by seat x step%4
for pl,nm in ((0,'us'),(1,'koshinm')):
    ph=collections.defaultdict(lambda:[0,0])
    for s,p,it,pr in FILLS:
        if p==pl and s>=576 and it in ('WOOL','MILK','STRAWBERRY','MELON','EGG','CARROT'):
            ph[(it,s%4)][0]+=1;ph[(it,s%4)][1]+=pr
    print(f'--- {nm} premium fills by step%4 (units, avg$) ---')
    for it in ('WOOL','MILK','STRAWBERRY','MELON'):
        row=[]
        for m in range(4):
            n,v=ph.get((it,m),[0,0]);row.append(f"{m}:{n}u@${v/n if n else 0:.0f}")
        print(f'  {it:11s}',"  ".join(row))
