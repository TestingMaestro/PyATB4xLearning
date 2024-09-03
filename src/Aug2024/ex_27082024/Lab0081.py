# Decorators chaining

def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()  # Call the original function

    return wrapper  # Return the wrapper function itself


def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()  # Call the original function

    return wrapper  # Return the wrapper function itself


@decorator1  # Apply decorator1 to the result of decorator2
@decorator2  # Apply decorator2 to say_hello
def say_hello():
    print("Hello!, There")


# Now, call the decorated function
say_hello()
