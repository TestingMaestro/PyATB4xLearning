# def mult_args(name, age, gender):
#     print(name, age, gender)
#
#
# mult_args("Yash", 30, "Male")
#
#
def print_args(*args):
    print(len(args))
    # for i in args:
    #     print(i, end=" ")


print_args()
print_args("Milk", "Bread", "Boobs", "Sou", 123, 3.142, True)


# default args

def default_args(name="Yash", age=20, place="Udupi"):
    print(f"{name}, {age}, {place}")


default_args(name="Yash")
default_args(place="Kundapura", name="Soup")
default_args()


def with_return_type(name, place):
    return name+place.upper()


res = with_return_type("Yash ", "Kundapura")
print(res)
