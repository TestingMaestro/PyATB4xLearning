class Father:
    __key = "123"

    def father_money(self):
        print(10)

    def __show_key(self):
        return self.__key

    def home(self):
        return "This is from Father"

    def show_everything(self):
        key_is = self.__show_key()
        print(key_is)

class Mother:
    def mother_money(self):
        print(5)

    def home(self):
        return "This is from Mother"


class Son(Mother, Father):
    pass


class Son2(Father, Mother):
    pass


son = Son()
print(son.home())
son.father_money()
son.mother_money()
son.show_everything()


son2 = Son2()
son2.father_money()
son2.show_everything()
son2.mother_money()
print(son2.home())
