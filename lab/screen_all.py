import sys,os,json; sys.path.insert(0,'kaggriculture-island-ga'); sys.path.insert(0,'.')
import inco, kagsim
from multiprocessing import Pool
PIPE='/Users/samrudh/Documents/Projects/kaggle/Kaggriculture/subI_pipe7.py'
ROOT='/Users/samrudh/Documents/Projects/kaggle/Kaggriculture'
def run(c):
    sys.path.insert(0,ROOT+'/kaggriculture-island-ga'); sys.path.insert(0,ROOT)
    import inco, kagsim
    try: ag=inco.load_agent(f'{ROOT}/rivals/{c}/main.py')
    except Exception as e: return (c,'LOAD_FAIL',0,0)
    try: pipe=inco.load_agent(PIPE)
    except Exception as e: return (c,'PIPE_FAIL',0,0)
    w=0;mg=0;n=0
    for s in (7001,7002,7003):
        try:
            g=kagsim.Game(seed=s)
            for t in range(720):
                g.step(ag(g.observe(0)), pipe(g.observe(1)))
            mg+=g.reward(0)-g.reward(1); n+=1; w+=g.reward(0)>g.reward(1)
        except Exception: break
    return (c, round(mg/max(n,1)), w, n)
if __name__=='__main__':
    cands=[d for d in os.listdir(ROOT+'/rivals') if os.path.exists(f'{ROOT}/rivals/{d}/main.py')]
    out=open(ROOT+'/screen_all.jsonl','w')
    with Pool(6) as p:
        for r in p.imap_unordered(run,cands):
            out.write(json.dumps(r)+'\n'); out.flush(); print(r,flush=True)
