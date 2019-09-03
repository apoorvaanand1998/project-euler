########################################################################################################################
# How many different ways can £2 be made using any number of coins? 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p) #
########################################################################################################################

kinds_of_coins = [1, 2, 5, 10, 20, 50, 100, 200]

def no_of_ways(amount, no_of_coins):
    if amount == 0:
        return 1
    if (amount < 0 or no_of_coins == 0):
        return 0
    return (no_of_ways(amount, no_of_coins - 1) +
            no_of_ways(amount - kinds_of_coins[-no_of_coins], no_of_coins))

print(no_of_ways(200, 8))

