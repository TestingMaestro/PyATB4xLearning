# Check the user age so that he can go to the club or not

age = input("Enter the age")
age = int(age)
#
# if age >= 21:
#     print("User can go to the club")
# else:
#     print("User can't go")
#
# # Logic 2
#
# if age >= 21:
#     print(f"User can go to the club {age}")
# else:
#     print(f"User can't go {age}")

# Logic 3 Using Ternary operator

print(f"User can go with this age {age}" if age >= 21 else f"User can't go {age}")
