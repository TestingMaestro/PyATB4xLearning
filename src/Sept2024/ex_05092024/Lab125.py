class Parent:
    gold = "2Kg"

    def BHK2(self):
        print("2 BHK house")


class Child(Parent):
    def BHK3(self):
        print("3 BHK house")


child = Child()
print(child.gold)
child.BHK2()
child.BHK3()
