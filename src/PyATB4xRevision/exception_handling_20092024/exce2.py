# single try - except block
try:
    a = int(input("Enter the number"))
    b = a / 0
except ZeroDivisionError as ze:
    print(ze)
