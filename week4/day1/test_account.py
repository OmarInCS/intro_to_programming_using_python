from week4.day1.account import Account

a1 = Account("Wael", 30000)

# a1.deposit(1000)
a1 += 1000
print(a1.get_balance())

# a1.withdraw(500)
a1 -= 500

print(a1.get_balance())
print(a1.get_monthly_int())
print(Account.annual_rate)
print(Account.get_monthly_rate())
