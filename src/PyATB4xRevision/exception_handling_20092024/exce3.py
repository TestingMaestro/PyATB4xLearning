# Multiple except [handling exceptions separately]
try:
    a = int(input("Enter 1st number"))
    b = int(input("Enter 2nd number"))
    c = a / b
except ValueError as ve:
    print("Only integers are allowed ")
except ZeroDivisionError as ze:
    print("A number cannot be divided by zero")
