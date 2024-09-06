# Encapsulation
# Biding wrapping the data members within the class using private access specifiers and using methods only
# Parent  class securing its attributes using access specifiers and by using methods only

my_tuple = (1, 2, 3, 4, 5)

# tuple to set
my_set = set(my_tuple)
my_set.update({10, 20, 30, 40, 50})
my_tuple1 = tuple(my_set)
print(my_tuple1)

# tuple to list
my_list = list(my_tuple)
my_list.extend([6, 7, 8, 9, 0])
my_tuple2 = tuple(my_list)
