
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
# COMBINATIONS IN A LIST AND AT THE END IT RETURNS THE MOST EFFICIENT OF THEM ALL     #
#######################################################################################

