import sys; sys.path.insert(0,'.')
import inco, kagsim
from multiprocessing import Pool
from collections import defaultdict
ROOT='/Users/samrudh/Documents/Projects/kaggle/Kaggriculture'
def game(args):
    a_path,b_path,seed,swapped=args
    sys.path.insert(0,ROOT)
    import inco, kagsim
    ag=inco.load_agent(ROOT+'/'+a_path); op=inco.load_agent(ROOT+'/'+b_path)
    g=kagsim.Game(seed=seed)
    for t in range(720):
        o0,o1=g.observe(0),g.observe(1)
        if swapped: g.step(op(o1),ag(o0))
        else: g.step(ag(o0),op(o1))
    return (a_path,b_path,seed,swapped,g.reward(1) if swapped else g.reward(0),
            g.reward(0) if swapped else g.reward(1))
if __name__=='__main__':
    A='rivals/jaxa623_2802/main.py'
    pool=['rivals/boatlee_v29-r1-adaptive-market-hysteresis/main.py',
          'rivals/romanrozen_strong-barnyard-economist/main.py',
          'rivals/the-2945-farm-96-vs-the-top-10-public-bots/main.py',
          'rivals/skomuro_2000-baseline-silver-medal-route/main.py',
          'rivals/salemali7_kaggriculture-2900/main.py']
    tasks=[]
    for opp in pool:
        for s in range(8500,8504):
            tasks.append((A,opp,s,False)); tasks.append((A,opp,s,True))
    agg=defaultdict(lambda:[0,0,0])
    with Pool(6) as p:
        for r in p.imap_unordered(game,tasks):
            a,b,s,sw,ra,rb=r
            agg[b][0]+=ra-rb; agg[b][1]+=ra>rb; agg[b][2]+=1
            print(f'{b.split("/")[1][:40]:42s} seed{s} {"s1" if sw else "s0"}: {ra-rb:+7.0f}',flush=True)
    for k,(mg,w,n) in agg.items():
        print(f'== 2802 vs {k.split("/")[1][:50]}: W{w}-L{n-w} {mg/n:+.0f}')
