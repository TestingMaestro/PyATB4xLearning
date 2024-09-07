# hierarchical Inheritance

"""
Multiple subclasses inheriting the properties of single parent class

"""


class Car:

    @staticmethod
    def car_types():
        print("Running Car")


class Xuv700(Car):
    def running_xuv_car(self):
        print("XUV700")


class TUV500(Car):
    def running_tuv_car(self):
        print("TUV500")


obj1 = TUV500()
obj1.car_types()
obj1.running_tuv_car()

obj2 = Xuv700()
obj2.car_types()
obj2.running_xuv_car()
