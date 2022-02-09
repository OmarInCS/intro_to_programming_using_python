from week4.day2.account import Account

a1 = Account("Ahmed", 20000)
a2 = Account("Wael", 15000)

a1.withdraw(5000)
a2.deposit(5000)

print(a1.name, a1.get_balance())
print(a2.name, a2.get_balance())
print(Account.annual_rate)
print(Account.get_monthly_rate())