##################################################################################
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, #
# a2 + b2 = c2                                                                   #
#                                                                                #
# For example, 32 + 42 = 9 + 16 = 25 = 52.                                       #
#                                                                                #
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.       #
# Find the product abc.                                                          #
##################################################################################

s = 1000

for a in range (1, (s - 3)//3):
    for b in range (a, (s - a - 1)//2):
        c = s - a - b
        if c*c == a*a + b*b:
            print(a, b, c, a * b * c)
