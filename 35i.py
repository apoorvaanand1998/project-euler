def sieve(n):
    l = n * [True]
    l[0] = False
    l[1] = False

    for i in range(2, int(n**0.5)+2):
        if l[i] == True:
            for j in range(i*i, n, i):
                l[j] = False
    return l

l = sieve(1000000)

def dec_rs(n):
    n = n[-1:] + n[0:-1]
    return n

def all_rot(n):
    n = list(str(n))
    l = [n]
    c = dec_rs(n)
    while (c != n):
        l.append(c)
        c = dec_rs(c)
    return l

def all_rots_prime(n):
    for rot in all_rot(n):
        rot = int(''.join(rot))
        if not l[rot]:
            return False
    return True

count = 0
for i in range(1000000):
    if all_rots_prime(i):
        count += 1
print(count)
