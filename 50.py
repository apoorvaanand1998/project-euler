l = [True] * 1000000
l[0] = l[1] = False

for i in range(2, int(1000000**0.5)+2):
    if l[i]:
        for j in range(i*i, 1000000, i):
            l[j] = False

pl = []
ps = set()
for i in range(1000000):
    if l[i]:
        pl.append(i)
        ps.add(i)

longest = 0
for initial in range(len(pl)):
    for final in range(initial, len(pl)):
        if sum(pl[initial:final]) > pl[-1]:
            break
        elif sum(pl[initial:final]) in ps:
            if final-initial > longest:
                longest = final-initial
                lp = sum(pl[initial:final])
print(longest, lp)
        
