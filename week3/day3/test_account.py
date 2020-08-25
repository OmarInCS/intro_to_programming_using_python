
from week3.day3.account import Account

a1 = Account(101, 20000)
a2 = Account(102, 20000)
a3 = Account(103, 20000)

a1.withdraw(333)
a2.deposit(333)

print("Account 1:", a1.get_balance(), a1.get_monthly_int())
print("Account 2", a2.get_balance(), a2.get_monthly_int())

print(Account.get_monthly_rate())

print(a1 > a2)
print(a2 > a3)
print(a1 + a2)

print(a1)