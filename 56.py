def digital_sum(n):
    return sum(list(map(int, list(str(n)))))

mds = 0
for i in range(1, 100):
    for j in range(1, 100):
        ds = digital_sum(i**j)
        if ds > mds:
            mds = ds
print(mds)
