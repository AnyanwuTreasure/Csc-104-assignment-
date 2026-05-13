class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print("Deposit successful")

    def withdraw(self, amount):

        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")

        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance
