import Calculator
from pkg2 import shape_area
from collections import deque,OrderedDict

class Computation:

    def __init__(self):
        self.a = 12

    def am(self, a):
        return a * a


# obj_ref = Calculator.MyCalculator(6, 3)
# res1 = obj_ref.multiply(1, 1)
# res2 = obj_ref.add(1, 1)

# print(res1)
# print(res2)

a = int(input("Enter the radius/length or a value"))
b = int(input("Enter the breadth or b value"))
circle_a = shape_area.c_area
triangle_a = shape_area.t_area
obj_ref4 = Calculator.MyCalculator(a, b)

my1 = obj_ref4.add()
my2 = obj_ref4.multiply()
my3 = obj_ref4.division()

print(f"Addition of a={obj_ref4.a} + b={obj_ref4.b}: {my1}")
print(f"Subtraction of a={obj_ref4.a} + b={obj_ref4.b}: {my2}")
print(f"Division of a={obj_ref4.a} + b={obj_ref4.b}: {my3:.2f}")
print(f"Area Of Circle: {circle_a:.2f}")
print(f"Area Of Triangle: {triangle_a}")
