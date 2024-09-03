# Length

my_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

length = len(my_tuple)
print(length)

# Accessing multiple elements

for items in my_tuple:
    print(items, end=" ")
print("\n")
# Accessing multiple elements index wise/ based on index in reverse order

# for i in range(length - 1, 0, -1):
#     print(f"Element at index {i} is: {my_tuple[i]}")

# # Accessing multiple elements index wise/ based on index in normal order
for i in range(0, length):
    print(f"Element at index {i} is: {my_tuple[i]}")
