class InsufficientBalanceError(Exception):
    def __init__(self, message="Balance Exception"):
        self.message = message
        super().__init__(self.message)


def check_balance(withdrawal_amount, balance):
    if withdrawal_amount > balance or withdrawal_amount < 0:
        print(f"Amount Withdrawn:{withdrawal_amount}\nBalance:{balance}")
        raise InsufficientBalanceError("Insufficient Balance or Withdrawal Amount cannot be negative")

    else:
        balance = deposit_amount()
        new_balance = withdrawal_amount - balance
        print("Withdrawal is Possible")
        print(f"Amount Withdrawn:{withdrawal_amount}\nBalance:{new_balance}")


def deposit_amount(deposited_amount=0, balance=0):
    return deposited_amount + balance


try:
    check_balance(-1, 100)
except InsufficientBalanceError as e:
    print(e)
