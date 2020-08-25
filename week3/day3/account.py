
class Account:

    annual_rate = 0.04

    def __init__(self, id, balance):
        self.__id = id
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

    def __gt__(self, other):
        return self.get_balance() > other.get_balance()

    def __add__(self, other):
        return self.get_balance() + other.get_balance()

    def __str__(self):
        return f"Account {self.__id}: {self.__balance}, {self.get_monthly_int()}"


if __name__ == "__main__":
    a1 = Account(101, 30000)
    a1.deposit(333)
    print(a1)
    a1.withdraw(333)
    print(a1)
    print("-" * 30)