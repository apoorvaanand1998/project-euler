def lop(n):
    bop = [True] * n
    bop[0] = bop[1] = False
    for i in range(2, (int(n**0.5)+2)):
        for j in range (i*i, n, i):
            bop[j] = False
    lop = set()  ## again using set instead of list is good because "in" is so much more faster yo
    for i in range(n):
        if bop[i] == True:
            lop.add(i)
    return lop

lop = lop(10000)

def max_con_prime(a, b):
    l = 0
    i = 0
    while ((i*i + i*a + b) in lop):
        l += 1
        i += 1
    return l

lmcp = [0, 0, 0]  ## n, i, j
for i in range(-999, 1000):
    for j in range(-1000, 1001):
        mcp = max_con_prime(i, j)
        if mcp > lmcp[0]:
            lmcp = [mcp, i, j]

print(lmcp, lmcp[1]*lmcp[2])
        
        
        
