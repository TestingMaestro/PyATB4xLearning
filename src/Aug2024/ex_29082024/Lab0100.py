shopping_list_f_wife = ["Bread", "Butter", "paneer"]

# she told instead of paneer, bring milk

shopping_list_f_wife[2] = "Milk"
print(shopping_list_f_wife)

# Real world project where,
"""
the domains - thetestingacademy.com , sdet.live
these domains wont change forever
We can use tuple in this case
"""

my_tuple = ("tta.com", "sdet.live", "sdet.live")
my_tuple1 = ("google.com", "app.erasor.io")
my_tuple3 = my_tuple + my_tuple1
print(my_tuple3)

# Taking user input
# while adding elements to the tuple we dont have any methods or assigment is not possible
# so fist we add the element to the list then convert it to tuple

n = int(input("Enter the elements \n"))
shopping_list_f_wife = []
for i in range(n):
    element = input(f"Enter the element at {i} the index\n")
    shopping_list_f_wife.append(element)
my_tuple = tuple(shopping_list_f_wife)
print(my_tuple)
