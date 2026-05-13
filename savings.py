from Account import Account

class Savings(Account):

    def __init__(self, owner, balance=0):

        super().__init__(owner, balance)

        self.withdraw_limit = 100


    # Overriding withdrawal method
    def withdraw(self, amount):

        if amount > self.withdraw_limit:
            print("Withdrawal cannot exceed $100")

        else:
            super().withdraw(amount)


savings = Savings("Alice", 1000)

savings.withdraw(50)

savings.withdraw(200)
