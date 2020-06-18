

class Account:

    annual_rate = 0.04

    def __init__(self, id, balance):
        self.id = id
        self.__balance = balance

    def get_monthly_rate(self):
        return Account.annual_rate / 12

    def get_monthly_int(self):
        return self.get_monthly_rate() * self.__balance

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def __gt__(self, other):
        return self.__balance > other.__balance

    def __eq__(self, other):
        return self.__balance == other.__balance

    def __str__(self):
        return f"Account: {self.id}, {self.__balance}"


if __name__ == "__main__":
    a1 = Account(1, 13000)
    a1.deposit(1500)
    print(a1)
    print("-" * 30)
