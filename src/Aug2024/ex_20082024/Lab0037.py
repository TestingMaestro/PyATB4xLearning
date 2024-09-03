# Write a program to print max of 2 numbers

num1 = int(input("Enter the number 1\n"))
num2 = int(input("Enter the number 2\n"))

if num1 > num2:
    print("Num1 is greater")
elif num1 == num2:
    print(f"{num2, num2} are equal")
else:
    print("Number 2 is greater")

