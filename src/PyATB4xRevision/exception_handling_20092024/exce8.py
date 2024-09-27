# try - except, else and finally

try:
    a = int(input("Enter 1st number"))
    b = int(input("Enter 2nd number"))
    c = a / b
except (ValueError, ZeroDivisionError) as ve:
    print("Number cannot be strings or divided by zero")
else:
    print(f"Division:{c}")

finally:
    print("Exception occurs or not , Finally block will be executed")
