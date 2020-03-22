## SAME PRINCIPLE AS DP SOLUTION OF COIN CHANGE PROBLEM
## DRAW THE DP TABLE WITH "DENOMINATIONS" OF PRIMES <= CURRENT "AMOUNT"

def primes(n):
    p = [True] * (n+1)
    p[0] = p[1] = False

    for i in range(2, int(n**0.5)+2):
        if p[i]:
            for j in range(i*i, n+1, i):
                p[j] = False

    pl = []
    for i in range(n+1):
        if p[i]:
            pl.append(i)
    return pl, set(pl)

pl, ps = primes(10**6)
amount = 2
dp_table = [[1, 0]]
curr_prime_index = 1

while (dp_table[-1][-1] < 5000):
    el_for_2 = 1 if (amount % 2 == 0) else 0
    dp_table[0].append(el_for_2)

    prime_index = 1
    for i in range(1, len(dp_table)):
        el = dp_table[i-1][-1] + dp_table[i][amount-pl[prime_index]]
        dp_table[i].append(el)
        prime_index += 1

    if amount == pl[curr_prime_index]:
        l_to_add = []
        for i in range(len(dp_table[-1])-1):
            l_to_add.append(dp_table[-1][i])
        l_to_add.append(dp_table[-1][-1] + l_to_add[0])
        dp_table.append(l_to_add)
        curr_prime_index += 1

    amount += 1
print(amount-1)



