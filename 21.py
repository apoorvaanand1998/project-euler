import math
from itertools import combinations

def prod(l):
    prod = 1
    for e in l:
        prod *= e
    return prod

def pf(n):
    l = []
    while n % 2 == 0:
        n //= 2
        l.append(2)
    for i in range(3, math.ceil(math.sqrt(n))):
        while n % i == 0:
            n //= i
            l.append(i)
    if n > 1:
        l.append(n)
    return l

def pd(n):
    lpf = pf(n)
    pd = set(lpf)
    for i in range(2, len(lpf)):
        for e in list(combinations(lpf, i)):
            pd.add(prod(e))
    pd.add(1)
    try:
        pd.remove(n)
    except:
        pass
    return pd

sum_amicable = 0
for i in range(2, 10000):
    a = sum(pd(i))
    b = sum(pd(a))
    if i == b and a != b:
        sum_amicable += i

print(sum_amicable)


