
from week3.day3.account import Account

a1 = Account("Omar", 20000)
a2 = Account("Ahmed", 15000)

a1.withdraw(5000)
a2.deposit(5000)

print(a1.name, a1.get_balance(), a1.get_monthly_int())
print(a2.name, a2.get_balance(), a2.get_monthly_int())
