
from week4.day2.account import Account

a1 = Account(101, 20000)
a2 = Account(102, 12000)
a3 = Account(103, 22000)

a1.withdraw(3000)
a2.deposit(3000)

print(a1.id, a1.get_balance())
print(a2.id, a2.get_balance())

print(Account.get_monthly_rate())
print(a1 > a2)
print(a1 + (a2 + a3))
print(a1)
