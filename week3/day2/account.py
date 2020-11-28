
class Account:

    annual_rate = 0.045

    def __init__(self, id, balance):
        self.id = id
        self.balance = balance

    @staticmethod
    def get_monthly_rate():
        return Account.annual_rate / 12

    def get_monthly_int(self):
        return Account.get_monthly_rate() * self.balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def __gt__(self, other):
        return self.balance > other.balance

    def __sub__(self, other):
        self.withdraw(other)

    def __str__(self):
        return f"id: {self.id}, balance: {self.balance}"