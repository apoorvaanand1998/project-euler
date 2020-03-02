from math import factorial

def digit_fact_sum(n):
    dfs = 0
    while (n > 0):
        fd = factorial(n % 10)
        n //= 10
        dfs += fd
    return dfs

def build_dicts(len_dict, fact_chain_dict, count):
    for i in range(1, 10**6+1):
        curr = i
        chain = set()
        while (curr not in chain):
            chain.add(curr)
            try:
                curr = fact_chain_dict[curr]
            except KeyError:
                dfs = digit_fact_sum(curr)
                fact_chain_dict[curr] = dfs
                curr = dfs
        lc = len(chain)
        len_dict[i] = lc
        if lc == 60:
            count += 1
    return count

result = build_dicts(dict(), dict(), 0)

print(result)
