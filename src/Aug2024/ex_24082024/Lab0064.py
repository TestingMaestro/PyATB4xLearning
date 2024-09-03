# Types of User defined functions

"""

1. Function without return [Doesn't return anything]
2. Function with Return [They Return something]
3. Function without arguments or parameters
4. Functions with arguments or parameters

"""


# 1. Function without return [Doesn't return anything]
# or No Return Type and No arguments

def greet():
    print("1. No Return Type and No arguments")


print(greet())


# 2 No return Type with arguments

def user_email(email, name):
    print("Name:", name)
    print("Email:", email)


user_email("yk@gmail.com", "Yash")


# 3 No return Type with default argument

def default_arg(name="Yash"):  # default arg name  = Yash
    print("Hello", name)


default_arg("Sou")  # ----> name will be replaced with Hello Sou
default_arg()  # ------------> Default name will be printed that is, Hello Yash
default_arg(name="Yashu")  # ----> Positional Argument


# Multiple Arguments

def multiple_args(name1="Yash", name2="Sou", name3="Boss"):
    print("Multiple args:", name1, name2, name3, sep=" | ")


multiple_args(name1="Aravind", name2="Prema", name3="Minni")
multiple_args()
multiple_args(name2="Santu")
multiple_args("Soma", name3="Vinod")

print("\n")


# 4. Argument and Return Type

def sum_of_two_numbers(num1, num2):
    return num1 + num2


def sum_of_two_numbers_with_default(num1=10, num2=10):
    return num1 + num2


res1 = sum_of_two_numbers(10, 20)
res2 = sum_of_two_numbers(num1=40, num2=30)
res3 = sum_of_two_numbers_with_default()
res4 = sum_of_two_numbers_with_default(num2=100)

print(res1, res2, res3, res4, sep=" -- ")
