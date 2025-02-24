# [   CODE BY @RandomProgrammerGuy ON GITHUB   ]------------------------------------- #

# [   PROBLEM DESCRIPTION   ]-------------------------------------------------------- #
# Given an array of coins[] of size n and a target value sum, where coins[i]          #
# represent the coins of different denominations. You have an infinite supply of each #
# of the coins. The task is to find the minimum number of coins required to make the  #
# given value sum.                                                                    #
# ----------------------------------------------------------------------------------- #

from random import randint
from pprint import pprint
from time import time

# Initializing coins and n
coins = [1, 2, 5, 10, 20, 50, 100, 200] # Based on the EUR coins

n = randint(1, 10000) # Modelizes a random sum from 1 cent to 100 EUR
print(f'Random n = {n / 100:.2f} EUR')

# Algorithm starts here
start_time = time()

min_coins = [0 for number in range(n+1)]

for index in range(n + 1):

    # Initializing the first cell of the array
    if index == 0:
        min_coins[index] = 0
        continue

    # Setting a baseline value for all non-first cells
    else:
        min_coins[index] = min_coins[index - 1] + 1
    

    for coin in coins:
        
        if index - coin >= 0:
            min_coins[index] = min( min_coins[index - coin] + 1 , min_coins[index] )

end_time = time()

# Printing the reults
print(f'Minimum amount of coins to reach {n/100} EUR: {min_coins[n]:.2f}')
print(f'Elapsed time = { end_time - start_time }')