class MyException:

    def exception_method(self):
        a = int(input("Enter a number a"))
        b = int(input("Enter a number b"))
        c = a / b
        print("Result is:",c)


try:
    e = MyException()
    e.exception_method()
except Exception as e:
    print(type(e))
    print("Please check the inputs")
else:
    print(f"{e.exception_method()}")
finally:
    print("I'm always executed")
