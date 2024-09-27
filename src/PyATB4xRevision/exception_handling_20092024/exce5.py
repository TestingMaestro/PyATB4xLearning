# handling try-except with else block

try:
    a = int(input("Enter 1st number"))
    b = int(input("Enter 2nd number"))
    c = a / b
except (ValueError, ZeroDivisionError) as ve:
    print("Number cannot be strings or divided by zero")
else:
    print(f"Division:{c}")