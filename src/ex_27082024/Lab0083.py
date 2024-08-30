# before knowing decorators we must know below things


# 1.
def shout(text):
    return text.upper()


print(shout("Hello"))

yell = shout

print(yell("hello"))


# 2 In the below  example, the greet function takes another function as a parameter (shout and whisper in this case).
# The function passed as an argument is then called inside the function greet.

def shout(text):
    return text.upper()


def whisper(text):
    return text.upper()


def greet(func):
    greeting = func("I'm created by a function passed as an argument")
    print(greeting)


greet(whisper)
greet(shout)


def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(add_15(30))
