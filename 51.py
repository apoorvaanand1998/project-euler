def i2l(i):
    return list(map(int, list(str(i))))

def l2i(l):
    return int(''.join(map(str, l)))

def one_change(n, pos):
    n = i2l(n)
    family = []

    for i in range(10):
        n[pos] = i
        family.append(l2i(n))
    return family

l = [True] * 1000000
l[0] = l[1] = False

for i in range(2, int(1000000**0.5)+2):
    if l[i]:
        for j in range(i*i, 1000000, i):
            l[j] = False

pl = []
for i in range(1000000):
    if l[i]:
       pl.append(i)

found = 0
for number in pl:
    for pos in range(len(str(number))):
        family = one_change(number, pos)
        not_prime_c = 0
        for n in family:
            if not l[n]:
                not_prime_c += 1
            if not_prime_c >= 3:
                break
        if not_prime_c <= 2:
            found = 1
            break
    if found:
        print(number, pos, family)
        break
        
    
                

