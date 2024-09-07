class Grandparent:
    gold = "2kg"

    def grandparent_method(self):
        print("Grand Parent's Method")


class Parent(Grandparent):
    diamond = "4 kg"

    def parent_method(self):
        print("Parent's Method")


class Child(Parent):
    BTC = "1 BTC"

    def chilc_method(self):
        print("Child's Method")


child = Child()
child.grandparent_method()
