## HAVE TO UNDERSTAND OVERVIEW OF PROBLEM 31 FOR THIS
## THIS IS A VARIATION OF THE COIN CHANGE PROBLEM
## HAVE TO USE THE DP SOLUTION
## THE RECURSIVE SOLUTION IS TOO SLOW

def no_of_ways(s):
    l = [1] * (s + 1)
    for denomination in range(2, s):
        for amount in range(denomination, len(l)):
            l[amount] += l[amount - denomination]
            ## draw dp table to understand this
    return l[-1]

print(no_of_ways(100))
                
                
    
