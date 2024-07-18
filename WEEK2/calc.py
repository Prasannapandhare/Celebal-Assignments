def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(num1, "/", num2, "=", num1/num2)

print("=-=-=-=-=-=--=-=-=-=")
print(" Simple Calculator")
print("=-=-=-=-=-=--=-=-=-=")
print("Please select operation -\n" 
        "1. Addition\n" 
        "2. Subtraction\n" 
        "3. Multiplication\n" 
        "4. Division\n")

select = int(input("Select operations from 1, 2, 3, 4: "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if select == 1:
    print(num1, "+", num2, "=", add(num1, num2))

elif select == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))

elif select == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))

elif select == 4:
    divide(num1, num2)
else:
    print("Invalid input")
