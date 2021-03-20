
from week3.day2.account import Account

a1 = Account("Omar", 20000)
a2 = Account("Khaled", 30000)

a2.withdraw(10000)
a1.deposit(10000)

print(a1.name, a1.get_balance())
print(a2.name, a2.get_balance())

print(Account.annual_rate)
print(Account.get_monthly_rate())
