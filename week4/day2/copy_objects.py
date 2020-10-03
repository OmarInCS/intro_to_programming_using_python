
from week4.day2.account import Account

x = Account(101, 20000)
# y = x
y = x.copy()

y.withdraw(333)

print(x.get_balance())
print(y.get_balance())