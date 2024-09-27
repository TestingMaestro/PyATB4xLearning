# File Handling:

try:
    file = open("MyTestData.txt", "r")
except FileNotFoundError as fne:
    pass
else:
    content_read = file.read()
    print(content_read)
    if file:
        file.close()

file = open("MyTestData.txt", "a")
print(file.write(" Jai append"))
