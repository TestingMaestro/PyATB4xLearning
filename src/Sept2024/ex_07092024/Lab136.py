# Method Overriding
# Defining methods with the same name and signature in subclass as in super-class with different implementation
# To achieve method overriding, we need:
"""
1. Inheritance [IS-A Relationship]
2. Same Method name
3  Same Signature [Method Parameters/Arguments]

"""


class Bike:
    key = "123"

    def starts(self):
        print("Starting the Bike")


class Himalayan(Bike):
    def starts(self):
        print("Starting Himalayan with key", self.key)


him = Himalayan()
him.starts()  # Overridden Implementation
