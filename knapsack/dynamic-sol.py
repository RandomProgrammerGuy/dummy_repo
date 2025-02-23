### KNAPSACK PROBLEM ##################################################################
# SOLUTION #2                                                                         #
# CODE WRITTEN BY @RandomProgrammerGuy ON GITHUB                                      #
#######################################################################################

### ABOUT THIS SOLUTION ###############################################################
# THIS SOLUTION IS THE DYNAMIC PROGRAMMING SOLUTION TO THE PROBLEM. WE USE A 2D ARRAY #
# WHERE THE COLUMNS REPRESENT MAXIMUM KNAPSACK WEIGHT LIMITS FROM 0 TO THE ACTUAL     #
# LIMIT OF OUR KNAPSACK AND THE ROWS REPRESENT EACH OBJECT AS THEY APPEAR IN THE LIST #
# OF OBJECTS. THE INDEX 0 ROW AND COLUMN ARE INITIALIZED AT 0. FOR THE OTHERS, AS WE  #
# ITERATE THROUGH EACH CELL OF EACH ROW, IF THE WEIGHT OF THE ITEM CONSIDERED IS MORE #
# THAN THE COLUMN INDEX (AKA THE CONSIDERED MAXIMUM WEIGHT LIMIT), THE VALUE OF THE   #
# CELL WILL BE SET TO THE SAME AS THE CELL ABOVE IT. THIS REPRESENTS THE CASE WHERE   #
# WE "WOULD NOT CHOOSE THE ITEM" BECAUSE "IT DOESN'T FIT INTO THE SACK", AND THE      #
# IN THE CELL ABOVE IS THE PREVIOUS MAXIMUM VALUE FOUND FOR A SACK OF THAT CAPACITY   #
# IF THE ITEM "DOES FIT," WE THEN ANALYZE TWO OPTIONS: 1. PUTTING THE CONSIDERED ITEM #
# INTO THE SACK AND SEEING HOW MUCH WE CAN FIT INTO A SACK WHOSE CAPACITY IS EQUAL TO #
# THE CURRENT MAX CAPACITY MINUS THE CAPACITY TAKEN BY THE CHOSEN ITEM, AND 2. NOT    #
# TAKING THE OBJECT AND TAKING OTHERS INSTEAD. THE OPTION WITH THE MAXIMUM VALUE IS   #
# CHOSEN AND THE VALUE STORED IN THE ARRAY CELL. WITH THIS ALGORITHM, THE VALUE IN    #
# THE LAST CELL OF THE LAST COLUMN IS THE HIGHEST VALUE WE CAN STORE. IN THIS CODE WE #
# ALSO STORE THE COMBINATIONS IN AN ARRAY WITH THE SAME DIMENSIONS, SO WE CAN RECALL  #
# IT.
#######################################################################################

from random import randint
from pprint import pprint
from time import time

print('\n--------------------------------------------------')
print('-- KNAPSACK PROBLEM ------------------------------')
print('-- Solution 2 by @RandomProgrammerGuy on GitHub --')
print('--------------------------------------------------\n')

### Step 1 - Creating the objects list ################################################

n_obj = randint(10, 20)
obj_list = []

for i in range(n_obj):
    weight = randint(1, 10)
    value = randint(5, 25)
    obj_list.append((weight, value))

print(f'Object list (length = {n_obj}):\n')
pprint(obj_list)
print('\n')


### Step 2 - Initializing the knapsack ################################################

sack_max_w = randint(40, 80)                   
print(f'Knapsack weight limit = {sack_max_w}\n')


### Step 3 - The main algorithm #######################################################
start_time = time()

# Will store the max value for each max capacity and item combination
w_val_combos = [[0 for i in range(sack_max_w)] for j in range(n_obj)]

# Will store the corresponding combination for each cell in the prev. 2D array
obj_combos = [[[] for i in range(sack_max_w)] for j in range(n_obj)]

for obj_n in range(1, n_obj):

    for max_cap in range(sack_max_w):

        # Case where the code analyzes the first row or column (unexclusive or)
        if obj_n == 0 or max_cap == 0:

            w_val_combos[obj_n][max_cap] = 0
            continue

        obj_n_w = obj_list[obj_n][0]
        obj_n_value = obj_list[obj_n][1]

        # If the object is "too large" for the sack
        if obj_n_w > max_cap:

            w_val_combos[obj_n][max_cap] = w_val_combos[obj_n - 1][max_cap]

        # If the object "would fit" in the sack
        else :
            
            # Max value of sack items if the object is included
            max_v_w_obj = obj_n_value + w_val_combos[obj_n - 1][max_cap - obj_n_w]

            # Max value of sack items if the object is not included
            max_v_wo_obj = w_val_combos[obj_n - 1][max_cap]

            # If it's better to include the object
            if max_v_w_obj > max_v_wo_obj:

                w_val_combos[obj_n][max_cap] = max_v_w_obj

                best_combo_after_add = obj_combos[obj_n - 1][max_cap - obj_n_w]
                obj_combos[obj_n][max_cap] = best_combo_after_add + [obj_list[obj_n]]
                
            # If it's better NOT TO include the object
            else:

                w_val_combos[obj_n][max_cap] = max_v_wo_obj
                obj_combos[obj_n][max_cap] = obj_combos[obj_n - 1][max_cap - obj_n_w]

end_time = time()

### Step 4 - Printing the results #####################################################

print('Most efficient combination found :')
print(obj_combos[-1][-1])
print(f'\nMost efficient combination value = {w_val_combos[-1][-1]}\n')
print(f'Time elapsed = {end_time - start_time}s')
