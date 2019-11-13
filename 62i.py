def cube(x):
    return x*x*x

def numbsort(n):
    n = list(str(n))
    n.sort()
    return tuple(n)

d = {}
l = []
for i in range(10000):
    c = cube(i)
    nsc = numbsort(c)
    l.append(c)
    try:
        d[nsc] += 1
    except KeyError:
        d[nsc] = 1

for e in l:
    if d[numbsort(e)] == 5:
        print(e)
        break
