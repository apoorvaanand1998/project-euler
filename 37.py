def sieve(n):
    l = [True] * n
    l[0] = l[1] = False
    for i in range(2, int(n**0.5)+2):
        if l[i]:
            for j in range(i*i, n, i):
                l[j] = False
    return l

l = sieve(1000000)

tp = []

for i in range(10, 1000000):
    if not l[i]:
        continue
    if len(tp) == 11:
        break
    lr = len(str(i))
    flag = 0
    for j in range(1, lr):
        if not l[i % (10**j)]:
           flag = 1
           break
    if flag:
        continue
    n = i
    while (n > 0):
        if not l[n]:
            flag = 1
            break
        n //= 10
    if flag:
        continue
    tp.append(i)
print(tp, sum(tp))
    
