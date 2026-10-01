import gzip,json,collections,sys
import kaggle_environments.envs.kaggriculture.kaggriculture as ENG
from kaggle_environments import make
path=sys.argv[1]
d=json.load(gzip.open(path))
acts=d['actions'];seed=d['seed']
LED=collections.defaultdict(float);UNITS=collections.Counter()
_sb=[None]
_oc=ENG._commit_unit;_opm=ENG._process_market
def _pm(state,env):_sb[0]=state;return _opm(state,env)
def _c(op,item,price,farm,private,market,shed_capacity=100):
    ok=_oc(op,item,price,farm,private,market,shed_capacity)
    if ok:
        st=_sb[0][0].observation
        pl=0 if st.farms[0] is farm else 1
        LED[(pl,f'{op}:{item}')]+=price*(1 if op=='SELL' else -1)
        UNITS[(pl,op,item)]+=1
    return ok
ENG._commit_unit=_c;ENG._process_market=_pm
env=make('kaggriculture',configuration={'episodeSteps':720,'seed':seed},debug=False)
def mk(seat):
    def ag(obs):
        t=obs['step']+1
        return acts[t][seat] if t<len(acts) else {'farmer':['PASS'],'hands':[],'market':[]}
    return ag
env.run([mk(0),mk(1)])
r=[s.reward for s in env.steps[-1]]
print('rewards replayed:',r,'recorded:',d['rewards'],'MATCH' if r==d['rewards'] else 'DIVERGED')
for pl in (0,1):
    tot={'in':0,'out':0}
    print(f'--- seat {pl} ({d["teams"][pl]}) ---')
    for k in sorted(LED):
        if k[0]!=pl:continue
        op=k[1].split(':')[0]
        u=UNITS.get((pl,op,k[1].split(':')[1]),0)
        v=LED[k];tot['in' if v>0 else 'out']+=abs(v)
        print(f'  {k[1]:28s} {u:5d}u  ${v:>10.0f}')
    print(f'  flows: in=${tot["in"]:.0f} out=${tot["out"]:.0f} net=${tot["in"]-tot["out"]:.0f}')
