from abc import ABC, abstractmethod


class PyATB4x(ABC):  # incomplete class

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def pay_fee(self):
        pass

    def enrolled(self):
        print("Enrolled")


class Yash(PyATB4x):
    def pay_fee(self):
        print("Payed the fees")


y = Yash("1L")
y.pay_fee()
y.enrolled()
