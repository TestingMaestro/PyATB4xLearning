class Person:  # blue-print/ template--> No real entity is created
    # Attributes
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None

    # behaviour
    def talk(self):  # No Return type No arg
        print("I can Talk")

    def sleep(self, name):
        print(f"{name} is sleeping")
        return None

    def walk(self):
        print("I am walking")

    def walk_return(self):
        return "I am walking in return"


# Create an object of class
# object_reference = ClassName()--> Object

obj1 = Person()

# access attributes from class and initialize via obj
obj1.name = "Yash"
obj1.gender = "Male"
obj1.phone_no = "94354546451"
obj1.age = 30
obj1.id = "M2837"

# use
print(obj1.name)
print(obj1.gender)
print(obj1.id)
print(obj1.age)
print(obj1.phone_no)

# reinitialization
obj1.age = 28
print(obj1.age)

# access methods

obj1.talk()
obj1.sleep(obj1.name)
obj1.walk()
res = obj1.walk_return()
print(res)