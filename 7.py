
########################################################################################################
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. #
#                                                                                                      #
# What is the 10 001st prime number?                                                                   #
########################################################################################################

## 10000001 is just some large number
b_arr = [True] * 110000
b_arr[0] = False
b_arr[1] = False

for i in range (2, 110000):
    if b_arr[i] == True:
        for j in range (i*i, 110000, i):
            b_arr[j] = False

l = []

for i in range (110000):
    if b_arr[i]:
        l.append(i)

print(l[0], l[1], l[10000])

