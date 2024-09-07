# Inheritance

"""

A class acquiring attributes and behaviour of other class
or
Subclass acquiring attributes and behaviour of Parent class
or
Subclass inherits the properties of Parent class

Syntax: SubClass(ParentClass)

"""

# Single Inheritance

"""

Subclass inherits the properties of one Parent class
subclass can access properties of one parent class and can access his own properties

"""


#  Ex 1
class Father:
    key_car = "123"

    def car(self):
        print("Father has an Alto car")

    def car_key(self):
        print("Father's car can be accessed with", self.key_car)


class Son(Father):
    key_truck = "345"

    def truck(self):
        print("Son has an truck")

    def truck_key(self):
        print("Son's truck can be accessed with", self.key_truck)


father = Father()
father.car()
father.car_key()
print(father.key_car)

son = Son()
print(son.key_truck)
son.car()
son.car_key()
son.truck()
son.truck_key()

# Father can't access son's properties
