from itertools import permutations

def is_tri(y):
    n = (-1 + (1 + 8 * y)**0.5) / 2
    return n == int(n)

def is_sq(y):
    return y**0.5 == int(y**0.5)

def is_pen(y):
    n = (1 + (24 * y + 1)**0.5) / 6
    return n == int(n)

def is_hex(y):
    n = (1 + (1 + 8 * y)**0.5) / 4
    return n == int(n)

def is_hep(y):
    n = (3 + (9 + 40 * y)**0.5) / 10
    return n == int(n)

def is_oct(y):
    n = (2 + (4 + 12 * y)**0.5) / 6
    return n == int(n)

def prop(L):
    for i in L[0]:
        for j in L[1]:
            if str(i)[-2:] != str(j)[:2]:
                continue
            for k in L[2]:
                if str(j)[-2:] != str(k)[:2]:
                    continue
                for l in L[3]:
                    if str(k)[-2:] != str(l)[:2]:
                        continue
                    for m in L[4]:
                        if str(l)[-2:] != str(m)[:2]:
                            continue
                        for n in L[5]:
                            if str(m)[-2:] != str(n)[:2]:
                                continue
                            if str(n)[-2:] == str(i)[:2]:
                                print(i, j, k, l, m, n, i+j+k+l+m+n)
                                return True

def rearrange(l, perm):
    l = [l[perm[0]], l[perm[1]], l[perm[2]], l[perm[3]], l[perm[4]], l[perm[5]]]
    return l

tri_l, sq_l, pen_l, hex_l, hep_l, oct_l = [], [], [], [], [], []

for i in range(1000, 10000):
    if is_tri(i):
        tri_l.append(i)
    if is_sq(i):
        sq_l.append(i)
    if is_pen(i):
        pen_l.append(i)
    if is_hex(i):
        hex_l.append(i)
    if is_hep(i):
        hep_l.append(i)
    if is_oct(i):
        oct_l.append(i)

p = list(permutations([0, 1, 2, 3, 4, 5]))
l = [tri_l, sq_l, pen_l, hex_l, hep_l, oct_l]

for perm in p:
    ltc = rearrange(l, perm)
    if prop(ltc):
        print(perm)
        break


