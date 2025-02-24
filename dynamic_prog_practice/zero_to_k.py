# [   CODE BY @RandomProgrammerGuy ON GITHUB   ]------------------------------------- #

# [   PROBLEM DESCRIPTION   ]-------------------------------------------------------- #
# Given a positive integer K, the task is to find the minimum number of operations of #
# the following two types, required to change 0 to K:                                 #
# - Add one to the operand                                                            #
# - Multiply the operand by 2                                                         #
# ----------------------------------------------------------------------------------- #

from random import randint
from math import log2, ceil
from time import time

# Initializing and printing the integer k
k = randint(1, 20)
print(f'Random k = {k}')

# Main algorithm starts here
start_time = time()
array = [0 for i in range(k + 1)]

for i in range(k + 1):

    if i == 0:
        array[i] = 0

    else:
        if i % 2 == 0:
            array[i] = min(array[i - 1] + 1, array[int(i / 2)] + 1)
        
        else:
            array[i] = array[i - 1] + 1

end_time = time()

# Printing the results
print(f'The minimum no. of operations to reach k = {k} is {array[k]}')
print(f'Elapsed time: {end_time - start_time}')