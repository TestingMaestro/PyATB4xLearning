# Higher Order Functions
# A function that takes another function as an argument and calls inside
# Define basic mathematical operations

# a = float(input("Enter the number 1\n"))
# b = float(input("Enter the number 2\n"))


def add(a, b):
    return a + b


def subtract(a, b):
    return b - a


def division(a, b):
    if b != 0:
        return a / b
    else:
        print("cannot divide by zero")


def modulo_op(a, b):
    return a % b


def multiply(a, b):
    return a * b


def maths_operation(func):
    return func(10, 20)


print(maths_operation(add))
print(maths_operation(subtract))
print(maths_operation(division))
print(maths_operation(multiply))
print(maths_operation(modulo_op))
