################################################################################################################################
# https://medium.com/@aiswaryamathur/find-the-n-th-permutation-of-an-ordered-string-using-factorial-number-system-9c81e34ab0c8 #
################################################################################################################################

def factoradic(n):
    l = []
    i = 1
    while n > 0:
        l.append(n%i)
        n //= i
        i += 1
    return l[::-1]

def nth_perm(n, l):
    res = []
    n = factoradic(n)
    while len(n) < len(l):
        n.insert(0, 0)
    for e in n:
        res.append(l.pop(e))
    return res

print(list(map(lambda x: x-1, nth_perm(999999, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))))

 
