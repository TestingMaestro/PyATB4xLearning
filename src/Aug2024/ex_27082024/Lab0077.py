def my_decorator(func):
    def wrapper():
        print("Before the function call: Helmet")
        print("Before the function call: Knee Guards")
        print("Before the function call: gloves")
        func()
        print("After the function call")
        print("Secure Driving ")

    return wrapper()


@my_decorator  # When this is applied start_the_car_engine() is assigned to a func
def drive_bike():
    print("I'm riding bike")
