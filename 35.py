def is_prime(n):
    if n==2:
        return True
    if n%2 == 0 or n == 1:
        return False
    for i in range(3, int(n**0.5)+2, 2):
        if n%i == 0:
            return False
    return True

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
        if not is_prime(rot):
            return False
    return True

count = 0
for i in range(1000000):
    if all_rots_prime(i):
        count += 1
print(count)

