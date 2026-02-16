import numpy as np 

# 5. Sales Data Calculator
'''
# ========================================================================
# ========================== S T A R T ============================================
# ========================================================================




# 5 students × 10 days attendance (1 = Present, 0 = Absent)
attendance = np.array([
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 0]
])



# ========================================================================
# Attendance percentage per student.
student_attendance_percentage = []

for i in range(0, 5):

    s = attendance[i, :].sum()
    percentage = (s / 10) * 100
    student_attendance_percentage.append(percentage)

student_attendance_percentage = np.array(student_attendance_percentage)


# ========================================================================
# Attendance percentage of the entire class.
s = attendance[:, :].sum()
attendance_percentage_of_whole_class = (s / 50) * 100



# ========================================================================
# Students with attendance below 75%.
below_75_percentage_students = np.where(student_attendance_percentage < 75)[0]


# ========================================================================
# Counting total absences per student.
absences_per_student = []
for i in range(0, 5):

    s = 0

    for j in range(0, 10):

        if attendance[i, j] == 0:

            s += 1
        
        else:
            pass 

    absences_per_student.append(s)

absences_per_student = np.array(absences_per_student)




# ========================================================================
# Printing statements.
# print(f'{student_attendance_percentage}% \n')
# print(f'{attendance_percentage_of_whole_class}% \n')
# print(f'Students with percentage < 75 are: {below_75_percentage_students}\n')
# print(f'{absences_per_student} \n')



# ========================================================================
# ========================== E N D ============================================
# ========================================================================

'''








