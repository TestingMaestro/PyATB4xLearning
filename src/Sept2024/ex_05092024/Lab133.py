# Interview Question/Practice

class GF:
    def car(self):
        return "Old Car"


class F(GF):
    pass

    def car(self):
        return "honda civic"


class S(F):
    pass
    # def car(self):
    #     return "Lamborghini"


s = S()
print(s.car())
