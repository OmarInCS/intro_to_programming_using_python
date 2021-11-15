from week3.day4.account import Account


class SavingAccount(Account):

    def withdraw(self, amount):
        if self.get_balance() - amount >= 0:
            super().withdraw(amount)
