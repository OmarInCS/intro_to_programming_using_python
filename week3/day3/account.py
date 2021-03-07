

class Account:

    annual_rate = 0.04

    def __init__(self, id, balance):
        self.id = id
        self.__balance = balance

    @staticmethod
    def get_monthly_rate():
        return Account.annual_rate / 12

    def get_monthly_int(self):
        return self.get_monthly_rate() * self.__balance

    def get_balance(self):
        return self.__balance

    def withdraw(self, amt):
        self.__balance -= amt

    def deposit(self, amt):
        self.__balance += amt