# Calculator in python
# prompt: build a calculator which takes input from the user, beside basic functionality include modulus, floor division, Exponentiation

def calculator():
    """
    A calculator function that takes user input for numbers and operations,
    including modulus, floor division, and exponentiation.
    """
    while True:
        operation = input("Enter the operation (+, -, *, /, %, //, ** or 'q' to quit): ")
        if operation == 'q':
            break

        if operation not in ('+', '-', '*', '/', '%', '//', '**'):
            print('❌ Invalid operator! Try again.')
            continue

        try:
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
        except ValueError:
            print("❌ Invalid input. Please enter valid numbers.")
            continue

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("🚫 Error: Division by zero.")
                continue
        elif operation == '%':
            result = num1 % num2
        elif operation == '**':
            result = num1 ** num2
        elif operation == '//':
            if num2 != 0:
                result = num1 // num2
            else:
                print("🚫 Error: Division by zero.")
                continue
  
        print(f"✅ Result: {result}")
   
calculator()