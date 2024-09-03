# Multidimensional tuple

my_tuple1 = ("Batman", "Super man")
my_tuple2 = ("Flash", "Wonder Women")

my_tuple3 = (my_tuple1, my_tuple2)
print(my_tuple3)

# or

my_tuple = (
    (1, 2, 3),
    (4, 5, 6)
)

# accessing elements
ele1 = my_tuple[0][0]
print(ele1)
ele2 = my_tuple[0][1]
print(ele2)
ele3 = my_tuple[1][0]
print(ele3)

print(len(my_tuple3))
