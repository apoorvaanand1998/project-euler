from itertools import permutations, combinations
from collections import defaultdict

## Works by filtering (and pruning? I guess? Don't know the official term)
## Look at each function name to understand what it does

def pick_3_of_total(comb_list, total):
    poss = []
    for e in comb_list:
        if sum(e) == total:
            poss.append(e)
    return poss

def filter(poss):
    def all_10_in(e):
        all_10 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        e = list(map(set, e))
        return e[0].union(e[1], e[2], e[3], e[4]) == all_10

    def not_more_than_2_in(l):
        freq = defaultdict(int)
        for e in l:
            for el in e:
                freq[el] += 1
                if freq[el] > 2:
                    return False
        return True if (freq[10] == 1) else False
    ## 10 can only occur once because they want 16 digit string

    def diff_1_in(l):
        l = list(map(set, l))
        common = set()
        
        for i in range(len(l)):
            if i == len(l) - 1:
                c = l[i].intersection(l[0])
            else:
                c = l[i].intersection(l[i+1])
            if len(c) == 1:
                common = common.union(c)
        return len(common) == 5

    def arrange_list_of_five(lof):
        lof = list(map(set, lof))
        common = []

        for i in range(len(lof)):
            if i == len(lof) - 1:
                c = max(lof[i].intersection(lof[0]))
            else:
                c = max(lof[i].intersection(lof[i+1]))
            common.append(c)

        singles = []
        for e in lof:
            singles.append(max(e - set(common)))

        c = common
        s = singles

        arranged = [ s[0], c[-1], c[0], s[1], c[0], c[1], s[2], c[1], c[2], s[3],  c[2], c[3], s[4], c[3], c[4] ]

        return arranged

    poss = list(combinations(poss, 5))
    all_10 = []
    for e in poss:
        if all_10_in(e):
            all_10.append(e)
    poss = all_10

    if poss == []:
        return False

    not_more_than_2 = []
    for e in poss:
        if not_more_than_2_in(e):
            not_more_than_2.append(e)
    poss = not_more_than_2

    if poss == []:
        return False

    diff_1 = []
    for e in poss:
        p = list(permutations(e))
        for el in p:
            if diff_1_in(el):
                diff_1.append(el)
    poss = diff_1

    if poss == []:
        return False

    arranged_strings = []
    for e in poss:
        arr = arrange_list_of_five(e)
        arranged_strings.append(arr)

    return min(arranged_strings, key=lambda x:x[0])

comb_list = list(combinations(list(range(1, 11)), 3))

for total in range(13, 28):
    poss = pick_3_of_total(comb_list, total)
    print(total, filter(poss))
