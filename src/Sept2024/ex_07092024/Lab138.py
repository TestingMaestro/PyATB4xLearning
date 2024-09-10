#  Overriding ex -->2
"""
super()
1. In case of method overriding if user wants to access superclass properties(methods/attributes) in subclass
2. super() is used in case of Non static context
"""


class Father:
    __key = "234"
    door_no = "2"

    def home(self):
        print("Father's 2 BHK")

    def secured_key(self, isAuth):
        if isAuth is not None:
            print("Access Confirmed! Get in", self.__key)
        else:
            print("No Entry")


class Son(Father):
    b = 10

    def home(self):
        super().home()  # If user wants to access parent's method/behaviour we use super() keyword
        print(super().door_no)  # If user wants to access parent's attributes we use super() keyword
        print("Son's 3 BHK")
        print(self.b)  # ----> My b


obj = Son()
obj.home()
obj.secured_key(True)
