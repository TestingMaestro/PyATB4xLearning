# os Module:-->
# We use os to interact with OS related files

import os

# get the current working directory
current_directory = os.getcwd()
print(f"Current Working Directory: {current_directory}")

# To move to a different directory, use os.chdir().
# First specify the path where you want to move and then continue

# os.chdir(r"C:\Users\91914\PycharmProjects\PyATB4xLearning\src\Sept2024\ex_07092024")
# print("New Directory:", os.getcwd())
# list_files = os.listdir(os.getcwd())
# print(list_files)

# You can create a new directory using os.mkdir().

# list_files = os.listdir(os.getcwd())
# print(list_files)
# for dirs in range(1, 5):
#     dir_names = input(f"Enter {dirs} Directory name")
#     if not os.path.exists(dir_names):
#         os.mkdir(dir_names)
#     else:
#         print("Directory already exists")

file_path = os.path.join("C:/Users/91914/PycharmProjects/PyATB4xLearning/src/Sept2024/", "ex_10092024")
print(file_path)
# List all directories and files present in current working directory
lists = os.listdir(os.getcwd())
print(lists)

# to check if a file or directory exists at a certain path, use os.path.exists().
if os.path.exists("../ex_10092024"):
    print("Dir exists")
else:
    print("Doesn't exist")

