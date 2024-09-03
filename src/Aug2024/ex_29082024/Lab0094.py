my_list = ["Yash", "Sou", "Minni", "Pappa", "Mummy", "Kushinu"]

print(my_list.count("Gombi"))

my_list.sort(key=len, reverse=False)
print(my_list)

# for i in my_list:
#     print(i.upper())

for i in range(len(my_list)):
    print(my_list[i - 1])
    # if my_list[i] == "Gombi":
    #     print(my_list.reverse())
    # print(f"Element at index {i}: {my_list[i]}")
    # print(str(my_list[-1]))
# my_list.reverse()
# print(my_list)


# Joining 2 lists [Concatenation]

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = list_1 + list_2
print(list_3)

# Sorting in descending order

# type 1

list_3.reverse()
print(list_3)

# type 2

my_list1 = [0, 10, 20, 200, 30, 50, 60, 70, 80, 90, 99]
my_list1.sort(reverse=True)
print(my_list1)
