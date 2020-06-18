
from week3.day4.account import Account

a1 = Account(1, 20000)
a2 = Account(2, 15000)

a1.withdraw(2000)
a2.deposit(2000)

print(a1.id, a1.get_balance(), a1.get_monthly_int())
print(a2.id, a2.get_balance(), a2.get_monthly_int())

a3 = Account(2, 17000)

# print(a1 + a2)
print(a1 > a2)
print(a2 == a3)
print(a1)

