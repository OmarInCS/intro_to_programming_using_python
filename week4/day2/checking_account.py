from week3.day4.account import Account


class CheckingAccount(Account):

    def __init__(self, name, balance, limit):
        Account.__init__(self, name, balance)
        self.limit = limit

    def withdraw(self, amount):
        if self.get_balance() - amount >= -self.limit:
            super().withdraw(amount)
