a = 10


class Person:
    b = 11

    def print_info(self):
        global a
        a = "Note"
        print(a )
        print(self.b)  # Cant use directly b because it belongs to clss [self.b]


obj1 = Person()
obj1.print_info()
