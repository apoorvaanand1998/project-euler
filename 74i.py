def digit_fact_sum(n):
    fact = [1, 1, 2, 3*2, 4*3*2, 5*24, 24*5*6, 7*24*30, 56*24*30, 9*56*24*30]
    dfs = 0
    while (n > 0):
        fd = fact[n % 10]
        n //= 10
        dfs += fd
    return dfs

def build_dict(chain_dict):
    for i in range(1, 10**6+1):
        curr = i
        chain = []
        chain_set = set()

        while (curr not in chain_set):
            chain.append(curr)
            chain_set.add(curr)
            try:
                chain_length = chain_dict[curr]
                for j in range(len(chain)-2, -1, -1):
                    chain_dict[chain[j]] = chain_length + (len(chain) - 1 - j)
                break
            except KeyError:
                curr = digit_fact_sum(curr)
        else:
            j = 0
            while (chain[j] != curr):
                chain_dict[chain[j]] = len(chain) - j
                j += 1
            chain_dict[chain[j]] = len(chain) - j
    return chain_dict

cd = build_dict({169 : 3,
                 363601 : 3,
                 1454 : 3,
                 871 : 2,
                 872 : 2,
                 45361 : 2,
                 45362 : 2})
'''
Why is it important to start build_dict with the above
numbers already in chain_dict? That is because these 
are the only 3 numbers that form a loop. For example, 
during the building of the dict, let's say 1454 is 
encountered. In this case, the next curr is 169. Since,
169 is already in chain_dict, our algorithm will assign
1454 chain_dict[169] + 1 as the chain_length, which is 
wrong. THE ALGORITHM DOES NOT HOLD UP TO THE EDGE CASES
OF THE LOOPS ABOVE. chain_dict[1454] should be the same
as chain_dict[169] (Just draw the chain in your head)
'''
count = 0
for e in cd:
    if cd[e] == 60:
        count += 1
print(count)
                
            
