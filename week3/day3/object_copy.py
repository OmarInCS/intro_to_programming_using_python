from week3.day3.account import Account

a1 = Account(101, 20000)
a2 = a1
a3 = Account(a1.id, a1.get_balance())

a1.withdraw(1333)

print(a1)
print(a2)
print(a3)