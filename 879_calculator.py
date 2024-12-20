# Define calculator functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    # Throw an error if second value is 0.
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by 0.")


while True:
    operationName = ""
    value = 0
    print("Enter two numbers.")

    # Throw an error and exit loop if input is not numerical
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
    except ValueError:
        print("Error: Only numbers allowed.")
        break

    print("Select the operation to be done: \n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division")
    operation = str(input())
    
    if operation == "1" :
        value = add(num1, num2)
        operationName = "sum"
    elif operation == "2":
        value = sub(num1, num2)
        operationName = "difference"
    elif operation == "3":
        value = mul(num1, num2)
        operationName = "product"
    elif operation == "4":
        value = div(num1, num2)
        operationName = "quotient"
    else:
        print("Input is invalid. Try again.")
    print(f"Your {operationName} is {value}.")

    option = input("Enter 'y' to exit: ").lower()
    if option == 'y' :
        break