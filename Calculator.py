
while True:
    #This part of the code makes sure the calculator is repeating everytime
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
        #This line tells use you can't use any random character as an operator in this calculator you can only add, subtract, multiply and divide

    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() != 'yes':
        print("Goodbye!")
        break
