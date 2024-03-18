print("""Welcome Everyone
Please provide the mention details:""")
def is_eligible_for_discount(age , student_info):
    return (age <= 12) or ((13 <= age <= 18) and student_info.lower() == "yes")

age = int(input("Enter your age: "))
student_info = input("are you a student? (yes/no): ")
if is_eligible_for_discount (age, student_info):
    print("You are eligible for a discount")
else:
    print("You are not eligible for a discount")
print("sorry")