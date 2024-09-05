# real Time example

class VWOLoginPage:
    def __init__(self, email1, password1):
        self.email1 = email1
        self.password1 = password1

    def confirm_login(self):
        if self.email1 == "yash@gmail.com" and self.password1 == "pass123":
            print("Login is allowed")
        else:
            print("Not allowed to login")


email = input("Enter the username\n")
password = input("Enter the password\n")
email = email.lower()
password = password.lower()
creds1 = VWOLoginPage(email, password)
creds1.confirm_login()
