a, b, c = (10, 20, 30)

print(a)
print(b)
print(c)

# Search in tuple

cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("London" in cities)
print("India" in cities)

# Concatenation

t = (10, 20, 30)
my_tuple = t + (4,)
print(my_tuple)

t = ("Yash", "Sou")
my_tuple = t + ("minni",)
print(my_tuple)

# List to Tuple

ENV_API_URLS = tuple(["abc.com/get", "xyz.com/get", "qwe.com/put"])
print(ENV_API_URLS)
