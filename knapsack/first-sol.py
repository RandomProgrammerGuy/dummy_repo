
### KNAPSACK PROBLEM ##################################################################
# SOLUTION #1                                                                         #
# CODE WRITTEN BY @RandomProgrammerGuy ON GITHUB                                      #
#######################################################################################

### ABOUT THIS SOLUTION ###############################################################
# THIS SOLUTION IS THE ONE THAT INTUITIVELY CAME TO MY MIND UPON SEEING THE PROBLEM.  #
# IT IS NOT NECESSARILY THE MOST EFFICIENT NOR THE MOST ELEGANT, BUT I WROTE THIS     #
# WITHOUT LOOKING AT ANY OTHER SOLUTIONS. IT IS REALLY A FIRST ATTEMPT. IT WORKS BY   #
# FIRST CALCULATING THE MAXIMUM NUMBER OF COMBINATIONS BY DIVIDING THE SACK'S MAXIMUM #
# WEIGHT BY THE WEIGHT OF THE LIGHTEST ITEM IN THE LIST. THEN FOR ALL VALUES OF K     #
# FROM 1 TO THE MAXIMUM NUMBER OF COMBINATIONS, IT CALCULATES ALL K-COMBINATIONS OF   #
# THE ITEMS LIST AND SELECTS THE MOST EFFICIENT. IT STORES ALL OF THE MOST EFFICIENT  #
# COMBINATIONS IN A LIST AND AT THE END IT RETURNS THE MOST EFFICIENT OF THEM ALL.    #
# AS YOU MAY HAVE REALIZED, IT IS A NON-DYNAMIC SOLUTION, WITH A TIME COMPLEXITY OF   #
# O(n * 2^n) (IF I CALCULATED THAT CORRECTLY)                                         #
#######################################################################################

from random import randint
from pprint import pprint
from itertools import combinations
from time import time

print('\n--------------------------------------------------')
print('-- KNAPSACK PROBLEM ------------------------------')
print('-- Solution 1 by @RandomProgrammerGuy on GitHub --')
print('--------------------------------------------------\n')

### Step 1 - Creating the objects list ################################################

obj_list_len = randint(10, 20)
obj_list = []

for i in range(obj_list_len):
    weight = randint(1, 10)
    value = randint(5, 25)
    obj_list.append((weight, value))

print(f'Object list (length = {obj_list_len}):\n')
pprint(obj_list)
print('\n')


### Step 2 - Initializing the knapsack ################################################

knapsack_max_weight = randint(40, 80)
print(f'Knapsack weight limit = {knapsack_max_weight}\n')


### Step 3 - The main algorithm #######################################################

start_time = time() # Used to calculate elapsed time

max_weight = 0
max_value_combination = ()
max_value = 0

for k in range(1, obj_list_len+1):

    combinations_list = list(combinations(obj_list, k))

    for combination in combinations_list:

        weight = 0
        value = 0

        for item in combination:
            weight += item[0]
            value += item[1]

        if weight <= knapsack_max_weight and max_value < value:
            max_weight = weight
            max_value_combination = combination
            max_value = value

end_time = time()

print('Most efficient combination found :')
print(max_value_combination)
print(f'\nMost efficient combination value = {max_value}\n')
print(f'Most efficient combination weight = {max_weight}\n')
print(f'Time elapsed = {end_time - start_time}s')