# Polymorphism ---->Poly -->many::Morphism--->Forms
"""

Objects behaves differently at different stages of its life cycle

objects has many forms---[One object many forms]

it is mostly behaviour

2 Types

compile time polymorphism [Method Overloading]
Run-time polymorphism [Method Overriding]

Method Overloading
[Traditionally method overloading is not supported in python but can be achieved via default args or *args]

Method Overriding
Defining methods with the same name and signature in subclass as in super-class with different implementation


"""


# Method Overloading

class Calc:
    def sum(self, a=0, b=0, c=0):
        return a + b + c


cal = Calc()
print(cal.sum())
print(cal.sum(1, 2))
print(cal.sum(1, 2, 3))
