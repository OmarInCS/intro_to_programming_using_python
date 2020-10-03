
class Account:

    annual_rate = 0.04

    def __init__(self, id, balance):
        self.id = id
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    @staticmethod
    def get_monthly_rate():
        return Account.annual_rate / 12

    def get_monthly_int(self):
        return self.get_monthly_rate() * self.__balance

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def copy(self):
        return Account(self.id, self.__balance)

    def __gt__(self, other):
        return self.__balance > other.__balance

    def __add__(self, other):
        if isinstance(other, int):
            return self.__balance + other
        else:
            return self.__balance + other.__balance

    def __repr__(self):
        return f"Account {self.id}: {self.__balance}"