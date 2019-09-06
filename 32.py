from collections import defaultdict

def pandigital1_9(*args):
    str_args = list(map(str, args))
    nums = defaultdict(int)
    for arg in str_args:
        for num in arg:
            nums[num] += 1
    if nums['0'] == 0:
        if nums['1'] == nums['2'] == nums['3'] == nums['4'] == nums['5'] == nums['6'] == nums['7'] == nums['8'] == nums['9'] == 1:
            return True
    return False

sum_prod = 0
for i in range(4396, 10000):
    for j in range(1, int(i**(0.5)+1)):
        if int(i/j) == i/j:
            if pandigital1_9(j, i//j, i):
                sum_prod += i
                break

print(sum_prod)

