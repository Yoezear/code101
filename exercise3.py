from queue import Queue
patient_list=Queue()
current_list=None
while True:
    print("Desk Manager - Patient registration and appointment system")
    print("""1. Register patient
          2. Remove patient after meeting doctor
          3. Display patient list
          4. Exit""")
    selection= int(input("Enter your choice from (1-4): "))

    if selection == 1 :
        name=input("Please enter the name of the patient: ")
        patient_list.put(name)
        current_list=name
        print(f"current_list: {name}Patient is registered")
        
    
    elif selection == 2 :
        patient_list.get()
        print(f"current_list: {current_list} Patient removed successfully from the queue after meeting doctor.")

    
    elif selection == 3 :
        for i in patient_list.queue:
            print(i)

    
    elif selection == 4 :
        print("Exiting the program..")
        break
    
    
    else:
        print("Invaild information.")
print("Thank you.!!!")
