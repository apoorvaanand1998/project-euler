def euler_totient(n):
    result = n
    for i in range(2, int(n**0.5+2)):
        if (n % i == 0):
            while (n % i == 0):
                n //= i
            result -= result // i 
    if (n > 1):
        result -= result // n
    return result
'''
## takes ~30 seconds

max_nbe = 0, 0
for i in range(10, 1000001):
    et = euler_totient(i)
    nbe = i / et
    if nbe > max_nbe[1]:
        max_nbe = i, nbe
print(max_nbe)
'''
print(euler_totient(510510))
