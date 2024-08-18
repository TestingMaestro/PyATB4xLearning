# Task #6
import math

# - Develop a Python script that calculates the square and cube of a given number.

number = int(input("Enter a Number\n"))

squareOfNumber = pow(number, 2)
cubeOfNumber = pow(number, 3)
print("Square and a cube of given number", number, "is", squareOfNumber, " & ", cubeOfNumber)

# Logic 2

print(f"Square and a cube of given number, {number} is {squareOfNumber, cubeOfNumber}")

# Logic 3
print(f"Square and a cube of given number, {number} is {math.pow(number, 2), math.pow(number, 3)}")
