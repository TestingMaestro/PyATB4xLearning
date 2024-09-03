# List Methods

my_list = [10, 20, 30, 40, 50]

my_list.append(60)
print(my_list)
print("length: ", len(my_list))

# my_list.append(70,80)
# print(my_list) --> Type error

my_list.extend([70, 80, 90, 20, 40, 30, "Pramod"])
print(my_list)

my_list.insert(2, 200)
print(my_list)

my_list.insert(0, 0)
print(my_list)

# insert element at -1th index

my_list.insert(-1, 99)
print(my_list)

# 4. remove(element) ---removes first occurrence of an ele from the list

my_list.remove("Pramod")
print(my_list)

# 2 same elements , then it removes first occurrence
my_list.remove(40)
print(my_list)

# if you want to remove multiple elements use for loop

for i in my_list:
    if i == i:
        my_list.remove(i)
print(my_list)

##
for i in range(len(my_list)):
    print(f"Element at {i}th position: {my_list[i]}")

print("----------------------------------")
print("----------------------------------")
# 5 copy()

my_new_list = my_list.copy()
print(my_list)
print(my_new_list)

my_new_list.append("Yash")
my_new_list.remove("Yash")

# sort() --> Sorts the items in the list in ascending order. sort takes 2 optional arguments key, reverse
my_new_list.sort()
print(my_new_list)

# reverse  ---> Reverse the order of it

my_new_list.reverse()
print(my_new_list)

# count()----> count tells number of times items appeared in the list

my_list1 = [0, 10, 20, 200, 30, 50, 60, 70, 80, 90, 20, 40, 30, 99, 30, 30]
items_count = my_list1.count(30)
print(f"30 repeated {items_count} times")
