class CheckSuper:

    def my_method(self):
        print("Method 1")

    def my_other(self, a, b):
        print(a + b)


class Check1(CheckSuper):

    def my_method(self):
        super().my_method()
        super().my_other(10,20)
        print("Check1 method")


class Check2(Check1):
    def my_method(self):
        super().my_method()
        print("Check2 method")


check2 = Check2()
check2.my_method()
