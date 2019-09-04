kinds_of_coins = [1, 2, 5, 10, 20, 50, 100, 200]

d = {}

def no_of_ways(amount, no_of_coins):
    try:
        return d[(amount, no_of_coins)]
    except:
        if amount == 0:
            return 1
        if (amount < 0 or no_of_coins == 0):
            return 0
        ans = (no_of_ways(amount, no_of_coins - 1) +
               no_of_ways(amount - kinds_of_coins[-no_of_coins], no_of_coins))
        d[(amount, no_of_coins)] = ans
        return ans

print(no_of_ways(200, 8))  ## btw this memoized version still fails to calculate 10000 
