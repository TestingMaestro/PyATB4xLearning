# Slicing---> Fully works with indices

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Syntax ---> my_list[start:stop:step]

# To get elements from index 1 to 4:
print(my_list[1:5])

#  To get all elements from the beginning up to index 4

print(my_list[:5])

# To get all elements from index 5 to the end:
print(my_list[5:])

# To get elements from the third-to-last to the last:

print(my_list[-3:])

# To get elements from the beginning up to the third-to-last:

print(my_list[:-3])

#  To get every second element in the list:

sub_list = my_list[::2]
print(sub_list)

# to get every second element, starting from index 1

sub_list = my_list[1::2]
print(sub_list)

#  Reverse the list
sub_list = my_list[::-1]
print(sub_list)

# To get every second element in reverse order:

sub_list = my_list[::-2]
print(sub_list)
