##################################################################################################
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9? #
##################################################################################################

def next_perm(a):
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            k = i
    for j in range(k+1, len(a)):
        if a[j] > a[k]:
            l = j
    a[k], a[l] = a[l], a[k]
    a = a[:k+1] + a[-1:k:-1]
    return a

p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(999999):
    p = next_perm(p)
print("".join(map(str, p)))

###############################################################################
# https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order #
# https://www.topcoder.com/blog/generating-permutations/                      #
###############################################################################
    
    


