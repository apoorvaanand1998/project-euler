l = [[1, 3], [1, 2]]
d = 12000
i = 0

while (i < len(l) - 1):
    num = l[i][0] + l[i+1][0]
    denom = l[i][1] + l[i+1][1]

    if num < d and denom <= d:
        l.insert(i + 1, [num, denom])
    else:
        i += 1
print(len(l)-2)
