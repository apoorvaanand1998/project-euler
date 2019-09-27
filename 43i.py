from itertools import permutations

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
primes = [17, 13, 11, 7, 5, 3, 2]

def l2i(l):
    return int(''.join(map(str, l)))

perm = list(permutations(digits, 3))

mod_dict = {
    2: [], 3: [], 5: [], 7: [], 11: [], 13: [], 17: []
}

for e in perm:
    n = l2i(e)
    for prime in primes:
        if n % prime == 0:
            mod_dict[prime].append(list(e))

poss = mod_dict[17]
for i in range(1, 7):
    temp = []
    for n in poss:
        for p in mod_dict[primes[i]]:
            if n[:2] == p[-2:] and p[0] not in n:
                temp.append([p[0]] + n)
    poss = temp

sum_p = 0
for e in poss:
    element = set(digits) - set(e)
    n = l2i(list(element) + e)
    print(n)
    sum_p += n
print(sum_p)

    
