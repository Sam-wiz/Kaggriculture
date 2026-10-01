import importlib.util,sys
from concurrent.futures import ProcessPoolExecutor
def loadm(p):
    spec=importlib.util.spec_from_file_location('m'+p[-7:-3],p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def job(seed):
    from kaggle_environments import make
    m=loadm('subV_sirxC.py')
    env=make('kaggriculture',configuration={'episodeSteps':720,'seed':seed},debug=False)
    env.run([m.agent,m.agent])
    r=m._CXO_REPORT
    return seed,r['cxo_to_cow'],r['cxo_to_sheep'],r['cxo_declined'],r['cxo_rewrites'],r['cxo_blocked_room']
if __name__=='__main__':
    with ProcessPoolExecutor(6) as ex:
        for seed,c,s,d,rw,b in ex.map(job,range(1100,1124)):
            fire=c+s
            print(f'seed {seed}: swaps={fire} (to_cow={c} to_sheep={s}) declined={d} rewrites={rw} blocked={b}')
