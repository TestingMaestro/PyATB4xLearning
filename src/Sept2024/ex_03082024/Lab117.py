class Person:
    # name = "Yash"  # hardcoded value
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2

    def print_value(self):
        my_string = "&"
        print(self.name1, "&", self.name2)


yash = Person("Yash", "Sou")
fam = Person("Pramod", "Praveen")
yash.print_value()
fam.print_value()
