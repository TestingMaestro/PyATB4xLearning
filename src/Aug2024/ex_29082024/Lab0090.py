# List is a collection of items which,
"""
1. Allows duplicates
2. Allows you to add homogeneous and heterogeneous type of data
3. Items are generally ordered  [but we van change the order using some list functions]
4. Items are Changeable [ we can add, change/update/ and remove items in the list]

"""

# my_list = ["Bread", "Butter", "Cheese", "Milk"]
# my_list2 = [21, 33.32, "Cheese", "Milk"]
#
# # Accessing Elements on by one
#
# # First Element [indexing]
# print("Element at index 0", my_list[0])
#
# # Slicing
# print("Accessing multiple elements", my_list2[1:3])
#
# # print(my_list[1])
# # print(my_list[2])
# # print(my_list[3])
#
# # Last Element
# print(my_list[-1])
#
# # Accessing all elements using for loop
# for items in my_list:
#     print(f"{items}")
#
# # Length
#
# print(len(my_list))
#
# # Index Error
# # print(my_list[4])
#
# # re initialize/change the value
# my_list[0] = "Banana"
#
# # Duplicates are allowed
# my_list[1] = "Bun"
# my_list[2] = "Bun"
#
# # Assigning/changing different type of value to the list
# my_list2[-1] = True
# print(my_list)
# print(my_list2)
num = int(input("Enter the elements would you like to add to the list\n"))
my_list = []
for i in range(num):
    element = input(f"Enter element {i}: ")
    my_list.append(element)
print(my_list)
