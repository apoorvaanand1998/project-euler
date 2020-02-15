'''
printing the values from the commented program below
we notice that the numerator increases by 3 and
the denominator increases by 7 as we get closer to the value we want

diff = [1, 1, 1] ## difference between fraction being tested and 3/7
## we went this difference to be the smallest while the fraction
## itself is lesser in value than 3/7

for denominator in range(2, 10**6+1):
    for numerator in range(2, denominator):
        if denominator % numerator != 0:
            if numerator / denominator >= 3/7:
                break
            else:
                our_frac_val = numerator / denominator
                if (3/7 - our_frac_val) < diff[2]:
                    diff = [our_frac_val,
                            str(numerator) + "/" +
                            str(denominator),
                            3/7 - our_frac_val]
                    print(diff)
'''

denom = 12  ## first denom found by above program
denom_counter = 0
while (denom+7) < 10**6:
    denom += 7
    denom_counter += 1

numer = 5  ## first numer found by above program
numer = numer + denom_counter * 3
print(numer)
