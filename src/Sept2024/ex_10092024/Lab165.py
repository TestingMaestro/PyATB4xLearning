# FILE HANDLING

# r ---> read mode--> opens the file in read mode. If file doesn't exist it throws FileNotFound error
file = open("My Data.txt", "r")
if file:
    content = file.read()
    print(content)
else:
    print("File Doesn't exist")
