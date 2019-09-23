n = 0
i = [-1]
while True:
    l = list(map(int, list(str(n))))
    i = [i[-1]+1]
    while (len(i) < len(l)):
        t = i[-1]+1
        i.append(t)
    if (1 in i):
        print(l[i.index(1)])
    elif (10 in i):
        print(l[i.index(10)])
    elif (100 in i):
        print(l[i.index(100)])
    elif (1000 in i):
        print(l[i.index(1000)])
    elif (10000 in i):
        print(l[i.index(10000)])
    elif (100000 in i):
        print(l[i.index(100000)])
    elif (1000000 in i):
        print(l[i.index(1000000)])
        break
    n += 1

