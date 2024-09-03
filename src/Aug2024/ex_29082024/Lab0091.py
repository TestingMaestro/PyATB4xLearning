# List Methods

my_list1 = [21, 22, 23, 24, 25, 26]
my_list2 = ["Bread", "Butter", "Cheese", "Milk"]

# print(my_list1)
# print(my_list2)

# 1. append(str) ---> Adds the element at the end of the list
#  append() takes single argument only

my_list2.append("Butter")
my_list2.append("Banana")
my_list2.append("Sauce")
my_list1.append(27)

print(my_list1)
print(my_list2)

# 2. Extend() ---> Adds the element(s) at the end of the list
# It can take multiple or single argument
# Square brackets tells tha we want to extend the original list with this ite, ex: 28


my_list1.extend([28])

my_list1.extend([29, 30, 31, 32])

# 3 insert() --->
print(my_list1)

my_list1.insert(-1, "Yashodhar")
print(my_list1)
