# Using the parent exception class if we exacty dont know the exception or we can have a custom exception
import math

try:
    a = float(input("Enter 1st number"))
    b = float(input("Enter 2nd number"))
    c = a / b
except Exception as ve:
    print("Number cannot be strings or divided by zero")
else:
    print(f"{c:.2f}")


