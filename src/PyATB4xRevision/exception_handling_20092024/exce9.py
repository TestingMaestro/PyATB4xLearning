# Files closing
import os


def create_file(my_file):
    if not os.path.exists(my_file):
        with open(my_file, "w") as file1:
            file1.write("textfile")
        print(f"File {os.path.basename(my_file)} created")
    else:
        print(f"File {os.path.basename(my_file)} already exists")


try:
    file = os.path.join(
        r"C:\Users\91914\PycharmProjects\PyATB4xLearning\src\PyATB4xRevision\exception_handling_20092024",
        "my_file.txt")
    create_file(file)
except FileNotFoundError as fnfe:
    print(fnfe)
finally:
    print("I'm execute no matter exception exists or not")
