# static method: ---> In real world example, we use the method as static when it common

# ex: for a test case common methods are start browser >> Open URL >> Login >> Logout >> Stop the browser
# [mark them as static]

"""
1. Belongs to class or Bound to class
2. If we want to access static members of the class in other class, directly use ClassName.method_name
3. Inheritance is required to access static members
4. If we want to access non-static members of the class in other class, inherit the parent class and
    create the object for subclass and access the static members

static to static---> directly accessible
static to non-static ---> Directly accessible
non-static to non-static ----> Directly Accessible
non-static to static ---> create the object

"""


# static to static---> directly accessible

class MyClass1:
    @staticmethod
    def my_method1():
        print("Calling my method 1")

    @staticmethod
    def my_method2():
        print("Calling my method 2")


class MyClass2:  # Inheritance is not required to access static members

    @staticmethod
    def my_method3():
        MyClass1.my_method1()
        MyClass1.my_method2()


MyClass2.my_method3()
