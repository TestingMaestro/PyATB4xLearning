# Type Conversion

# string to int
a = "20"
print(type(a))

conv = int(a)
print(type(conv))

# String to float
b = "300.34343"
conv = float(b)
print(type(conv))

# str to list
c = "123ABC"
conv = list(c)  # since it is a string, it iterates over each character
print(conv)

# int to float

m = 30
print(type(m))

conv = float(m)
print(type(conv))

# int to str
conv = str(m)
print(type(conv))

# str to list
c = "123ABC"
conv = list(c)  # since it is a string, it iterates over each character
print(conv)

# str to tuple
c = "123ABC"
conv = tuple(c)  # since it is a string, it iterates over each character
print(conv)

# str to set
c = "123ABCC"
conv = set(c)  # since it is a string, it iterates over each character
print(conv)

# list to str
my_list = ["Bread"]

con = str(my_list)
print(con)
print(type(con))

# bool 1 and 0
booll = bool(0) + 1
print(booll)

# Print ascii value
print(chr(90))

print(ord('A'))

print(bytes(m))
