from decimal import *
import math

total = 0
for i in range(1, 101):
    sr = math.sqrt(i)
    if sr != int(sr):
        getcontext().prec = 102
        n = list(str(Decimal(i).sqrt()))[:-2] ## making prec 102 and doing this
        ## to stop rounding errors
        n.remove('.')
        digital_sum = sum(map(int, n))
        ##  print(i, digital_sum)
        total += digital_sum
print(total)
