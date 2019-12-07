## https://en.wikipedia.org/wiki/Chakravala_method

def first_sol(D):
    a = int(D**0.5)+1
    return a, 1, (a**2-D)

def find_m(D, a, b, k):
    m = m1 = m2 = int(D**0.5)
    #print(m)
    while (((a+(b*m1)) % k) != 0):
        m1 += 1
    while (((a+(b*m2)) % k) != 0):
        m2 -= 1
    if abs(m1*m1-D) > abs(m2*m2-D):
        return m2
    return m1

def chakravala(D, fs):
    (a, b, k) = fs
    m = find_m(D, *fs)
    old_a = a
    a = (a*m + D*b)/abs(k)
    b = (old_a + b*m)/abs(k)
    k = (m*m - D)/k
    
    while (k != 1):
        m = find_m(D, a, b, k)
        old_a = a
        a = int((a*m + D*b)/abs(k))
        b = int((old_a + b*m)/abs(k))
        k = int((m*m - D)/k)
            
    return (a, b)

skip_list = set([x*x for x in range(2, 32)])

max_x = [0, 0]
for i in range(2, 1001):
    print(i)
    if i not in skip_list:
        x = chakravala(i, first_sol(i))[0]
        if x > max_x[1]:
            max_x = [i, x]

print(max_x)
