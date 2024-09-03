import math

num = 10


def give_me_power(num):
    return math.pow(num, 2)


op = give_me_power(num)
print(op)

# Lambda Expression
op2 = lambda : math.pow(int(input("Enter the number\n")), 2)
print(f"{op2():.0f}")
