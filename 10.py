#########################################################
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. #
#                                                       #
# Find the sum of all the primes below two million.     #
#########################################################
import math

l = []
lp = [True] * 2000000
lp[0] = False
lp[1] = False

for i in range(math.ceil(math.sqrt(len(lp)))):
    if lp[i]:
        for j in range (i * i, len(lp), i):
            lp[j] = False

for i in range(len(lp)):
    if lp[i]:
        l.append(i)

print(l, sum(l))
