# Multilevel Inheritance

"""
Subclass accessing the properties of its parent class and
this parent class which in turn accessing property of its parent

"""


class GrandFather:
    gold = "2kg"

    def BHK2(self):
        print("2 BHK")


class Father(GrandFather):
    diamond = "4 kg"

    def BHK1(self):
        print("1 BHK")


class Son(Father):
    BTC = "1 BTC"

    def BHK3(self):
        print("3 BHK")


son = Son()
print(son.gold)
print(son.diamond)
print(son.BTC)
son.BHK1()
son.BHK2()
son.BHK3()
