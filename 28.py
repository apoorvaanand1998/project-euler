###################################################################################################
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way #
###################################################################################################
n = 1
sum_of_diagnols = 1
counter4 = 0
interval = 2

while (n < 1001*1001):
    if counter4 == 4:
        counter4 = 0
        interval += 2
    n += interval
    sum_of_diagnols += n
    counter4 += 1

print(sum_of_diagnols)
