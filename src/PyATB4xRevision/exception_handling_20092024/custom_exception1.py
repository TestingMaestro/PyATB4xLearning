# Custom Exception/ user defined exception

class MyCustomException(Exception):
    def __init__(self, message="Custom Exception Occurred"):
        self.message = message
        super().__init__(self.message)


class MyExceptionClass(MyCustomException):
    def __init__(self):
        self.my_age = -20

    def age_validation(self):
        if self.my_age < 0:
            raise MyCustomException()
        else:
            print(f"My Age:{self.my_age}")



try:
    obj1 = MyExceptionClass()
    obj1.age_validation()
except MyCustomException as mec:
    print(mec.message)
