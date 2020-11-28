from week3.day2.account import Account

a1 = Account(101, 20000)
# a2 = a1
a2 = Account(a1.id, a1.balance)

# a2.withdraw(500)
a2 - 500

print(a1.id, a1.balance)
print(a2.id, a2.balance)

print(a1 > a2)
print(a1)

