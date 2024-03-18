num_students=int(input("Enetr the numbers of the students: "))
i = 1
while i<= num_students:
    total_grade=0
    num_subjects=int(input("Enter the number of subjects for student {1}: "))

    for j in range(1, num_subjects + 1):
        garde=float(input("Enter subject {j} garde for student {1}: "))
        total_grade += garde

    average_garde= total_grade / num_subjects
    print(f"Average grade for student {i}: {average_garde: .2f}")
    i += 1