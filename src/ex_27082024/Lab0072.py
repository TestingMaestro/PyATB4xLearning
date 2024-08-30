#  Function Scope
# Local Variable scope is from beginning of function till the end of function
# Scop of Global variable is from beginning of the function till the end of the function

global_b = 70


def function_scope():
    a = 10
    print(a)  # Local Variable
    print(global_b)


print(global_b)


def function_scope1():
    a = 10
    print(a)  # Local Variable
    print(global_b)  # Global variable


# print(a)  # Outside the function
function_scope()
function_scope1()
