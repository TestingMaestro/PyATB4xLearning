# Take 2 user inputs a & b and perform arithmetic operations
# data type for input is string or return type is string
num1 = int(input("Enter the number 1"))
num2 = int(input("Enter the number 2"))

# Here concatenation happens using + operator
# we cant div/mul/sub two strings we get an error
print(type(num1), "&", type(num2))
print("Sum: ", num1 + num2)
print("Sub: ", num1 - num2)
print("Mul: ", num1 * num2)
print("Div: ", f"{num1 / num2:.2f}")
