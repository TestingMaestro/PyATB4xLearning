# Decorators

"""
Steps:
Wrap and Call
"""
# Example - Start the car

"""
Before Starting the car, we need,

>>>> Keys and unlock
>>>> Open the door
>>>> Sit in the car
>>>> Start the car
>>>> Turn off the engine
>>>> Open the door 
>>>> Loc the car with the keys
"""

car1 = "NISSAN GTR"
car2 = "PORSCHE 911 Turbo"


def my_decorator(func):
    def wrapper1():
        print(car1)
        print("Before the function call: Keys and unlock")
        print("Before the function call: Open the door")
        print("Before the function call: Sit in the car")
        func()
        print("After the function call: Turn off the engine")
        print("After the function call: Open the door ")
        print("After the function call: Lock the car with the keys")

    def wrapper2():
        print(car2)
        print("Before the function call: Keys and unlock")
        print("Before the function call: Open the door")
        print("Before the function call: Sit in the car")
        func()
        print("After the function call: Turn off the engine")
        print("After the function call: Open the door ")
        print("After the function call: Lock the car with the keys")

    return wrapper1(), wrapper2()


@my_decorator  # When this is applied start_the_car_engine() is assigned to a func
def start_the_car_engine():
    print("Car Engine Starts")


@my_decorator  # When this is applied to a function car_acceleration() is assigned to a func
def car_acceleration():
    print("Lights are switched on")
