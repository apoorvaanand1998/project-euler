l = [True] * 1000000
l[0] = l[1] = False

for i in range(2, int(1000000**0.5)+2):
    if l[i]:
        for j in range(i*i, 1000000, i):
            l[j] = False

pl = []
ps = set()
psum = [0]
for i in range(1000000):
    if l[i]:
        pl.append(i)
        ps.add(i)
        psum.append(psum[-1]+i)

longest = [0, 0]
for i in range(len(psum)):
    current = psum[i]
    for j in range(i, len(psum)):
        if (psum[j]-current) > 1000000:
            break
        if (psum[j]-current) in ps and (psum[j]-current) > longest[0] and (j-i) > longest[1]:
            longest = [psum[j]-current, j-i]
print(longest)

