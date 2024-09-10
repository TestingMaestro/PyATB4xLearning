# Ex2---> Method Overloading---using *args

class Calculator:
    def sum(self, *args):
        print(*args)


calc = Calculator()

calc.sum(1, 2, 3)
calc.sum("Yash", 2)
