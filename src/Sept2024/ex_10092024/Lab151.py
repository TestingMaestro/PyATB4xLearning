# handling the exception
# 1. Using Single try and except

try:
    a = 10
    b = 0
    c = a / b
except ZeroDivisionError as e:
    print(e)
    print("Please check your inputs, it shouldn't be string or zero")
else:
    print(f"Result:{c}")




