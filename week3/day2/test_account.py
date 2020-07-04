
from week3.day2.account import Account

a1 = Account(1, 20000)
a2 = Account(2, 20000)
a3 = Account(3, 20000)
a4 = Account(4, 20000)

a1.withdraw(2500)
a1.deposit(3333)

print(a1.id, a1.get_balance(), a1.get_monthly_int())

print(a1 > a2)
print(a3 == a4)
print(a2)
