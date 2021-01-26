
class Account:

    annual_rate = 0.04

    def __init__(self, id, balance):
        self.id = id
        self.__balance = balance

    @staticmethod
    def get_monthly_rate():
        return Account.annual_rate / 12

    def get_monthly_int(self):
        return Account.get_monthly_rate() * self.__balance

    def __gt__(self, other):
        return self.__balance > other.__balance

    def __add__(self, amount):
        self.__balance += amount

    def __sub__(self, amount):
        self.__balance -= amount

    def __str__(self):
        return f"Account: {self.__balance}"