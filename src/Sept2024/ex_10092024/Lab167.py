# Ex 1 --> Creating and writing into file

# file = open("MyTestData.txt", "w")
#
# # Write data to the file
# file.write("Hello, this is Yashodhar\n")
# file.write("We are learning file handling")
#
# # Close the file
# file.close()
#
#
# # Ex 2 --> Reading the data from the file
# file = open("MyTestData.txt", "r")
# cont = file.read()
# print(cont)
#
# file.close()
#
#
# # Ex 3 --> Appending new content to the file
# file = open("MyTestData.txt", "a")
# cont = file.write("\nAppending new content to the file.")
#
# file.close()


# Ex 4 --> Reading the data from the file line by line
file = open("MyTestData.txt", "r")
for line in file:
    print(line, end="")


# Using the with Statement (Best Practice)
# It’s a good practice to use the with statement
# for file handling because it automatically closes the file after you’re done with it, even if an error occurs.

with open("MyTestData.txt", "r") as file:
    print(file.read())

