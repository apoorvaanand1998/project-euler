## Using the direct sieve approach described in the problem overview

d = 10**6

phi = []
for i in range(d+1):
   phi.append(i)

for i in range(2, d+1):
    if phi[i] == i:
        for j in range(i, d+1, i):
            phi[j] -= phi[j] / i

result = 0            
for i in range(2, d+1):
    result += phi[i]
print(result)
