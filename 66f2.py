## https://en.wikipedia.org/wiki/Chakravala_method
## https://en.wikipedia.org/wiki/Pell%27s_equation
## https://sites.google.com/site/tpiezas/008

def first_sol(D):
    a = int(D**0.5)+1
    return a, 1, (a**2-D)

def find_m_form(a, b, k):
    i = 1
    k = abs(k)
    
    while (((a + b*i) % k) != 0):
        i += 1
    first = i

    i += 1
    while (((a + b*i) % k) != 0):
        i += 1
    second = i

    t = second - first
    return t, first

def find_m(D, a, b, k):
    m_form = find_m_form(a, b, k)

    prev_m = m_form[1]
    next_m = m_form[0] + m_form[1]
    
    abs_prev_m = abs(prev_m*prev_m - D)
    abs_next_m = abs(next_m*next_m - D)
    
    i = 1
    
    while (abs_next_m < abs_prev_m):
        prev_m = m_form[0]*i + m_form[1]
        next_m = m_form[0]*(i+1) + m_form[1]

        abs_prev_m = abs(prev_m*prev_m - D)
        abs_next_m = abs(next_m*next_m - D)
        i += 1
    return prev_m

def m_is_124(D, a, b, k):
    '''Read negative pell equation and transformations on wiki'''
    old_a = a

    if (k == -1):
        a = a*a + D*b*b
        b = 2*old_a*b
    elif (k == 2):
        a = (a*a - 1) 
        b = old_a*b
    elif (k == -2):
        a = (a*a + 1)
        b = old_a*b
    elif (k == 4):
        a = (a*a - 3)*a / 2
        b = (old_a*old_a - 1)*b / 2
    else:
        a = (a**4 + 4*a**2 + 1)*(a**2 + 2) / 2
        b = (b**2 + 3) * (b**2 + 1) * old_a*b / 2
    return (a, b, 1)

def chakravala(D, fs):
    (a, b, k) = fs
    if k == 1:
        return (a, b)
    m = find_m(D, *fs)
    old_a = a
    a = (a*m + D*b)/abs(k)
    b = (old_a + b*m)/abs(k)
    k = (m*m - D)/k
    
    while (k != 1):
        ## print("a, b, k = ", a, b, k)
        bhrama_obs = [-1, 2, -2, -4]
        if (k in bhrama_obs and k != -4):
            (a, b, k) = m_is_124(D, a, b, k)
            return (a, b)
        elif (k == -4):
            if a % 2 == 1 and b % 2 == 1:
                (a, b, k) = m_is_124(D, a, b, k)
                return (a, b)
        
        m = find_m(D, a, b, k)
        old_a = a
        a = int((a*m + D*b)/abs(k))
        b = int((old_a + b*m)/abs(k))
        k = int((m*m - D)/k)
            
    return (a, b)

skip_list = set([x*x for x in range(2, 32)])

max_x = [0, 0]
for i in range(2, 1001):
    if i not in skip_list:
        x = chakravala(i, first_sol(i))[0]
        print("{}\t{}".format(i, int(x)))
        if x > max_x[1]:
            max_x = [i, x]

print(max_x)

##print(chakravala(21, first_sol(21)))
