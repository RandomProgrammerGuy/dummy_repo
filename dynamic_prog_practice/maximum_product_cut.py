# [   CODE BY @RandomProgrammerGuy ON GITHUB   ]------------------------------------- #

# [   PROBLEM DESCRIPTION   ]-------------------------------------------------------- #
# Given a rope of length n meters, cut the rope in different parts of integer lengths #
# in a way that maximizes product of lengths of all parts. You must make at least one #
# cut. Assume that the length of rope is more than 2 meters.                          #
# ----------------------------------------------------------------------------------- #

from random import randint
from time import time

# Initializing the cord length variable
cord_length = randint(2,100)

print(f'Randomly generated cord length = {cord_length}')

# Algorithm starts here
start_time = time()

# N+1 x N array where each line represents cord length and each column the number of cuts
lengths_cuts = [ [0 for i in range(cord_length)] for j in range(cord_length+1) ]


# Initializing value for cord length 2 (minimum)
lengths_cuts[2][1] = 1

for i in range(3, cord_length + 1):

    for j in range(1, cord_length):
        if j == 1:
            lengths_cuts[i][j] = (i // 2) * (i - (i // 2))
        
        elif j < i :
            maximum = 1

            for k in range(1, i - (j - 1) + 1):
                if k * lengths_cuts[i - k][j - 1] > maximum:
                    maximum = k * lengths_cuts[i - k][j - 1]

            lengths_cuts[i][j] = maximum

        else:
            break

result = max(lengths_cuts[i])
end_time = time()

# Printing results
print(f'Optimal cut product for cord length = {cord_length} is {result}')
print(f'Elapsed time = {end_time - start_time}s')
