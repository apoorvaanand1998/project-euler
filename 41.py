from itertools import permutations

def is_prime(n):
    n = int(''.join(map(str, n)))
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    for i in range(5, int(n**0.5)+2, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
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


    
    
