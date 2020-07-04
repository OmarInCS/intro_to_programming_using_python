
class Account:

    ann_rate = 0.045

    def __init__(self, id, balance):
        self.id = id
        self.__balance = balance

    def get_monthly_rate(self):
        return Account.ann_rate / 12

    def get_monthly_int(self):
        return self.__balance * self.get_monthly_rate()

    def withdraw(self, amt):
        self.__balance -= amt

    def deposit(self, amt):
        self.__balance += amt

    def get_balance(self):
        return self.__balance

    def __gt__(self, other):
        return self.get_balance() > other.get_balance()

    def __eq__(self, other):
        return self.get_balance() == other.get_balance()

    def __str__(self):
        return f"Account {self.id}: {self.__balance}"


if __name__ == "__main__":
    a1 = Account(4, 20000)

    a1.withdraw(2500)
    a1.deposit(3333)

    print(a1.id, a1.get_balance(), a1.get_monthly_int())
