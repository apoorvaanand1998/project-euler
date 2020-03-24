from itertools import permutations

def does_it_fit(n, nums):
    flag = 1
    for e in nums:
        if not flag:
            return False
        e = list(map(int, list(str(e))))
        if ((n.index(e[0]) < n.index(e[1])) and
            (n.index(e[1]) < n.index(e[2]))):
            flag *= 1
        else:
            flag *= 0
    return True

shortest_passcode_chars = set()
succ_logs = []

with open('p079_keylog.txt') as f:
    for e in f:
        succ_logs.append(int(e[:-1]))
        l = list(map(int, list(e)[:-1]))
        shortest_passcode_chars.update(map(int, list(e)[:-1]))

    shortest_passcode_chars = list(shortest_passcode_chars)

p = list(permutations(shortest_passcode_chars))

for e in p:
    if does_it_fit(e, succ_logs):
        print(int(''.join(map(str, list(e)))))
        break
