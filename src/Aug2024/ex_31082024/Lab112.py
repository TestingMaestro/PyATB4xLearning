# Constructor

# Global variable
#a = 10
class Dog:
    name = None  # Instance variables

    def __init__(self, name, age):
        print("DC | I'm automatically called when object is created")
        self.name = name
        self.age = age

    def sleep(self):
        print(f"{self.name}'s  age is {self.age} ")


dog1 = Dog("Choww", 10)  # Constructor is automatically called when object is created

dog2 = Dog("Moww", 30)

dog1.sleep()
dog2.sleep()
