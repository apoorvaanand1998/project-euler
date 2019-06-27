
################################################################################################################################################
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be: #
#                                                                                                                                              #
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...                                                                                                       #
#                                                                                                                                              #
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.           #
################################################################################################################################################

fib = [1, 2]

ne = 3
res = 2  # 2 is already in the fib list and accounted for here

while ne < 4000000:
    fib.append(ne)
    ne = fib[-1] + fib[-2]
    if ne%2 == 0:
        res += ne
print(res)
