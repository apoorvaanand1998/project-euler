def sieve(n):
    l = n * [True]
    l[0] = False
    l[1] = False

    for i in range(2, int(n**0.5)+2):
        if l[i] == True:
            for j in range(i*i, n, i):
                l[j] = False
    return l

l = sieve(1000000)

count = 0
for i in range(1000000):
    if not l[i]:
        continue
    n = i
    t = len(str(i))-1
    flag = 1
    for j in range(t):
        n = (n%10)*10**t + (n//10)
        if not l[n]:
            flag = 0
            break
    if flag == 1:
        count += 1
        
print(count)
