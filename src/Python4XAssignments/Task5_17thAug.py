### Task #5


# - Create a program that takes two numbers as input and prints whether the first number is greater than,
# less than, or equal to the second number.

# logic 1

num1 = int(input("Enter the First Number\n"))
num2 = int(input("Enter the Second Number\n"))

print("First Number is Greater" if num1 > num2 else "Second Number is Greater")
print("First Number is Greater" if num1 <= num2 else "Second Number is Greater")

# Logic 2

print("First Number is Greater" if num1 > num2 >= num1 else "Second Number is Greater")

# Logic 3

if num1 > num2 >= num1:
    print("First Number is Greater")
else:
    print("Second Number is greater")
