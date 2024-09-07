# Multiple Inheritance

class Father:
    def father_money(self):
        return 6

    def home(self):
        return "This is from Father"


class Mother:
    def mother_money(self):
        return 5

    def home(self):
        return "This is from Mother"


class Son(Mother, Father):
    pass


class Son2(Father, Mother):
    pass


son = Son()
print(son.home())

son2 = Son2()
print(son2.home())
