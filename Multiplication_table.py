def generate_multiplication_table():
  while True:
    try:
      number = int(input("Enter the number for the multiplication table: "))
      limit = int(input("Enter the limit up to which you want the table generated: "))
      if limit <= 0:
        print("Limit must be a positive integer. Please try again.")
      else:
        break
    except ValueError:
      print("Invalid input. Please enter integers only.")
  print(f"Multiplication Table for {number}")
  for i in range(1, limit + 1):
    product = number * i
    print(f"{number} x {i} = {product}")
generate_multiplication_table()
