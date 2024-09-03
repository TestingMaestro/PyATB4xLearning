### Task #8
import datetime
import sys

# ✅ Triangle Classifier:
#
#
# Write a program that classifies a triangle based on its side lengths.
#
# Given three input values representing the lengths of the sides,
#
# determine if the triangle is equilateral (all sides are equal),
#
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
#
# Use an if-else statement to classify the triangle.


# sdLen1 = int(input("Enter the length 1\n"))
# sdLen2 = int(input("Enter the length 2\n"))
# sdLen3 = int(input("Enter the length 3\n"))

sdLen1 = float(input("Enter the length 1\n"))
sdLen2 = float(input("Enter the length 2\n"))
sdLen3 = float(input("Enter the length 3\n"))

if sdLen1 == sdLen2 and sdLen1 == sdLen3:
    print("Equilateral Triangle")
elif sdLen1 == sdLen2 or sdLen1 == sdLen3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")


