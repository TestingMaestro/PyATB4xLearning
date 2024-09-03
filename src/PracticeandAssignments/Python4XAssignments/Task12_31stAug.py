"""
Create a Employee Class
A - name,age, phone, address, eid
B - walk, talk, printdetails,
with the Constructor which will set the values
Ask the user about the information for E1, E2
print the details of the E1, E2 via the print employee functions.

"""


class Employee:  # blue-print/ template--> No real entity is created
    # Attributes

    def __init__(self, eid, name, age, address, phone_no):
        self.eid = input("Enter Employee Id: ")
        self.name = input("Enter Employee Name: ")
        self.age = input("Enter Employee Age: ")
        self.address = input("Enter Employee Address: ")
        self.phone_no = input("Enter Employee Phone No: ")

    # behaviour
    def talk(self):  # No Return type No arg
        print("Employee can talk")

    def walk(self):
        print("I am walking")

    def print_details(self):
        print(f"Employee Name:{self.name}")
        print(f"Employee id:{self.eid}")
        print(f"Employee Phone No:{self.phone_no}")
        print(f"Employee Address:{self.address}")
        print(f"Employee Age:{self.age}")


employee1 = Employee(name=None, eid=None, age=None, address=None, phone_no=None)
employee1.print_details()

employee2 = Employee(name=None, eid=None, age=None, address=None, phone_no=None)
employee2.print_details()
