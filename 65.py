def e_period_list(n):
    if n == 1:
        return [2]
    else:
        pl = []
        pl.append(2)
        j = 1
        while (len(pl) < n):
            if (len(pl)+1) % 3 == 0:
                pl.append(j*2)
                j += 1
            else:
                pl.append(1)
        return pl

def n_plus_frac(n, numer, denom):
    return (n*denom+numer, denom)

pl = e_period_list(100)
n, d = 1, pl[99]

for i in range(98, -1, -1):
    d, n = n_plus_frac(pl[i], n, d)

sod = 0
while (d > 0):
    sod += d % 10
    d //= 10
print(sod)
