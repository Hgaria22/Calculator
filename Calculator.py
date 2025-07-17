

operator = input("Enter an operator (+ - * /): ")
# To choose an operator for your calculation
num1 = float(input("Choose your first number: "))
num2 = float(input("Choose your second number: "))
#Choose two numbers to use the operator and find out the result

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
#To tell user any random character isn't a valid operator

