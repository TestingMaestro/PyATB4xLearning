# Functions with or without parameters or arguments

#  Function without arguments/parameters

def user_email():
    print("yashodhar.karki@gmail.com")


# Functions with arguments or parameters

def user_name(name):
    print("Hello, ", name)


# We can pass any data type
user_email()
user_name("Yash")
user_name(123)
user_name(3.14)
user_name(True)
user_name(None)
user_name(3 + 4j)

# is the above function is returning anything? answer  ---> no lets see----> o/p will be None

# result = user_name("Pramod")
# print(result)
