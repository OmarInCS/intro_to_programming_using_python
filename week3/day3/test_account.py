from week3.day3.account import Account

a1 = Account(101, 20000)
a2 = Account(102, 15000)

print(a1.get_monthly_int())
print(a2.get_monthly_int())
print(Account.get_monthly_rate())

print(a1 > a2)
a1 + 500
a1 - 1500

print(a1)