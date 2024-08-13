# Given 2 numbers to take the user input num1 and num 2

num1 = int(input("Enter the 1st number \n"))
num2 = int(input("Enter the 2nd number \n"))

maximum = max(f"{num1}", f"{num2}")
print("maximum of 2 numbers", num1, "&", num2, "=", maximum)

power = pow(num1, num2)
print("Result of", f"{num1}", "^", f"{num2}", "=", power)

subtract = num2 - num1
print("Result of", f"{num2}", "-", f"{num1}", "=", subtract)

summation = num1 + num2
print("Result of", f"{num1}", "+", f"{num2}", "=", summation)

division = num2/num1
print("Result of", f"{num2}", "/", f"{num1}", "=", division)

multiply = num2*num1
print("Result of", f"{num1}", "*", f"{num2}", "=", multiply)



