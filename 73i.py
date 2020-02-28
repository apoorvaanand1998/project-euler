d = 12000
curr = [1, 3]
frac_list = [[1, 2]]
count = 0

while (len(frac_list) > 0):
    num = curr[0] + frac_list[-1][0]
    denom = curr[1] + frac_list[-1][1]

    if num < d and denom <= d:
        frac_list.append([num, denom])
        count += 1
    else:
        curr = frac_list.pop()
print(count)
