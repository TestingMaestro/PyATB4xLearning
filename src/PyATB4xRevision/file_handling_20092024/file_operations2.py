# Using with statement

with open("MyTestData.txt", "w") as file_w:
    file_w.write("Contents of file are \n")
    file_w.write("My best favourite file handling")

with open("MyTestData.txt", "r") as file_r:
    read = file_r.read()
    print(read)
