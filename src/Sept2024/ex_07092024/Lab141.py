# Abstraction ----> Hiding the internal details and showcasing only the required functionality

# Concrete Class --->
"""
class which has concrete methods and it has method declaration and body
We can create object for this class
"""

# Abstract Class --->
"""

Class which consists of one or more abstract method
We cant create object for abstract class
Abstract class's abstract method has no implementation and we need to provide implementation in sub class or
This those method should be overridden in the subclass

"""

# Abstract Method:

"""

Abstract Method doesn't have the body...it has only the definition
This abstract method should be overridden in the derived class to create the object class
if that class also failed to provide the implementation it should be overridden in the following subclasses

"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def bark(self):
        pass


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog = Dog()
dog.bark()
