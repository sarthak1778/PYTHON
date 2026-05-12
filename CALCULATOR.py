'''Exercise 1 ->>>>>>>>>>>>
Create a calculator capable of performing:
1. Addition 
2. Subtraction
3. Multiplication
4. Division
operations on two numbers.
Your program should format the output in a readable manner!'''

# Daily Life Style Calculator

print("=========== CALCULATOR ===========")

while True:

    # Taking input
    num1 = float(input("\nEnter first number: "))
    operator = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Calculations
    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"

    else:
        result = "Invalid Operator"

    # Display result
    print("\n==============================")
    print("Result =", result)
    print("==============================")

    # Continue or exit
    choice = input("\nDo you want another calculation? (yes/no): ")

    if choice.lower() != "yes":
        print("\nCalculator Closed.")
        break