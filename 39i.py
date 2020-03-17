## https://projecteuler.net/overview=009
## VERY IMPORTANT THAT YOU UNDERSTAND THIS ABOVE TO SOLVE THIS AND PROBLEM 75

import math

def gcd(a, b):
    if (b == 0):
        return a
    return gcd (b, a % b)
    
def euclid_pyth(s):
    result = []
    s2 = s / 2
    mlimit = math.ceil(s**0.5) - 1
    for m in range(2, mlimit+1):
        if s2 % m == 0:
            sm = s2 / m
            while sm % 2 == 0:
                sm = sm / 2
            if m % 2 == 1:
                k = m + 2
            else:
                k = m + 1
            while k < 2*m and k <= sm:
                if sm % k == 0 and gcd(k, m) == 1:
                    d = s2 / (k*m)
                    n = k-m
                    a = d * (m**2 - n**2)
                    b = 2 * d * m * n
                    c = d * (m**2 + n**2)
                    result.append([m, n, a, b, c, a+b+c])
                k += 2
    return result

max_sol = [-1, -1]
for p in range(12, 1001):
    no_of_sol = len(euclid_pyth(p))
    if no_of_sol > max_sol[1]:
        max_sol = [p, no_of_sol]
print(max_sol)         
    
            
