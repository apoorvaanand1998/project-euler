from itertools import permutations

def prop(n):
    primes = (2, 3, 5, 7, 11, 13, 17)
    for i in range(7, 0, -1):
        sub = int(''.join(map(str, n[i:i+3])))
        prime = primes[i-1]
        if sub % prime != 0:
            return False
    return True

perm = list(permutations(range(10)))
sum_p = 0

for e in perm:
    if prop(e):
        sum_p += int(''.join(map(str, e)))
print(sum_p)
