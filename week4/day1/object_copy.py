
from week4.day1.account import Account

x = Account(101, 20000)
# y = x
y = Account(x.id, x.get_balance())

y.withdraw(500)

print(x.get_balance())
print(y.get_balance())
