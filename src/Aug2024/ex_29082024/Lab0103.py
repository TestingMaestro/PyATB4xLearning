# Multidimensional List

my_list1 = ["Yash", "Sou", "Minni", "Pappa", "Mummy", "Kushinu"]
my_list2 = ["Bread", "Butter", "Cheese", "Milk", "Cookies", "Biscuits"]

my_list3 = [my_list1, my_list2]
# print(my_list3)
#
# ele1 = my_list3[0][1]
# print(ele1)
# ele2 = my_list3[1][4]
# print(ele2)

# length = len(my_list3)
#
# for i in my_list3:
#     print(my_list3)


my_lists = [
    ["Yash", "Sou", "Minni"],
    ["Bread", "Butter", "Cheese"]
]
length = len(my_lists[0])
print(length)

for i in range(len(my_lists)):
    for j in range(len(my_lists[i]) - 1, -1, -1):
        print(my_lists[i][j])
