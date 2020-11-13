
from week4.day1.account import Account

a1 = Account(101, 20000)
a2 = Account(102, 20000)

a1.withdraw(300)
a2.deposit(300)

print(a1.get_balance())
print(a2.get_balance())

print(Account.get_monthly_rate())
