## Felt bad about taking advantage of python's decimal module
## Computed the square root using the long divison method

import math

def sr(n):
    def find_divisor(cq, dd):
        def closest_to_zero(l):     
            ## returns e in l closest to zero and e < 0
            closest_yet = [0, math.inf]
            for i in range(len(l)):
                if ((l[i] >= 0) and (((l[i] - 0) < closest_yet[1]))):
                    closest_yet = [i, l[i] - 0]
            return closest_yet[0]
        
        beg_part = 2*cq
        diffs = []
        for i in range(0, 10):
            to_sub = int(str(beg_part) + str(i)) * i
            after_sub = dd - to_sub
            diffs.append(after_sub)
            
        cy = closest_to_zero(diffs)
        div = int(str(beg_part) + str(cy))
        return div

    def stitch_nums(l):
        return int(''.join(map(str, l)))

    decimal_digits = []
    i = 1
    while ((i+1)**2 <= n):
        i += 1
    decimal_digits.append(i)

    dividend = (n - (i*i)) * 100
    divisor = i
    curr_quotient = i

    while len(decimal_digits) < 100:
        new_divisor = find_divisor(curr_quotient, dividend)
        decimal_digits.append(new_divisor % 10)

        curr_quotient = stitch_nums(decimal_digits) 
        dividend = (dividend - (new_divisor * (new_divisor % 10))) * 100
     
    return decimal_digits

total = 0
for i in range(2, 100):
    if math.sqrt(i) != int(math.sqrt(i)):
        s = sum(sr(i))
        total += s
print(total)
