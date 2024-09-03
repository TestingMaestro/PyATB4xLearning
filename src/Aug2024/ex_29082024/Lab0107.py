# Set Operations

# 6 union() or | ---> returns all elements from both set

my_set1 = {1, 2, 3, 4, 5, 6, 7}
my_set2 = {8, 45, 20, 22, 30, 1, 2}

# union()
union_set = my_set1.union(my_set2)
print(union_set)

# |
union_set1 = my_set1 | my_set2
print(union_set1)

# 7 intersection() or & ---> returns common elements from both the sets

my_set1 = {1, 2, 3, 4, 5, 6, 7}
my_set2 = {8, 45, 20, 22, 30, 1, 2, 4}

# intersection()
union_set = my_set1.intersection(my_set2)
print(union_set)

# &
union_set1 = my_set1 & my_set2
print(union_set1)

# 8 difference() or '-' ---> returns new set with elements from set1 but not in set 2

my_set1 = {1, 2, 3, 4, 5, 6, 7}
my_set2 = {8, 45, 20, 22, 30, 1, 2, 4}

# difference()
union_set = my_set1.difference(my_set2)
print(union_set)

# -
union_set1 = my_set1 - my_set2
print(union_set1)

# 9 system_difference() or '^' ---> returns new set with elements from set1 but not in set 2

my_set1 = {1, 2, 3, 4, 5, 6, 7}
my_set2 = {8, 45, 20, 22, 30, 1, 2, 4}

# system_difference()
union_set = my_set1.symmetric_difference(my_set2)
print(union_set)

# ^
union_set1 = my_set1 ^ my_set2
print(union_set1)

# 10 subset ---> if one set is subset of another issubset() or <=

my_set1 = {1, 2,6}
my_set2 = {1, 2, 3, 4, 5}

print(my_set1.issubset(my_set2))
print(my_set1 <= my_set2)

# 11 superset ---> if one set is superset of another issuperset() or >=

my_set1 = {1, 2, 3, 4}
my_set2 = {1, 2, 3, 4, 5}

print(my_set2.issuperset(my_set1))
print(my_set2 >= my_set1)

# 12 disjoint - --> check if 2 sets have no common elements
my_set1 = {1, 2, 3, 4}
my_set2 = {6, 7, 8}

print(my_set1.isdisjoint(my_set2))
