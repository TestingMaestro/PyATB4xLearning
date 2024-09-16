# 4. Ex: 2 --> General Catch [Catching all Exceptions]
import math

try:
    math.exp(1000)  # OverflowError: math range error
except Exception as e:
    print(type(e))
    print("Use Lower value for exponential types")
