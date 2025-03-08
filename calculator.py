# Simple Calculator in Python

# Function to perform calculation
def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Choose operation (+, -, *, /): ")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error! Division by zero.")
            return
    else:
        print("Invalid operator!")
        return

    print("Result:", result)

# Run the calculator function
calculator()
