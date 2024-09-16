# 6. try, except and finally
try:
    a = int(input("Enter a number a"))
    b = int(input("Enter a number b"))
    c = a / b
except Exception as e:
    print(type(e))
    print("Please check the inputs")
else:
    print(f"Result is: {c}")
finally:
    print("I'm always executed")
