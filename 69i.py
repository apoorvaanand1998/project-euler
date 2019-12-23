## https://projecteuler.net/overview=069

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

nbe = 1
for e in primes:
    if nbe*e > 10**6:
        break
    nbe *= e
print(nbe)
