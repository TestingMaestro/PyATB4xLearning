# os module
import os

# cwd
current_dir = os.getcwd()
print(current_dir)

# list directories
print(os.listdir())

# change directory
# new_path = r"C:\Users\91914\PycharmProjects\PyATB4xLearning\src\PyATB4xRevision\file_handling_20092024\dir1"
# old_path = os.getcwd()
# os.chdir(new_path)

# path--> path of file/directories

# joins directories or files
file = os.path.join(os.getcwd(), "RawData.txt")
patht = r"C:\Users\91914\PycharmProjects\PyATB4xLearning\src\PyATB4xRevision\file_handling_20092024\dir1\RawData.txt"

# os.path.exists check whether file/directory exists or not
# os.path.basename(path) returns file name
if os.path.exists("RawData.txt"):
    print(f"{os.path.basename(patht)} exists")

    # get directory name:
dir_name = os.path.dirname(r".\dir1\RawData.txt")
print(dir_name)

# directory exists
if os.path.exists(os.getcwd()):
    print(os.path.dirname(r"dir1\RawData.txt"))

# is file or directory

b = os.path.isfile(patht)
print(b)

# b = os.path.isdir(os.getcwd())
# print(b)
#
# my_path = os.path.abspath("")
# print(my_path)
#
# my_path1 = os.path.relpath(patht)
# print(my_path1)

# Let's put all together
new_path = r"C:\Users\91914\PycharmProjects\PyATB4xLearning\src\PyATB4xRevision\file_handling_20092024"
print(os.getcwd())
if not os.path.exists('dir2'):
    os.mkdir('dir2')
    print("Created Successfully")
else:
    print("directory already exists")

# create a file in that directory and write into file

new_pathww = r"C:\Users\91914\PycharmProjects\PyATB4xLearning\src\PyATB4xRevision\file_handling_20092024\dir2"
os.chdir(new_pathww)
print(os.getcwd())

if not os.path.exists("RawData2.txt"):
    with open("RawData2.txt", "w") as file2:
        file2.write("Contents of file are:\n")
        file2.write("Details of entire file operations")
        print("File created successfully")
else:
    print("File exists already")

# reading files

with open("RawData2.txt", "r") as filee:
    print(filee.read())
