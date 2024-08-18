# ### Task #4
# - Write a Python program to calculate the area of a circle given its radius using the
# formula ``` area=π×r^2``` ( Take pie as 3.14)

"""
Step 1: Figure out the inputs
1. input -> radius -> data type -> float
2. input pi -> 3.14
3. exponential ->> "**" or pow()

Step 2: Rough Logic

area = pi * pow(radius,2) or area = pi * (radius**2)

Step 3: Write the Logic """
import math

# Logic 1 -->

radius = int(input("Enter the radius of Circle\n"))
pi = 3.14
area = pi * (radius ** 2)
print("Area of the Circle is ", area)
print(f"Area of the Circle is [Using f - Strings]: {area:.1f}")

# Logic 2

rad = int(input("Enter the radius of Circle\n"))
area = math.pi * math.pow(rad, 2)
# print(math.pi)
print("Area of the Circle using Logic #2: ", area)
print(f"Area of the Circle is [Using f - Strings]: {area:.2f}")

# Logic 3
r = int(input("Enter the radius of Circle\n"))
print(f"Area of Circle = {math.pi * math.pow(r, 2):.2f}")
