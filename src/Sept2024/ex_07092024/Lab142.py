from abc import ABC, abstractmethod


class Father(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def pay_fee(self):
        pass


class Son(Father):
    def pay_fee(self):
        print("Paid the loan")


s = Son("YY")
s.pay_fee()
