import math

def ncr(n, r):
    return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))

counter = 0
for i in range(1, 101):
    for j in range(1, i):
        if ncr(i, j) > 1000000:
            counter += 1
print(counter)
