# 3. Handling Multiple specific exceptions

try:
    a = int(input("Enter a number a"))
    b = int(input("Enter a number b"))
    c = (a / b) + "Yash"
except (ZeroDivisionError, ValueError, TypeError) as e:
    print("Entered value cannot be zero or Strings other types!! Please check the Inputs")
else:
    print(f"Result: {c:.2f}")
