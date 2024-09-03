#  Multiple arguments with no limit------->*args

def print_arguments(*args):  # *args -> is a list
    for i in args:
        print(i)


print_arguments("Pramod", "Lucky", "Yash", "Sou")
# print_arguments("Lucky", "Yash", "Sou")
# print_arguments("Yash", "Lucky")
print_arguments("Sou", 3.14, 60, True)

my_fruits = ["Mango", "Orange", "Banana", "Jack Fruit", "Dragon Fruit"]


def fruits(check_fruits):
    for i in my_fruits:
        print(i, end=" ")


fruits(my_fruits)
