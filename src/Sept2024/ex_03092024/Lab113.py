# taking user input

class Person:

    def __init__(self):
        self.name = input("Enter the Name\n")
        self.age = input("Enter the age\n")
        self.phone = input("Enter the phone\n")
        self.occupation = input("Enter the occupation\n")

    def person_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Phone : {self.phone}")
        print(f"Occupation: {self.occupation}")


print("Enter Person 1 Details")
person1 = Person()
person1.person_details()

print("Enter Person 2 Details")
person2 = Person()
person2.person_details()
