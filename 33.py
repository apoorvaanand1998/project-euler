def common_digit(a, b):
    a = set(str(a))
    b = set(str(b))

    i = a.intersection(b)

    if len(i) == 1 and '0' not in i:
        for x in i:
            return int(x)
    return None

def remove_digit(n, r):
    if r == None:
        return None
    n = list(str(n))
    n.remove(str(r))

    return int(''.join(n))

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)

num_prod = denom_prod = 1
for i in range(10, 100):
    for j in range(i+1, 100):
        c = common_digit(i, j)
        try:
            if remove_digit(i, c)/remove_digit(j, c) == i/j:
                print(i, "/", j)
                num_prod *= i
                denom_prod *= j
        except:
            pass

print(denom_prod//gcd(num_prod, denom_prod))

