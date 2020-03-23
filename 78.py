## YET AGAIN THE SAME PRINCIPLE AS COIN CHANGE
## HERE THE "DENOMINATIONS" ARE ALL NUMBERS BETWEEN 1 AND "AMOUNT" (INCLUSIVE)
## USING ONLY THE DP SOLUTION DOES NOT WORK
## USING THE RECURRENCE RELATION FOUND IN PARTITION FUNCTION'S WIKI

memoize = {
    0 : 1,
    1 : 1,
    2 : 2
}
dp_table = [[1, 1, 1], [1, 1, 2]]
amount = 2

while (True):
    memoize[amount] = dp_table[-1][-1]
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
    return int((-1)**(k+1))
def pentagonal_term(k):
    return k*(3*k-1)//2

def p(n):
    if n < 0:
        return 0
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
        result = sum(l)
        memoize[n] = result
        return result

n = 101
while True:
    partitions = p(n)
    if partitions % 1000000 == 0:
        print(n, partitions)
        break
    n += 1
