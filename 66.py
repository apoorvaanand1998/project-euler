## https://en.wikipedia.org/wiki/Pell's_equation
## https://projecteuler.net/problem=64
## https://projecteuler.net/problem=65

import math

def nplusfrac(a, rootn, minus, numer):
    reciprocal = numer * (rootn**0.5 + minus) // (rootn - minus*minus)
    nnumer = (rootn - minus*minus) // numer
    nminus = (reciprocal * nnumer) - minus
    return reciprocal, (rootn, nminus, nnumer)
    
def sqrt_period(n):
    res = []
    a0 = math.floor(n**0.5)
    res.append(a0)
    res.append([])

    s = set()
    a, rootn, minus, numer = a0, n, a0, 1

    while (nplusfrac(a, rootn, minus, numer) not in s):
        next_vals = nplusfrac(a, rootn, minus, numer)
        s.add(next_vals)
        res[1].append(next_vals[0])
        a, rootn, minus, numer = next_vals[0], *next_vals[1]
    return res

def improper_frac(a0, l):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a%b)
    
    def n_plus_frac(n, numer, denom):
        nnumer = n * denom + numer
        ndenom = denom
        hcf = gcd(nnumer, ndenom)
        nnumer //= hcf
        ndenom //= hcf
        return (ndenom, nnumer)

    if len(l) == 1:
        return n_plus_frac(a0, 1, l[0])
    else:
        imp_frac = n_plus_frac(l[-2], 1, l[-1])
        for i in range(3, len(l)+1):
            imp_frac = n_plus_frac(l[-i], *imp_frac)
        imp_frac = n_plus_frac(a0, *imp_frac)
    return imp_frac
    
def check_pell(D):
    i = 0
    period = sqrt_period(D)
    period[0], period[1] = int(period[0]), list(map(int, period[1]))
    l = len(period[1])
    big_list = [period[1][i]]
    y, x = improper_frac(period[0], big_list)
    
    while (x*x - D*y*y != 1):
        i += 1
        big_list.append(period[1][i % l])
        y, x = improper_frac(period[0], big_list)
    return x

skip_set = set([x*x for x in range(1, 33)])

max_x = [0, 0]
for D in range(2, 1001):
    if D not in skip_set:
        x = check_pell(D)
        if x > max_x[1]:
            max_x = [D, x]
print(max_x)

    
    
    
