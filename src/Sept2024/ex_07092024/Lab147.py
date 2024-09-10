# Non-static to static ---> Directly accessible

class MyClass1:
    @staticmethod
    def my_method1():
        print("Calling my method 1")

    @staticmethod
    def my_method2():
        print("Calling my method 2")


class MyClass2:  # Inheritance is not required to access static members

    def my_method3(self):
        MyClass1.my_method1()  # if we want to access methods in the different class
        MyClass1.my_method2()


class2 = MyClass2()
class2.my_method3()
