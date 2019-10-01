def is_comp(n):
    for i in range(3, int(n**0.5)+2, 2):
        if n % i == 0:
            return True
    return False

def twice_square(n):
    i = 1
    ts = 2 * i * i
    tsl = []
    while (ts < n):
        tsl.append(ts)
        i += 1
        ts = 2 * i * i
    return tsl

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True

i = 9
while True:
    if is_comp(i):
        tsl = twice_square(i)
        found = 0
        for ts in tsl:
            if is_prime(i - ts):
                found = 1
                break
        if not found:
            print(i)
            break
    i += 2
        
