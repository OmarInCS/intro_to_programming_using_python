
from week3.day4.account import Account

a1 = Account(101, 20000)
# a2 = a1
a2 = Account(a1.id, a1.get_balance())

a2.withdraw(300)

print(a1.get_balance())
print(a2.get_balance())