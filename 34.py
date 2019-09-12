from math import factorial

def sfd(n):
    o = n
    res = 0
    while (n > 0):
        res += factorial(n%10)
        n //= 10
    return (o == res)

res = 0
for i in range(10, 7*factorial(9)):
    if sfd(i):
        print(i)
        res += i
print(res)
