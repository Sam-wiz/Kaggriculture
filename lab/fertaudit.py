import importlib.util,collections,sys
import kaggle_environments.envs.kaggriculture.kaggriculture as ENG
from kaggle_environments import make
def loadm(p):
    spec=importlib.util.spec_from_file_location('m'+str(abs(hash(p))%99999),p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
FILLS=[]
_oc=ENG._commit_unit;_opm=ENG._process_market;_sb=[None]
def _pm(state,env):_sb[0]=state;return _opm(state,env)
def _c(op,item,price,farm,private,market,shed_capacity=100):
    ok=_oc(op,item,price,farm,private,market,shed_capacity)
    if ok:
        pl=0
        try:pl=0 if _sb[0][0].observation.farms[0] is farm else 1
        except Exception:pass
        FILLS.append((_sb[0][0].observation.step,pl,op,item,price))
    return ok
ENG._commit_unit=_c;ENG._process_market=_pm
# also count FERTILIZE ops + end shed/carry fert
env=make('kaggriculture',configuration={'episodeSteps':720,'seed':int(sys.argv[1])},debug=False)
env.run([loadm('subV_sirxP.py').agent,loadm('subV_sirxP.py').agent])
bought=collections.Counter();spent=collections.Counter();sold=collections.Counter();earned=collections.Counter()
for step,pl,op,item,price in FILLS:
    if item=='FERTILIZER':
        if op=='BUY_PRODUCT':bought[pl]+=1;spent[pl]+=price
        elif op=='SELL':sold[pl]+=1;earned[pl]+=price
fz=collections.Counter()
for s in env.steps:
    a=s[0].get('action') or {}
    for u in [a.get('farmer')]+list(a.get('hands') or []):
        if u and u[0]=='FERTILIZE':fz[0]+=1
print('FERT bought:',bought[0],'spent $',spent[0],'| sold:',sold[0],'earned $',earned[0],'| FERTILIZE ops emitted:',fz[0])
# end-state fert stock
obs=env.steps[-1][0]['observation']
print('end shed FERT:',obs['private']['shed'].get('FERTILIZER',0),'carried:',sum(i.get('FERTILIZER',0) for i in obs['private']['inventories']))
