import math

def nplusfrac(a, rootn, minus, numer):
    reciprocal = numer * (rootn**0.5 + minus) // (rootn - minus*minus)
    nnumer = (rootn - minus*minus) // numer
    nminus = (reciprocal * nnumer) - minus
    return reciprocal, (rootn, nminus, nnumer)
    
def sqrt_period(n):
    res = []
    a0 = math.floor(n**0.5)
    res.append([a0])
    res.append([])

    s = set()
    a, rootn, minus, numer = a0, n, a0, 1

    while (nplusfrac(a, rootn, minus, numer) not in s):
        next_vals = nplusfrac(a, rootn, minus, numer)
        s.add(next_vals)
        res[1].append(next_vals[0])
        a, rootn, minus, numer = next_vals[0], *next_vals[1]
    return res

not_checked = set()

for i in range(1, 101):
    not_checked.add(i*i)

count = 0
for i in range(1, 10001):
    if i in not_checked:
        continue
    else:
        if len(sqrt_period(i)[1]) % 2 == 1:
            count += 1
print(count)


