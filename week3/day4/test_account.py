
from week3.day4.account import Account

a1 = Account(101, 20000)
a2 = Account(102, 15000)

a1.withdraw(300)
a2.deposit(300)

print(a1.id, a1.get_balance())
print(a2.id, a2.get_balance())
print(Account.annual_rate)
print(Account.get_monthly_rate())
