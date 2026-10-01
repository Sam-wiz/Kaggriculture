import importlib.util,collections
from kaggle_environments import make
SHOP_ITEMS={'BAKERY':('WHEAT','CARROT','EGG'),'PIZZA_SHOP':('WHEAT','CARROT','TOMATO','MILK'),
 'FARMERS_MARKET':('CARROT','TOMATO','STRAWBERRY','MELON'),'ICE_CREAM_SHOP':('MILK','STRAWBERRY','EGG'),
 'SMOOTHIE_SHOP':('STRAWBERRY','MELON','MILK'),'YARN_STORE':('WOOL',),'PET_CAFE':('CARROT','EGG','MILK'),
 'BBQ':('TOMATO','MELON','WOOL')}
def loadm(p):
    spec=importlib.util.spec_from_file_location('m'+str(abs(hash(p))%99999),p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
us=loadm('subV_sirxP.py').agent
dem=collections.defaultdict(lambda:collections.defaultdict(list))
nod=collections.defaultdict(lambda:collections.defaultdict(list))
env=make('kaggriculture',configuration={'episodeSteps':720,'seed':960},debug=False)
# observe prices each step: wrap env.step
orig=env.step
def rec(actions,logs=None):
    r=orig(actions,logs)
    o=env.steps[-1][0]['observation']
    s=o['step']
    if s>=576:
        active=set()
        for sh in o['town']['unlocked_shops']:
            for it in SHOP_ITEMS.get(sh,()):active.add(it)
        for it,pr in o['market']['prices'].items():
            (dem if it in active else nod)[it][s%4].append(pr)
    return r
env.step=rec
env.run([us,us])
for it in ('STRAWBERRY','MELON','WOOL','MILK','EGG','CARROT'):
    d1=dem[it].get(1);d0=dem[it].get(0)
    n1=nod[it].get(1);n0=nod[it].get(0)
    f=lambda v:f"{sum(v)/len(v):.0f}(n{len(v)})" if v else "-"
    print(f"{it:11s} demanded ph0={f(d0)} ph1={f(d1)} | not-demanded ph0={f(n0)} ph1={f(n1)}")
