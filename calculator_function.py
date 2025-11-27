def aliza():
    print("=== Calculator ===")

    # Taking first number
    num1 = (input("Enter first number: "))
    while not num1.isdigit():
        print("Invalid input! Please enter a valid number.")
        num1 = (input("Enter first number: "))
    num1 = float(num1)

    # Taking second number
    num2 = input("Enter second number: ")
    while not num2.isdigit():
        print("Invalid input! Please enter a valid number.")
        num2 = input("Enter second number: ")
    num2 = float(num2)

    # Taking operator input
    op = input("Enter operator (+, -, *, /): ")
    while op not in ['+', '-', '*', '/']:
        print("Invalid operator! Try again.")
        op = input("Enter operator (+, -, *, /): ")

    # Calculations
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            result = "Error! Cannot divide by zero."
        else:
            result = num1 / num2

    print("Result:", result)



aliza()
