def pf(n):
    pfd = {}
    while n % 2 == 0:
        try:
            pfd[2] += 1
        except KeyError:
            pfd[2] = 1
        n //= 2
        
    for i in range(3, int(n**0.5)+2, 2):
        while n % i == 0:
            try:
                pfd[i] += 1
            except KeyError:
                pfd[i] = 1
            n //= i
            
    if n != 1:
        pfd[n] = 1
    return pfd

def d2s(d):
    s = set()
    for key in d:
        s.add(key**d[key])
    return s

i = 644
while True:
    ## sorry for hacky continues, but really speeds things up
    a = pf(i)
    if len(a) != 4:
        i += 1
        continue
    b = pf(i+1)
    if len(b) != 4:
        i += 1
        continue
    c = pf(i+2)
    if len(c) != 4:
        i += 1
        continue
    d = pf(i+3)
    if len(d) != 4:
        i += 1
        continue

    a = d2s(a)
    b = d2s(b)
    c = d2s(c)
    d = d2s(d)
    if a.intersection(b, c, d) == set():
            print(i)
            print(a, b, c, d)
            break
    i += 1
    
