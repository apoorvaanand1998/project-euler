

######################################################################################################
# An irrational decimal fraction is created by concatenating the positive integers:                  #
#                                                                                                    #
# 0.123456789101112131415161718192021...                                                             #
#                                                                                                    #
# It can be seen that the 12th digit of the fractional part is 1.                                    #
#                                                                                                    #
# If dn represents the nth digit of the fractional part, find the value of the following expression. #
#                                                                                                    #
# d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000                                              #
######################################################################################################

l = []
l.append(0)
n = 1
while len(l) < 1000010:
    l += list(map(int, list(str(n))))
    n += 1

print(l[1], l[10], l[100], l[1000], l[10000], l[100000], l[1000000])
    
    
