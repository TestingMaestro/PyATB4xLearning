# max between 3

num1 = int(input("Enter the number 1\n"))
num2 = int(input("Enter the number 2\n"))
num3 = int(input("Enter the number 3\n"))

if num1 > num2 and num1 > num3:
    print("Max is Num1: ", num1)
elif num2 > num1 and num2 > num3:
    print("Max is Num2: ", num2)
else:
    print("Max is Num3: ", num3)

maxi = max(num3, num2, num1)
print("Max is ", maxi)
