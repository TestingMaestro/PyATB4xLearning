def my_decorator(func):  # func ---> custom function where u need extra functionality or extend behaviour/alter
    def wrapper():
        print("Open Browser")
        print("Enter the URL")
        print("Login")
        func()
        print("Logout")
        print("Close the browser ")

    return wrapper()


@my_decorator  # When this is applied start_the_car_engine() is assigned to a func
def test_ui():
    print("Testing Home page UI")
