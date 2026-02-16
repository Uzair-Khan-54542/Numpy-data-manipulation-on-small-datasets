
import numpy as np 




# 1. Student Marks Analyzer
'''
# ========================================================================
# ========================== S T A R T ============================================
# ========================================================================



names = np.array([
    "Ali", "Sara", "Usman", "Ayesha", "Bilal",
    "Hina", "Ahmed", "Zara", "Hamza", "Noor"
])

# Marks = Maths, Science, Computer

marks = np.array([
    [78, 85, 88],
    [92, 90, 94],
    [67, 72, 70],
    [81, 79, 84],
    [74, 69, 73],
    [89, 91, 93],
    [60, 65, 62],
    [83, 87, 85],
    [95, 93, 96],
    [70, 75, 78]
])

student_data = np.column_stack((names, marks))

average_per_student = []

#=============================================================
# Calculating Average of each student in the class.
for i in range(len(marks)):

    avg = np.mean(marks[i, 1:4])
    average_per_student.append(avg)

average_per_student = np.array(average_per_student)


#=============================================================
# Calculating Average of the whole class.
average_of_class = np.mean(marks[0:10, 1:4])


#=============================================================
# Fiding the maximum and the minimum marks in the whole class.
maximum = np.max(marks[0:10, 0:3])
minimum = np.min(marks[0:10, 0:3])


#=============================================================
# Finding students whose average is greater than whole class's average.
above_class_avg_students = student_data[average_per_student > average_of_class]


#=============================================================
# Increment all marks by 5.
marks[0:10, 0:3] += 5


#=============================================================
# Validating marks to stay inside 100 range after increment.
idx = np.where(marks > 100)
marks[idx] = 100


#=============================================================
# Result printing.
# print(f'Average per Student = {average_per_student}, \n')
# print(f'Average of Class = {average_of_class}, \n')
# print(f'Maximum marks = {maximum}\nMinimum marks = {minimum}\n')
# print(f'Students with average > whole class average = \n{above_class_avg_students}\n')




# ========================================================================
# ========================== E N D ============================================
# ========================================================================
'''