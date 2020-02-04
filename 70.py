'''
First, we know that for minimum possible 
n / phi(n), n has to be a prime number.

This is because phi(n) when n is a prime
is n - 1. Now, we also know that there is
no number p such that p and p - 1 are 
permutations of each other.

To find the next best candidate for least
n / phi(n), we need to look through all 2
combinations of primes. Why 2? Because by
increasing the number of primes (with 3 
combinations, 4 combinations and so on),
the n / phi(n) quotient actually increases.
'''
from itertools import combinations

def prod(l):
    p = 1
    for e in l:
        p *= e
    return p

def is_perm(n, t):
    return sorted(list(str(n))) == sorted(list(str(t)))

def list_of_primes(n):
    l = [True] * n
    l[0] = l[1] = False

    for i in range(int(n**0.5)+2):
        if l[i]:
            for j in range(i*i, n, i):
                l[j] = False
                
    pl = []
    for i in range(n):
        if l[i]:
            pl.append(i)
            
    return pl

l = list_of_primes(10**7)

min_nbe = [10, 10]  ## just some starting val
for i in range(len(l)):
    if l[i] > 2 * (10**7)**0.5:
        break
    for j in range(i+1, len(l)):
        x = l[i] * l[j]
        y = (l[i] - 1) * (l[j] - 1)
        if x > 10**7:
            break
        else:
            if is_perm(x, y):
                if (x / y) < min_nbe[1]:
                    min_nbe = [x, x/y]
print(min_nbe)
