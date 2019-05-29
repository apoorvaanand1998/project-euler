import math

n = 600851475143
lpf = []
while (n % 2 == 0):
    lpf.append(2)
    n = n / 2
i = 3
while (i <= math.ceil(math.sqrt(n)) + 1):
    if (n % i == 0):
        lpf.append(i)
        n = n / i
    else:
        i += 2
if n > 1:
    lpf.append(n)
print(lpf)

###############################################
# https://www.youtube.com/watch?v=6PDtgHhpCHo #
# Programming Challenges - Skiena             #
###############################################
