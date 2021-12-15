
class Account:
    annual_rate = 0.04

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_monthly_rate(self):
        return Account.annual_rate / 12

    def get_monthly_int(self):
        return self.get_monthly_rate() * self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance
