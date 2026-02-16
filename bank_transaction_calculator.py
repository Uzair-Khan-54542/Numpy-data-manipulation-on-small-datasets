import numpy as np 

# 8. Bank transaction calculator.
'''
# ========================================================================
# ========================== S T A R T ============================================
# ========================================================================




transactions = np.array([500, -200, 1200, -450, 300, -150, 700, -500, 900, -250, 400, -100, 650, -300, 1000])



# ========================================================================
# Final account balance.
final_account_balance = transactions.sum()


# ========================================================================
# Largest deposit.
largest_deposit = np.max(transactions)


# ========================================================================
# Largest withdrawl.
withdrawls = transactions[transactions < 0]
largest_withdrawl = np.min(withdrawls)


# ========================================================================
# counting total number of deposists and withdrawls.
total_transactions = len(transactions)
deposists = transactions[transactions > 0]
total_deposited_transactions = len(deposists)
total_withdrawn_transactions = len(withdrawls)


# ========================================================================
# Adding 2% interest rate to final balance.
interest_fee = final_account_balance * (2 / 100)




# ========================================================================
# Printing statements.
# print(f'Final transaction balance = {final_account_balance}\n')
# print(f'largest deposit = {largest_deposit}\n')
# print(f'largest withdrawl = {largest_withdrawl}\n')

# print(f'Total Transactions = {total_transactions}\nDeposited Trasnactions = {total_deposited_transactions}\nWithdrawn Transactions = {total_withdrawn_transactions}\n')
# print(f'Interest fee on final balance = {interest_fee}\n')


# ========================================================================
# ========================== E N D ============================================
# ========================================================================

'''





