#########################################################################################
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits? #
#########################################################################################

def find_fac(n):
    i = 1
    j = 1
    k = i + j
    pos = 3
    while (len(str(k)) < n):
        i, j = j, k
        k = i + j
        pos += 1
    return pos

print(find_fac(1000))
