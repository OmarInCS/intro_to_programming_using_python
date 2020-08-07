
from week4.day2.account import Account

a1 = Account(1, 20000)
a2 = Account(2, 15000)
a3 = Account(2, 15000)

a1.withdraw(500)
a1.deposit(1500)
print(a1.balance)

print(a1 > a2)
print(a3 == a2)
print(a1)
