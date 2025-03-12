# [   CODE BY @RandomProgrammerGuy ON GITHUB   ]------------------------------------- #

# [   PROBLEM DESCRIPTION   ]-------------------------------------------------------- #
# Given a rope of length n meters, cut the rope in different parts of integer lengths #
# in a way that maximizes product of lengths of all parts. You must make at least one #
# cut. Assume that the length of rope is more than 2 meters.                          #
# ----------------------------------------------------------------------------------- #

from random import randint
from time import time

# Initializing the cord length variable
cord_length = randint(2,20)

print(f'Randomly generated cord length = {cord_length}')

# Algorithm starts here
start_time = time()
