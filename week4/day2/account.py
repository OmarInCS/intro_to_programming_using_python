
class Account:

    annual_rate = 0.045

    def __init__(self, id, balance):
        self.id = id
        self.balance = balance


    def get_monthly_rate(self):
        return Account.annual_rate / 12

    def get_monthly_int(self):
        return self.get_monthly_rate() * self.balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def __gt__(self, other):
        return self.balance > other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __str__(self):
        return f"id: {self.id}, {self.balance}"


if __name__ == "__main__":
    print(__name__)
    a1 = Account(1, 13000)
    print(a1)