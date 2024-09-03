# Create a program to sum of 3 nos by taking user input

num1 = int(input("Enter number 1\n"))
num2 = int(input("Enter number 2\n"))
num3 = int(input("Enter number 3\n"))


def sum_of_three_nos(n1, n2, n3):
    return n1 + n2 + n3


result = sum_of_three_nos(num1, num2, num3)
print(result)
result = sum_of_three_nos(n1=num1, n2=num2, n3=num3)
print(result)