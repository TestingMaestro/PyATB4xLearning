# Encapsulation ex 1


class Bank:

    def __init__(self, account_number, balance):
        self.balance = balance
        self.__account_number = account_number

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def check_balance(self):
        print(self.balance)

    def show_my_account_number(self, isAuthenticated_user):
        if isAuthenticated_user:
            print("My Account Number:",self.__account_number)
        else:
            print("Not an Authenticated User")


obj_ref = Bank(949778967846, 0)
obj_ref.deposit(200)
obj_ref.check_balance()
obj_ref.deposit(200)
obj_ref.check_balance()
obj_ref.show_my_account_number(False)

