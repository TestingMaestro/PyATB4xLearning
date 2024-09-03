# Decorators vs normal function usage

# below we are altering actual code--> not recommended and that's why we use decorators

def start():
    print("Open Browser")
    print("Enter the URL")
    print("Login")


def end():
    print("Logout")
    print("Close the browser")


def test_ui():
    print("Testing home page Ui")


start()
test_ui()
end()
