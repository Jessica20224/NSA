# Function to perform addition
def addition(x, y):
    return x + y

# Function to perform subtraction
def subtraction(x, y):
    return x - y

# Function to perform multiplication
def multiplication(x, y):
    return x * y

# Function to perform division
def division(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Function to calculate remainder
def remainder(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x % y

# Main calculator loop
while True:
    # Input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Ask the user which operation to perform
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Remainder")
    print("6. Quit")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice == '1':
        print("Result: ", addition(num1, num2))
    elif choice == '2':
        print("Result: ", subtraction(num1, num2))
    elif choice == '3':
        print("Result: ", multiplication(num1, num2))
    elif choice == '4':
        print("Result: ", division(num1, num2))
    elif choice == '5':
        print("Result: ", remainder(num1, num2))
    elif choice == '6':
        break
    else:
        print("Please choose a valid operation.")
