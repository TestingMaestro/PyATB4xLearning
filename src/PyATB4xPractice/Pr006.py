a = 0
b = 1

"""
for i in range(0, 20):
    print(a, end=" ")
    temp = a + b
    a = b
    b = temp

"""

# for i in range(0, 20):
#     print(a, end=" ")
#     a = a + b
#     b = a - b

fact = 1
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(f"{j}", end=" ")
        fact = fact * j
    print(f"= {fact}")
    fact = j

