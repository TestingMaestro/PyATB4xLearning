# files
# try - except finally
from Lab159 import method_name

file = None
try:
    file = open("data.txt", 'r')
    print(file.read())
except Exception as fnfe:
    print("file Not found")
finally:
    if file:
        file.close()
        print("File closed")

