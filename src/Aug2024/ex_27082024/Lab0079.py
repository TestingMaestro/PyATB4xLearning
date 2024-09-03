#  Time Decorator   ---> Dec
import time

start_time = time.process_time()
end_time = time.process_time()


def time_decorator(func):
    def wrapper():
        print("Start Time:", start_time)
        func()
        print("End Time", end_time)
        print("Time Taken by the function", end_time - start_time)

    return wrapper


@time_decorator
def test_ui():
    print("Time Taken by this function")
    time.sleep(2)


test_ui()


@time_decorator
def test_ui2():
    print("Time Taken by this function2")
    time.sleep(5)


test_ui2()
