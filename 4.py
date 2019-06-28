
#########################################################################################################################################
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99. #
#                                                                                                                                       #
# Find the largest palindrome made from the product of two 3-digit numbers.                                                             #
#########################################################################################################################################

def ispal(n):
    if str(n) == str(n)[::-1]:
        return True
    return False

res = 0

for i in range (999, 900, -1):
    for j in range (999, 900, -1):
        if ispal(i * j) and (i * j) > res:
            res = i * j

print(res)
