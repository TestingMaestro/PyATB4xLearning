# 5 Nested try with except

import math

try:
    try:
        math.exp(1000)  # OverflowError: math range error
    except AttributeError as e:
        print(e, "Exception is caught in inner block")
except Exception as e:
    print(type(e))
    print("Exception caught in Outer block")

