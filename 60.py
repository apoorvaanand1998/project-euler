n = 10000  ## this takes around 3 minutes!!!! without precalculation of primes below

PRIME = [True] * 100000000
PRIME[0] = PRIME[1] = False

for i in range(int(100000000**0.5)+2):
    if PRIME[i]:
        for j in range(i*i, 100000000, i):
            PRIME[j] = False
            
def is_prime_l(l, n):
    def front(e, n):
        return int(str(n)+str(e))
    def back(e, n):
        return int(str(e)+str(n))
    
    if n in l:
        return False
    for e in l:
        if (not is_prime(front(e, n)) or
            not is_prime(back(e, n))):
            return False
    return True

def prime_prop(primes, l, n):
    nl = []
    sum_seen = set()
    while (len(l[0]) < n):
        for e in l:
            for prime in primes:
                if is_prime_l(e, prime):
                    ne = e + [prime]
                    if sum(ne) not in sum_seen:
                        sum_seen.add(sum(ne))
                        nl.append(ne)
        l = nl
        print(l)
        nl = []
    return l

def is_prime(n):
    return PRIME[n]

primes = []
primes_l = []
for i in range(n):
    if PRIME[i]:
        primes.append(i)
        primes_l.append([i])

res = prime_prop(primes, primes_l, 5)
    

