t = ("thetestingacademy.com", "for", "thetestingacademy.com")
print(t)
my_set = set(t)

print(my_set)

tup = tuple(my_set)
print(tup)

my_set = {1, 2, 3, 4, 5, 6}
# 1. add(element)  --> single element

my_set.add(7)
my_set.add(8)
my_set.add(8)
print(my_set)

# 2. update(elements)---> update multiple elements

my_set.update({20, 22, 45, 30, 1})
print(my_set)

# Removing elements

# 3. remove(ele)
my_set.remove(1)
print(my_set)

# 4. discard(ele)
my_set.discard(4)
print(my_set)

# 5. pop()---> remove and return arbitrary element
my_set1 = {100, 20, 40, 30, 90}
popped_ele = my_set1.pop()
print(popped_ele)
print(my_set1)
