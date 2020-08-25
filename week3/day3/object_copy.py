
from week3.day3.account import Account

a1 = Account(101, 20000)
# a2 = a1
a2 = Account(102, a1.get_balance())

print(a1)
print(a2)

a2.withdraw(500)

print(a1)
print(a2)
