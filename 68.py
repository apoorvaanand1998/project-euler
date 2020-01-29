from itertools import permutations, combinations
from collections import defaultdict

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
        return True if (freq[10] == 1) else False ## 10 can only occur once because they want 16 digit string

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
    #print(poss, len(poss))
    if poss == []:
        return False

    diff_1 = []
    for e in poss:
        p = list(permutations(e))
        for el in p:
            if diff_1_in(el):
                diff_1.append(e)
    print(diff_1, len(diff_1))

comb_list = list(combinations(list(range(1, 11)), 3))
poss = pick_3_of_total(comb_list, 14)
filter(poss)
