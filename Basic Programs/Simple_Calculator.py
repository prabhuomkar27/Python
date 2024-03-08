# Simple calculator

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y!=0:
        return x/y
    else:
        return "Cannot divide by zero"

# Get user input

num1 = float(input("Enter the first number : "))
operator = input("Enter the operation : ")
num2 = float(input("Enter the second number : "))

# Perform calculations based on user input

if operator == '+':
    result = add(num1,num2)
elif operator == '-':
    result = subtract(num1,num2)
elif operator == '*':
    result = multiply(num1, num2)
elif operator == '/':
    result = divide(num1,num2)
else:
    result="Invalid operator"

# Display the result

print("Result:",result)
