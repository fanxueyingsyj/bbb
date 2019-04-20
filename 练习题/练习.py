import random
x = [random.randint(1,20) for i in range(50)]
r = dict()
for i in x:
    r[i] = r.get(i,0)+1
for k, v in r.items():
    print(k, v)
