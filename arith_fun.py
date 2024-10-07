def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result_add = add(num1, num2)
print("Addition:", result_add)

result_subtract = subtract(num1, num2)
print("Subtraction:", result_subtract)

result_multiply = multiply(num1, num2)
print("Multiplication:", result_multiply)

result_divide = divide(num1, num2)
print("Division:", result_divide)