
import numpy as np 



# 4. Sales Data Calculator
'''
# ========================================================================
# ========================== S T A R T ============================================
# ========================================================================



# 7 days × 3 products sales or quantities (prod_1, prod_2, prod_3, revenue(Rupees))
data = np.array([
    [10, 15, 20, 20000],
    [12, 18, 22, 30000],
    [14, 17, 19, 10000],
    [11, 16, 21, 22000],
    [13, 15, 20, 25000],
    [12, 18, 23, 31000],
    [15, 17, 22, 16000]
])



# ========================================================================
# Calculating total sales per day.
total_sales_per_day = []

for i in range(0, 7):

    total_sales_per_day.append(data[i, 0:3].sum())

total_sales_per_day = np.array(total_sales_per_day)



# ========================================================================
# Calculating total sales per product.

total_sales_per_product = []

for i in range(0, 3):

    total_sales_per_product.append(data[0:7, i].sum())

total_sales_per_product = np.array(total_sales_per_product)


# ========================================================================
# Best selling day.
best_day = np.max(total_sales_per_day)
day = np.where(total_sales_per_day == best_day)[0]



# ========================================================================
# Best selling product.
best_product = np.max(total_sales_per_product)
product = np.where(total_sales_per_product == best_product)[0]


# ========================================================================
# Applying 10% discount to revenue of each day.
discounted_revenue = data[:, 3] * 0.9


# ========================================================================
# Checking total revenue difference after discount.
before_discount_revenue = data[:, 3].sum()
after_discount_revenue = discounted_revenue.sum()

difference = before_discount_revenue - after_discount_revenue





# ========================================================================
# Printing statements.

# print(total_sales_per_day, '\n')
# print(total_sales_per_product, '\n')
# print(f'Day with best selling = {day + 1}\n')
# print(f'Best selling product = {product + 1}\n')
# print(data, '\n')
# print(discounted_revenue, '\n')
# print(f'Net-Revenue before discount = {before_discount_revenue}\nNet-Revenue after discount = {after_discount_revenue}\nDifference in Net-Revenue after discount = {difference}\n')






# ========================================================================
# ========================== E N D ============================================
# ========================================================================

'''








