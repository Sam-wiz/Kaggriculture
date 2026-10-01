import importlib.util
from kaggle_environments import make
def loadm(p):
    spec=importlib.util.spec_from_file_location('m'+str(abs(hash(p))%9999),p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
for f in ('subV_sirxP.py','subV2_sirxP.py'):
    env=make('kaggriculture',configuration={'episodeSteps':720,'seed':731},debug=False)
    env.run([loadm(f).agent,loadm(f).agent])
    print(f,[s.status for s in env.steps[-1]],[s.reward for s in env.steps[-1]])
