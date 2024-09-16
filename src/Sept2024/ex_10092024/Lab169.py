"""
Use os.path.isfile() to check if the path points to a file.
Use os.path.isdir() to check if the path points to a directory.
"""
import os

file_path1 = os.path.join(r"C:\Users\91914\PycharmProjects\PyATB4xLearning\src\Sept2024\ex_10092024", r".\data.txt")
file_path2 = os.path.join(r"C:\Users\91914\PycharmProjects\PyATB4xLearning\src\Sept2024\ex_1009202")
if os.path.isfile(file_path1):
    print("It is a File")
elif os.path.isdir(file_path2):
    print("It is a Directory")
else:
    print("not a file/directory")

# If you have a relative path and want the full absolute path, use os.path.abspath().
rel_path = r".\data.txt"
abso_path = os.path.abspath(rel_path)
print(abso_path)

nae = os.path.dirname(r"C:\Users\91914\PycharmProjects\PyATB4xLearning\src\Sept2024\ex_10092024\data.txt")
print(nae)
name = os.path.basename(r"C:\Users\91914\PycharmProjects\PyATB4xLearning\src\Sept2024\ex_10092024\data.txt")
print(name)