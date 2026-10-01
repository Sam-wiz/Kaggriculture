import importlib.util,collections,sys,json
import kaggle_environments.envs.kaggriculture.kaggriculture as ENG
from kaggle_environments import make
def loadm(p):
    spec=importlib.util.spec_from_file_location('m'+str(abs(hash(p))%99999),p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
FILLS=[]
_orig_commit=ENG._commit_unit
_orig_pm=ENG._process_market
_orig_hire=ENG._do_hire
_orig_land=ENG._do_buy_land
_statebox=[None]
def _hire(farm,private,board_size,mult):
    prev=farm["money"];_orig_hire(farm,private,board_size,mult)
    spent=prev-farm["money"]
    state=_statebox[0]
    pl=0
    try:pl=0 if state[0].observation.farms[0] is farm else 1
    except Exception:pass
    if spent>0:FILLS.append((state[0].observation.step,pl,"HIRE","",spent))
def _land(farm,board_size):
    prev=farm["money"];_orig_land(farm,board_size)
    spent=prev-farm["money"]
    state=_statebox[0]
    pl=0
    try:pl=0 if state[0].observation.farms[0] is farm else 1
    except Exception:pass
    if spent>0:FILLS.append((state[0].observation.step,pl,"BUY_LAND","",spent))
def _pm(state,env):
    _statebox[0]=state
    return _orig_pm(state,env)
def _commit(op,item,price,farm,private,market,shed_capacity=100):
    ok=_orig_commit(op,item,price,farm,private,market,shed_capacity)
    if ok:
        state=_statebox[0]
        pl=0
        try:
            farms=state[0].observation.farms
            pl=0 if farms[0] is farm else 1
        except Exception:pass
        step=state[0].observation.step if state else -1
        FILLS.append((step,pl,op,item,price))
    return ok
ENG._commit_unit=_commit
ENG._process_market=_pm
ENG._do_hire=_hire
ENG._do_buy_land=_land

if __name__=='__main__':
    ap,bp,seed=sys.argv[1],sys.argv[2],int(sys.argv[3])
    env=make('kaggriculture',configuration={'episodeSteps':720,'seed':seed},debug=False)
    env.run([loadm(ap).agent,loadm(bp).agent])
    led={0:collections.defaultdict(float),1:collections.defaultdict(float)}
    for step,pl,op,item,price in FILLS:
        k=op if op in ('HIRE','BUY_LAND') else op+':'+str(item)
        led[pl][k]+=price
    for pl in (0,1):
        tot=sum(led[pl].values())
        print(f'seat{pl} filled $ flow (SELL positive, BUY* negative-spend):')
        for k,v in sorted(led[pl].items()):print(f'   {k:22s} {v:+10.0f}')
        print('   TOTAL                 ',f'{tot:+10.0f}')
    print('rewards',[s.reward for s in env.steps[-1]])
