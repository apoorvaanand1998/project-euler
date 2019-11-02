def is_prime(n):
    if n <= 1:
        return False
    elif n <= 4:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

def count_primes(diagnol):
    count = 0
    for n in diagnol:
        if is_prime(n):
            count += 1
    return count

cppd = 3  ## count of primes in previous diagnols
cpd = 5
curr_diag = [13, 17, 21, 25]
curr = 25
gap = 3
perc = 62

while (perc >= 10):
    cppd += count_primes(curr_diag)
    cpd += len(curr_diag)
    curr_diag = []
    gap += 2
    
    for i in range(4):
        curr += gap + 1
        curr_diag.append(curr)
    perc = ((cppd + count_primes(curr_diag)) / (cpd + len(curr_diag))) * 100
print(gap+2)  ## gap = length of side of square - 2
    
    
        
    
            
