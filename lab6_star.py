rows = int(input("Enter the number of rows for the triangle: "))
for i in range(rows):
    for j in range(i + 1):  
        print("*", end="")  
    print()  