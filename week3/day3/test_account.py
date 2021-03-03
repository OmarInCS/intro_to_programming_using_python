
from week3.day3.account import Account

a1 = Account(101, 20000)
a2 = Account(102, 15000)

a1.withdraw(5000)
a2.deposit(5000)

print(a1.id, a1.get_balance(), a1.get_monthly_int())
print(a2.id, a2.get_balance(), a2.get_monthly_int())
print(Account.get_monthly_rate())