# Escape sequence

print("Hello Yashodhar")
print("Hello\nYashodhar")  # \n---> New Line
print("Hello\tYashodhar")  # \n---> Tab Line
print("Hello\b\nYashodhar")  # \n---> Back space

# dir = 'C:\yash\n.txt'  # ---> Here \n will be taken as escape sequence so error --->error
# dir = "C:\yash\n.txt"  # ---> Here \n will be taken as escape sequence so error --->printed in new line
dir = r"C:\yash\n.txt"  # ---> Here \n will be taken as escape sequence so error --->sol: cover with r--->raw string
dir2 = r'C:\yash\n.txt'  # ---> Here \n will be taken as escape sequence so error --->sol: cover with r--->raw string
print(dir)
print(dir2)

name = "Yash'karki"
print(name)
# name2 = 'Yash'Karki'   # Error because it is used in single quotes. Sol: use escape sequence "\"

name2 = 'Yash\'karki'
print(name2)
