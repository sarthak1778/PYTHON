'''Exercise 1 ->>>>>>>>>>>>
Create a calculator capable of performing:
1. Addition 
2. Subtraction
3. Multiplication
4. Division
5. Remainder
6. FOR division two decimal places correction 
7. Log function
8. Exponential Function 
9. Continues loop of user to be given *
10. Percentage of a number  
operations on two numbers.
Your program should format the output in a readable manner!'''

# Daily Life Style Calculator

import math

def calculator():
    print("--- 🧮 Advanced Command-Line Calculator ---")
    
    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Remainder (%)")
        print("6. Logarithm (log base x of y)")
        print("7. Exponential (x^y)")
        print("8. Percentage (x% of y)")
        print("9. Exit")

        choice = input("\nEnter choice (1-9): ")

        if choice == '9':
            print("Exiting... Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):
            try:
                num1 = float(input("Enter first number (x): "))
                num2 = float(input("Enter second number (y): "))

                if choice == '1':
                    result = num1 + num2
                    print(f"\n> Result: {num1} + {num2} = {result}")

                elif choice == '2':
                    result = num1 - num2
                    print(f"\n> Result: {num1} - {num2} = {result}")

                elif choice == '3':
                    result = num1 * num2
                    print(f"\n> Result: {num1} * {num2} = {result}")

                elif choice == '4':
                    if num2 == 0:
                        print("\nError: Division by zero is undefined.")
                    else:
                        result = num1 / num2
                        # Two decimal places correction as requested
                        print(f"\n> Result: {num1} / {num2} = {result:.2f}")

                elif choice == '5':
                    result = num1 % num2
                    print(f"\n> Result: Remainder of {num1} / {num2} = {result}")

                elif choice == '6':
                    if num1 <= 0 or num2 <= 0 or num2 == 1:
                        print("\nError: Logarithm arguments must be positive and base cannot be 1.")
                    else:
                        result = math.log(num1, num2)
                        print(f"\n> Result: log base {num2} of {num1} = {result:.4f}")

                elif choice == '7':
                    result = math.pow(num1, num2)
                    print(f"\n> Result: {num1} raised to the power of {num2} = {result}")

                elif choice == '8':
                    result = (num1 / 100) * num2
                    print(f"\n> Result: {num1}% of {num2} = {result}")

            except ValueError:
                print("\nInvalid input! Please enter numerical values.")
        else:
            print("\nInvalid selection. Please choose a number between 1 and 9.")

        print("-" * 30)

if __name__ == "__main__":
    calculator()