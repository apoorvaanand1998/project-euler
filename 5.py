##############################################################################################################
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. #
#                                                                                                            #
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?          #
##############################################################################################################

import math
import pprint
from collections import defaultdict

def lpf(n):
    l = []
    while (n % 2 == 0):
        l.append(2)
        n = n / 2
    i = 3
    while (i <= math.ceil(math.sqrt(n)) + 1):
        if (n % i == 0):
            l.append(i)
            n = n / i
        else:
            i += 2
    if n > 1:
        l.append(n)
    return l
    
lpf_dict = {}

for i in range (1, 21):
    lpf_dict[i] = lpf(i)

pprint.pprint(lpf_dict)

count_dict = defaultdict(int)

for i in range (1, 21):
    for j in range (1, 21):
        if j in lpf_dict[i]:
            if lpf_dict[i].count(j) > count_dict[j]:
                count_dict[j] = lpf_dict[i].count(j)

pprint.pprint(count_dict)

res = 1
for i in count_dict:
    res = res * math.pow(i, count_dict[i])
print(res)
