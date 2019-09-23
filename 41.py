from itertools import permutations

def is_prime(n):
    n = int(''.join(map(str, n)))
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)+1
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f += 6
    return True    

perm = permutations(range(1, 8))
li = list(perm)
l = len(li)

for i in range(1, l+1):
    if is_prime(li[-i]):
        print(li[-i])
        break

## range(1, 10) or range(1, 9) not used because 1+2+..+8 = 36 and 1+..+9 = 45
## Both are divisible by 3


    
    
