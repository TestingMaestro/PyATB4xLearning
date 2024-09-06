class Dog:
    # attributes
    name = None
    color = None
    breed = None

    # behaviour

    def bark(self):
        print("barking")

    def sleep(self):
        return "sleeping"


dog1 = Dog()
dog1.name = "Suraj"
dog1.color = "Black"
dog1.breed = "German Sheph"

print(id(dog1.name))
print(dog1.name)
print(dog1.color)
print(dog1.breed)

dog2 = Dog()
dog2.name = "Johnny "
dog2.color = "Word"
dog2.breed = "Golden ret"

print(id(dog2.name))
print(dog2.name)
print(dog2.color)
print(dog2.breed)

