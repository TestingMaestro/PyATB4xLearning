# Custom Exception

"""
Custom exception is nothing but a user defined which provides details about something wrong happened in the code
or code tells faulty logic

Creating Custom exception

"""


# Below class tells python that "My code has Exception"
class CustomException(Exception):

    # Below line is used to initialize the message and stor the message or details obout the faulty logic occurred
    def __init__(self, message="Custom Error Occurred"):
        self.message = message
        super().__init__(self.message)  # this is a very important to call base class constructor to initialize
        # the parent class constructor and uses all the properties of Exception class
        #  If we don't use this, it will omit or bypass all the built_in functionality results
        #  to improper behavior and my error don't behave like a proper exception


def my_age(age):
    if age < 0 or age > 120:
        raise CustomException("Invalid Input")
    else:
        print(f"My Valid Age:{age}")


try:
    my_age(int(input("Enter the invalid/valid input")))
except CustomException as ce:
    print(ce.message)
