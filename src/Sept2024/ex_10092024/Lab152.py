# 2. Using Single try and multiple except

try:
    a = int(input("Enter a number a"))
    b = int(input("Enter a number b"))
    c = a / b
except ZeroDivisionError as e:
    print("Entered value cannot be zero!! Please check the Inputs")
except ValueError as e:
    print("Entered value cannot be String!! Please check the Inputs")
else:
    print(f"Result: {c:.2f}")
