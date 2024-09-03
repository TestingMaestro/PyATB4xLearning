userType = input("Enter the user --> Admin, Manager and Guest\n")
userType = userType.lower()
match userType:
    case "admin" | "manager":
        print("Hello Sir!")
    case "guest":
        print("Hello Guest")
    case _:
        print("Hello X")
