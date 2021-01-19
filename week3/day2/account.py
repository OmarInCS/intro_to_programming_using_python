
class Account:

    annual_rate = 0.04

    def __init__(self, id, balance):
        self.__balance = balance
        self.id = id

    @staticmethod
    def get_monthly_rate():
        return Account.annual_rate / 12

    def __gt__(self, other):
        return self.__balance > other.__balance

    def __str__(self):
        return f"id: {self.id}, balance: {self.__balance}"


a1 = Account(101, 20000)
a2 = Account(102, 15000)
a3 = Account(103, 25000)
print(Account.annual_rate)
print(Account.get_monthly_rate())

print(a1 > a2)
print(a1)