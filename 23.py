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
    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
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

abundant_numbers = set()  ## using a set here because 'in' is O(1)

for i in range(12, 28124):
    if sum(pd(i)) > i:
        abundant_numbers.add(i)

tot = 0
for i in range(1, 28124):
    if i in abundant_numbers and i/2 in abundant_numbers:
        continue
    for e in abundant_numbers:
        if e > i:
            tot += i
            break
        other = i - e 
        if other in abundant_numbers:
            break
print(tot)
