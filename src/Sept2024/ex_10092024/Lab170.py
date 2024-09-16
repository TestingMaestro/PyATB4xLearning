#  Combining Everything: Working with Files and Directories Using the os Module

"""
File Handling with the os Module: Import the os module to interact with the file system.

---> Create directories.
---> Create and write to a file inside the directory.
---> Read the file.
---> Delete the file and directories.

"""
import os.path

# Creating Directory

if not os.path.exists("Folder1"):
    os.mkdir("Folder1")
    print("Directory Created Successfully")
else:
    print("Folder1 already exists")

# Create and write to a file inside the directory

# os.chdir(r"C:\Users\91914\PycharmProjects\PyATB4xLearning\src\Sept2024\ex_10092024\Folder1")
#
# with open("File1.txt", "w") as file:
#     file_path = os.path.join(r"C:\Users\91914\PycharmProjects\PyATB4xLearning\src\Sept2024\ex_10092024\Folder1",
#                              r"File1.txt")
#     file.write("Directories and Files\n")
#     file.write("Yashodhar loves Souparnika\n")
#     file.write(f"File:{os.path.basename(file_path)}\n")
#     file.write(f"Directory:{os.path.dirname(r"Folder1\File1.txt")}")
#
# with open("File1.txt", "r") as file:
#     content = file.read()
#     print(content)
#
# # os.rename("File1.txt", "newFile1.txt")


old_dir = r"C:\Users\91914\PycharmProjects\PyATB4xLearning\src\Sept2024\ex_10092024\Folder1"
new_dir = r"C:\Users\91914\PycharmProjects\PyATB4xLearning\src\Sept2024\ex_10092024\NewFolder1"

try:
    if os.path.exists(old_dir):
        os.rename(old_dir, new_dir)
        print(f"{old_dir} is changed to {new_dir}")
    else:
        print(f"{old_dir} doesn't exist")
except FileNotFoundError as fne:
    print(fne)
