## YET AGAIN THE SAME PRINCIPLE AS COIN CHANGE
## HERE THE "DENOMINATIONS" ARE ALL NUMBERS BETWEEN 1 AND "AMOUNT" (INCLUSIVE)
## USING ONLY THE DP SOLUTION DOES NOT WORK
## USING THE RECURRENCE RELATION FOUND IN PARTITION FUNCTION'S WIKI
## (DON'T REALLY NEED DP SOLUTION BELOW BUT KEEPING IT IN)

memoize = {
    0 : 1,
    1 : 1,
    2 : 2
}
pent_mem_pos = [0]
pent_mem_neg = [0]

dp_table = [[1, 1, 1], [1, 1, 2]]
amount = 2

while (True):
    memoize[amount] = dp_table[-1][-1] % 1000000
    if amount >= 100:
        break
    dp_table[0].append(1)

    for i in range(1, amount):
        el = dp_table[i-1][-1] + dp_table[i][amount - i]
        dp_table[i].append(el)

    l_to_add = dp_table[-1][:-1] + [dp_table[-1][-1] +
                                    dp_table[-1][0]]
    dp_table.append(l_to_add)
    amount += 1

def sign(k):
    return 1 if (k % 2 == 1) else -1
def pentagonal_term(k):
    try:
        if k >= 1:
            return pent_mem_pos[k]
        elif k <= -1:
            return pent_mem_neg[abs(k)]
    except IndexError:
        pt = k*(3*k-1)//2
        if k <= -1:
            pent_mem_neg.append(pt)
        else:
            pent_mem_pos.append(pt)
        return pt

def p(n):
    if n < 0:
        return 0
    if n == 1:
        return 1
    try:
        return memoize[n]
    except KeyError:
        l = []
        i = 1

        while True:
            l.append(sign(i) * p(n - pentagonal_term(i)))
            l.append(sign(-i) * p(n - pentagonal_term(-i)))
            if l[-1] == 0:
                break
            i += 1
        result = sum(l) % 1000000
        memoize[n] = result
        return result

n = 101
while True:
    partitions = p(n)
    if partitions % 1000000 == 0:
        print(n)
        break
    n += 1
