maxc = [0, 0]
for p in range(120, 1001):
    count = 0
    for a in range(1, p//3+2):
        for b in range(a, p//2+1):
            if a**2 + b**2 == (p - a - b)**2:
                count += 1
    if count > maxc[1]:
        maxc = [p, count]
print(maxc)
