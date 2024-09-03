my_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# Syntax ---> my_tuple [start:stop:step]

# To get elements from index 1 to 4:

ele = my_tuple[1:9]
print(ele)

#  To get all elements from the beginning up to index 4
ele = my_tuple[:5]
print(ele)

# To get all elements from index 5 to the end:
ele = my_tuple[:5]
print(ele)

# To get elements from the third-to-last to the last:
ele = my_tuple[3:]
print(ele)

# To get elements from the beginning up to the third-to-last:
ele = my_tuple[:-3]
print(ele)

#  To get every second element in the list:
ele = my_tuple[2::2]
print(ele)

# to get every second element, starting from index 1
ele = my_tuple[1::2]
print(ele)

#  Reverse the list
ele = my_tuple[::-1]
print(ele)

# To get every second element in reverse order:
ele = my_tuple[-1::-2]
print(ele)
