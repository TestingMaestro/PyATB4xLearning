browser_name = input("Enter the browser\n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        print("Firefox Browser")
    case "EDGE":
        print("Edge Browser")
    case "chrome":
        print("Chrome Browser")
    case _:
        print("No browsers are installed")
