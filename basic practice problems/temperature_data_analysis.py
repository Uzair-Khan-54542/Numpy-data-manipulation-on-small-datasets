


import numpy as np 



# 3. Temperature Data Analysis
'''
# ========================================================================
# ========================== S T A R T ============================================
# ========================================================================



# Daily temperatures for 30 days (in Celsius)
temperatures = np.array([
    22, 24, 21, 23, 25, 26, 24, 22, 23, 21,
    20, 22, 24, 25, 23, 21, 22, 24, 26, 25,
    23, 22, 21, 20, 22, 23, 24, 25, 26, 24
])



# ========================================================================
# Converting all temperatures into fahrenheit.
temperatures = ((temperatures * (9 / 5)) + 32)



# ========================================================================
# Fidnging the highest and the lowest temperature recorded.
maximum_temp = round(np.max(temperatures), 2)
minimum_temp = round(np.min(temperatures), 2)


# ========================================================================
# Computing average temperature.
average_temperature = np.mean(temperatures)



# ========================================================================
# Counting days with temperature above average.
temp_above_avg = (temperatures > average_temperature).sum()


# ========================================================================
# Converting tempertaure from Fahrenheit to celcius again and finding index of temperatures > 35.
temperatures = (temperatures - 32) * (5 / 9)
idx = np.where(temperatures > 35)[0]



# ========================================================================
# Printing statements.
# print(temperatures, '\n')
# print(f'Maximum temperature = {maximum_temp} F\nMinimum temperature = {minimum_temp}F\n')
# print(f'Average temperature = {average_temperature} F\n')
# print(f'Indexes where temperature is above 35 = {idx} \n')



# ========================================================================
# ========================== E N D ============================================
# ========================================================================

'''


