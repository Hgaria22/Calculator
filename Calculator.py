

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Choose your first number: "))
num2 = float(input("Choose your second number: "))


if operator == '+':
    print(float(num1 + num2))
elif operator == '-':             
    print(float(num1 - num2))
elif operator == '*':
    print(float(num1 * num2))
elif operator == '/':
    if num2 == 0:
        print("Cannot divide by 0")
    else:
        print(float(num1 / num2))
else:
    print(f"{operator} isn't a valid operator")

