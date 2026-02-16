import numpy as np 

# 9. Basic salary calculator.
'''
# ========================================================================
# ========================== S T A R T ============================================
# ========================================================================



salaries = np.array([35000, 42000, 39000, 47000, 51000, 46000, 38000, 44000])
# print(f'Salaries without tax deduction = {salaries}\n')

# ========================================================================
# Deducting 10% tax from each employess salary.
salaries = salaries * 0.9


# ========================================================================
# Adding 5% bonus to each taxed salary and creating the final salary.
bonus = salaries * 0.05
salaries += bonus


# ========================================================================
# Finding the highest and the lowest final salary.
highest_final_salary = np.max(salaries)
lowest_final_salary = np.min(salaries)


# ========================================================================
# Calculating the final average salary.
average_final_salary = np.mean(salaries)




# ========================================================================
# Printing statements.
# print(f'Salaries = {salaries}\n')
# print(f'Salaries after 10% tax deduction = {salaries}\n')
# print(f'Highest final salary = {highest_final_salary}\nLowest final salary = {lowest_final_salary}\n')
# print(f'Average final salary = {average_final_salary}\n')



# ========================================================================
# ========================== E N D ============================================
# ========================================================================

'''


