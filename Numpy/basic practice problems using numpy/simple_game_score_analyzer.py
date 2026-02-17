import numpy as np 

# 7. Simple game score analyzer.
'''
# ========================================================================
# ========================== S T A R T ============================================
# ========================================================================




scores = np.array([78, 92, 35, 88, 49, 73, 90, 81, 69, 95])



# ========================================================================
# Sorting scores in ascending order.
scores.sort()

print(f'Original scores = {scores}\n')


# ========================================================================
# Extracting top 3 highest scores.
top_3_scores = np.array(scores[10:6:-1])



# ========================================================================
# Counting players who passed (scored >= 50)
passed_players = (scores >= 50).sum()



# ========================================================================
# Replacing all scores < 50 with '50'.
scores[scores < 50] = 50


# ========================================================================
# Average score after modifications.
average_score = np.mean(scores)


# ========================================================================
# Printing statements.
print(f'Passed players = {passed_players} out of {len(scores)}\n')
print(f'Scores after replacing (score < 50) with 50 = {scores}\n')
print(f'Top 3 scores = {top_3_scores}\n')
print(f'Average score after modification = {average_score}\n')




# ========================================================================
# ========================== E N D ============================================
# ========================================================================

'''






