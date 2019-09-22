l = []
l.append(0)
n = 1
while len(l) < 1000010:
    l += list(map(int, list(str(n))))
    n += 1

print(l[1], l[10], l[100], l[1000], l[10000], l[100000], l[1000000])
    
    
