def primes(n):
    pl = [True] * n
    pl[0] = pl[1] = False

    for i in range(int(n**0.5)+2):
        if pl[i]:
            for j in range(i*i, n, i):
                pl[j] = False

    prime_set = set()
    for i in range(n):
        if pl[i]:
            prime_set.add(i)
    return prime_set

def phi(n):
    result = n
    i = 2
    while (i*i <= n):
        if (n % i == 0):
            while (n % i == 0):
                n /= i
            result -= result // i
        i += 1
    if n > 1:
        result -= result // n
    return result

p = primes(10**6)
d = 10**6 + 1
ans = 0

for i in range(2, d):
    if i in p:
        ans += (i-1)
    else:
        ans += phi(i)
print(int(ans))
