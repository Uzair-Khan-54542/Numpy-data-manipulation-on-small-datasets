import numpy as np 

# 10. Dice role simulator.
'''
# ========================================================================
# ========================== S T A R T ============================================
# ========================================================================



dice_rolls = np.array([1,4,1,5,6,4,2,1,2,4,4,1,4,3,3,6,5,3,2,6,2,2,3,1,4,3,5,3,5,2,1,5,3,1,3,1,5,4,4,1,6,3,2,5,1,5,5,1,4,1,5,2,1,6,4,1,5,2,3,6,2,6,1,1,1,3,2,3,6,5,5,5,6,5,5,5,6,5,3,3,5,3,3,3,4,4,3,2,2,2,4,5,3,6,4,3,5,1,4,5])


# ========================================================================
# Counting the occurance of each number in the dice (1-6).
ones_count = np.sum(dice_rolls == 1)
twos_count = np.sum(dice_rolls == 2)
threes_count = np.sum(dice_rolls == 3)
fours_count = np.sum(dice_rolls == 4)
fives_count = np.sum(dice_rolls == 5)
sixes_count = np.sum(dice_rolls == 6)

each_number_occurance = np.array((ones_count, twos_count, threes_count, fours_count, fives_count, sixes_count))


# ========================================================================
# Calculating the probability of each number.
p_1 = ones_count / 100
p_2 = twos_count / 100
p_3 = threes_count / 100
p_4 = fours_count / 100
p_5 = fives_count / 100
p_6 = sixes_count / 100

each_number_probability = np.array((p_1, p_2, p_3, p_4 ,p_5, p_6))


# ========================================================================
# Most frequently rolled number.
most_frequently_rolled_number = np.argmax(each_number_occurance) + 1



# ========================================================================
# Printing statements.
# print(dice_rolls, '\n')
# print(each_number_occurance, '\n')
# print(each_number_probability, '\n')
print(f'Most frequently rolled number = {most_frequently_rolled_number}\n')



# ========================================================================
# ========================== E N D ============================================
# ========================================================================

'''