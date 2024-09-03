# Lambda Expressions [Lambda Function]
import math


# syntax---> lamda parameters: expression

def multiple(num):
    return math.pow(num, 3)


o = multiple(5)
print(o)

# Write above using lamda expression

o = lambda num: math.pow(num, 3)
print(o(5))
