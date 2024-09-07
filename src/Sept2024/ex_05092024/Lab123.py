class Bank:

    def __init__(self, account_number, balance):
        self.__balance = balance
        self.__account_number = account_number

    def deposit(self, deposit_amount):
        self.__balance += deposit_amount
        return self.__balance

    def authenticated_user_check(self, isAuth, deposit_amount):
        if isAuth:
            print(self.__account_number)
            check_balance = self.deposit(deposit_amount)
            print(check_balance)
        else:
            print("Not an Authenticated User")


icici_bank = Bank(789789798798797, 0)
icici_bank.authenticated_user_check(True, 100)
icici_bank.authenticated_user_check(True, 100)
