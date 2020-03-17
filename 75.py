## PROBLEM 9 OVERVIEW NEEDS TO BE UNDERSTOOD
## https://mathworld.wolfram.com/PythagoreanTriple.html

import math
from collections import defaultdict

def euclid_pyth(L):
    result = []
    m_limit = math.ceil((L/2)**0.5)
    '''
    Why is that m_limit?
    a = (m**2 - n**2)
    b = 2*m*n
    c = (m**2 + n**2)
    s = a + b + c 
    
    a + c < s
    therefore, 2*m**2 < s
    '''
    for m in range(1, m_limit):
        for n in range(1, m):
            if ((m + n) % 2 == 1) and math.gcd(m, n) == 1:
                a = m**2 - n**2
                b = 2*m*n
                c = m**2 + n**2
                if (a+b+c) > L:
                    break
                result.append([a, b, c])
    return result

def mk_non_prim(prim, max_L):
    non_prim = set()
    for e in prim:
        d = 1
        poss_np = [d*x for x in e]
        while (sum(poss_np) <= max_L):
            non_prim.add(tuple(sorted(poss_np)))
            d += 1
            poss_np = [d*x for x in e]
    return non_prim

prim = euclid_pyth(1500000)
non_prim = mk_non_prim(prim, 1500000)

d = defaultdict(int)
for e in non_prim:
    d[sum(e)] += 1

count = 0
for e in d:
    if d[e] == 1:
        count += 1
print(count)
    
