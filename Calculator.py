# This function adds two numbers
def addition(a, b):
    return a + b

# This function subtracts two numbers
def subtract(a, b):
    return a - b

# This function multiplies two numbers
def multiply(a, b):
    return a * b

# This function divides two numbers
def divide(a, b):
    return a / b


print("***Calculator Program***")
while True:
    # take input from the user
    choice = input("Enter your choice:\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(x, "+", y, "=", addition(x, y))

        elif choice == '2':
            print(x, "-", y, "=", subtract(x, y))

        elif choice == '3':
            print(x, "*", y, "=", multiply(x, y))

        elif choice == '4':
            print(x, "/", y, "=", divide(x, y))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_choice = input("Let's do next calculation? (yes/no): ")
        if next_choice == "no":
          break
    else:
        print("Invalid Input")
