#  Conversion

# list to tuple

my_list = ["Yash", "Sou", "Minni", "Pappa", "Mummy", "Kushinu"]

my_tuple = tuple(my_list)
print(my_tuple)

# if we want to reassign the original value then convert to list then convert to tuple

# tuple to list
my_list1 = list(my_tuple)
my_list1[2] = "Munni"
print(my_list1)
my_list1.append("Bhava")
print(my_list1)
my_tuple = tuple(my_list1)
print(my_tuple)

# Replication----> new_tuple = original_tuple *n

# Prints entire tuple 3 times
my_new_tuple = my_tuple * 3
print(my_new_tuple)

my_new_tuple = (0,) * 5
print(my_new_tuple)

my_new_tuple = ("A", "B")
print(my_new_tuple * 3)

my_new_tuple = ("A",)
print(my_new_tuple * 3)
