kinds_of_coins = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 10000

dp = [1] * (amount + 1)
l = len(kinds_of_coins)

for i in range(1, l):
    current_coin = kinds_of_coins[i]
    for j in range(current_coin, amount + 1):
        dp[j] += dp[j - kinds_of_coins[i]]
            
print(dp[10000])

########################################################################################################################################
# Explanation in overview and by drawing the dp table for this problem (can be found in many videos online but do it yourself instead) #
########################################################################################################################################
