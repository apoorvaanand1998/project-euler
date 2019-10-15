from itertools import permutations

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i < n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

def i2l(i):
    return list(map(int, list(str(i))))

def l2i(l):
    return int(''.join(map(str, l)))

counter = 0
for i in range(1000, 10000):
    if not is_prime(i):
        continue
    c = [i]
    for e in permutations(i2l(i)):
        if is_prime(l2i(e)) and e[0] != 0 and l2i(e) == c[-1]+3330:
            c.append(l2i(e))
    if len(c) == 3:
        print(l2i(c))
        counter += 1
    if counter == 2:
        break

