

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

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def __repr__(self):
        return f"Account: {self.id}, Balance: {self.__balance}, {self.get_monthly_int()}"

    def __gt__(self, other):
        return self.__balance > other.__balance

    def __add__(self, other):
        return self.__balance + other.__balance


if __name__ == "__main__":
    a1 = Account(101, 20200)
    print(a1)
    print("-" * 30)