# w---> opens the file in write mode. If file doesn't exist file will be created and
# If a file exists it overwrites

file = open("My Data.txt", "w")
content_write = file.write("PYTHON PROGRAMMING")
file = open("My Data.txt", "r")
content_read = file.read()
print(content_read)

# a ---> append the data at the end of file
file = open("My Data.txt", "a")
content_write1 = file.write("\tWelcome to PYTHON club")

file.close()

