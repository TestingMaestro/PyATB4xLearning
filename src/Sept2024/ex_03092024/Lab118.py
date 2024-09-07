class Car:
    def __init__(self, o_name, o_model, o_make):
        self.o_name = o_name
        self.o_make = o_make
        self.o_model = o_model

    def start_engine(self):
        print("Car Name :", self.o_name)
        print("Car Model:", self.o_model)
        print("Car Make:", self.o_make)


lambo = Car("Lamborgini", "V6", 2012)
lambo.start_engine()
xuv = Car("XVU 700", "V12", 2013)
xuv.start_engine()
