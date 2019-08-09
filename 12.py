######################################################################################
# What is the value of the first triangle number to have over five hundred divisors? #
######################################################################################

import math

ltn = []

for i in range(12000, 15000):
    ltn.append(i*(i + 1) / 2)

def lpf_modified(n):
    l = {}
    while n % 2 == 0:
        if 2 in l:
            l[2] += 1
        else:
            l[2] = 1
        n //= 2
    for i in range(3, math.ceil(math.sqrt(n)) + 2, 2):
        while n % i == 0:
            if i in l:
                l[i] += 1
            else:
                l[i] = 1
            n //= i
    if n > 1:
        l[n] = 1
    return l

def nod(lpf_d):
    nod = 1
    for key in lpf_d:
        nod *= lpf_d[key] + 1
    return nod

for e in ltn:
    n = nod(lpf_modified(e))
    if n > 500:
        print(e)

################################################################
# https://mathschallenge.net/library/number/number_of_divisors #
################################################################
