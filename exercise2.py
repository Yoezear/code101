print(" Welcome to Student Information Management System")
student_list=[]
student_dict={}
name=input("Please enter your name: ")
age=int(input("Enter your age: "))
grade=int(input("Enetr your grade: "))
student_list.append(name)
student_dict[age,grade]=name
print("Student information added successfully")
print(student_dict.items())
search_name= input("Enter the name of the student to serach or simply enter to skip: ")
if search_name in student_list:
    info= student_dict[search_name]
    print(f"Name: {search_name}, age: {info['age']}, garde: {info['grade']}")
else:
    print("Student details not found...")
remove_name=input("Enter the anme of the student to remove or simply enter to skip: ")
if remove_name in student_list:
    del student_dict[remove_name]
    student_list.remove(remove_name)
    print("student remove successfully....")
else:
    print("student not found..")