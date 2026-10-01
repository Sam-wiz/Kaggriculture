import sys, json
sys.argv=[sys.argv[0]]
exec(open('/tmp/opus_r3/libopen.py').read().split('if __name__')[0])
for n,p in [('hs2700','/tmp/opus_r3/gz_herd-safe-sale-w/main.py'),('rescue','/tmp/opus_r3/gz_7-turn-rescue-hi/main.py'),('twocoins','/tmp/opus_r3/gz_two-coins-one-sh/main.py')]:
    print(n, work((n,p))[2][:160])
