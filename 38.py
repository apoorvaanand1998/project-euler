###############################################################################################################################################################################
# Take the number 192 and multiply it by each of 1, 2, and 3:                                                                                                                 #
#                                                                                                                                                                             #
#     192 * 1 = 192                                                                                                                                                           #
#     192 * 2 = 384                                                                                                                                                           #
#     192 * 3 = 576                                                                                                                                                           #
#                                                                                                                                                                             #
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)                                   #
#                                                                                                                                                                             #
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5). #
#                                                                                                                                                                             #
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?                          #
###############################################################################################################################################################################

def is_pan(n):
    return sorted(list(str(n))) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']
   
for i in range(9000, 10000):
    if is_pan(int(str(i)+str(i*2))):
        print(i, i*2, sep='')

###################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
# The problem tells us that 918273645 is a pandigital number. Therefore the pandigital number we have to find has to be greater than 918273645. For us to get a larger pandigital number we need a two (or more) digit(s) number starting with 9. It cannot be a two digit number starting with 9 because 9x * 3 gives us a 3 digit number therefore it's impossible to form pandigital numbers with a two digit number. Similarly, it is impossible for a pandigital number to be formed that starts with 9 and is 3 digits. Therefore it has to be a four digit number starting with 9 that when multiplied by 2, gives us a 5 digit number, the concatenation of which is a pandigital number. #
###################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################



    
