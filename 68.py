from itertools import combinations, permutations

def all_10_in(e):
    all_10 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    e = list(map(set, e))
    return e[0].union(e[1], e[2], e[3], e[4]) == all_10

def not_more_than_2_in(l):
    lr = list(range(1, 11))
    freq = {}
    for e in lr:
        freq[e] = 0
        
    for e in l:
        for el in e:
            freq[el] += 1
            if freq[el] > 2:
                return False
    return True

l = list(range(1, 11))
c = list(combinations(l, 3))

poss = []
for e in c:
    if sum(e) == 14:
        poss.append(e)
print(poss, len(poss))

all_10 = []
c = list(combinations(poss, 5))
for e in c:
    if all_10_in(e):
        all_10.append(e)
print(all_10)

not_more_than_2 = []
for e in all_10:
    if not_more_than_2_in(e):
        not_more_than_2.append(e)
print(not_more_than_2)
        
