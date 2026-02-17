
import numpy as np 


#2. Monthly Expense Tracker
'''
# ========================================================================
# ========================== S T A R T ============================================
# ========================================================================



import numpy as np

# Column array: 12 rows (one per month)
expenses = np.array([
    [1200],
    [1350],
    [1100],
    [1400],
    [1500],
    [1600],
    [1700],
    [1550],
    [1450],
    [1300],
    [1250],
    [1380]
])


# ========================================================================
# Calculating total yearly expense.
yearly_expense = expenses.sum()


# ========================================================================
# Calculating monthly average expense.
monthly_average = round(np.mean(expenses), 2)


# ========================================================================
# Finding the highest and lowest monthly expense.
highest_expense = np.max(expenses)
lowest_expense = np.min(expenses)


# ========================================================================
# Finding the index/month with the highest expense.
idx = np.where(expenses == highest_expense)[0]


# ========================================================================
# Reducing all expenses by 10 %.
reduced_expenses = expenses * 0.9
print(reduced_expenses, '\n')



# ========================================================================
# Comparing yearly expenses before and after 10% reduction.
yearly_expense_after_reduction = reduced_expenses.sum()
savings = yearly_expense - yearly_expense_after_reduction

print(f'Expense before 10% reduction = {yearly_expense}\nExpense after 10% reduction = {int(yearly_expense_after_reduction)}\n')

print(f'Total Savigs per year after 10% deduction = {savings}\n')



# ========================================================================
# Printing statements.
# print(f'Yearly expense = {yearly_expense}\n')
# print(f'Monthly average = {monthly_average}\n')
# print(f'Highest monthly expense = {highest_expense}\nLowest monthly expense = {lowest_expense}\n')
# print(f'Month with highest expense = {idx + 1}\n')





# ========================================================================
# ========================== E N D ============================================
# ========================================================================

'''

