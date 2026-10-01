import sys, json
sys.argv=[sys.argv[0]]
exec(open('/tmp/opus_r3/libopen.py').read().split('if __name__')[0])
sys.path.insert(0,'/tmp/opus_r3/x_hakdevelopment_kaggriculture-2887-score-fieldcraft-agent')
for n,p in [('fieldcraft','/tmp/opus_r3/x_hakdevelopment_kaggriculture-2887-score-fieldcraft-agent/main.py'),('guru_v4','/tmp/opus_r3/x_guruprasaathas111_kaggriculture-top-2-master-engine-v4/main.py')]:
    print(n, work((n,p))[2][:170])
