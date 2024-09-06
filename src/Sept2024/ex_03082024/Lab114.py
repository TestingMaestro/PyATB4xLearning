class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def div(self):
        return self.a / self.b

    def mul(self):
        return self.a * self.b


a = int(input("Enter the value of a \n"))
b = int(input("Enter the value of b\n"))
cal_1 = Calculator(a, b)
res1 = cal_1.sum()
print(res1)
res1 = cal_1.sub()
print(res1)
res1 = cal_1.div()
print(f"{res1:.2f}")
res1 = cal_1.mul()
print(res1)
