from week3.day4.account import Account

a1 = Account("Omar", 20000)
a2 = Account("Khalid", 15000)

a1.withdraw(5000)
a2.deposit(5000)

print(a1.name, a1.get_balance())
print(a2.name, a2.get_balance())

print(Account.get_monthly_rate())
