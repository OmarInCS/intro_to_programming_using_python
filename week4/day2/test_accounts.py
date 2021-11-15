from week4.day2.checking_account import CheckingAccount
from week4.day2.saving_account import SavingAccount

ca1 = CheckingAccount("Ahmed", 5000, 1000)
sa1 = SavingAccount("Ali", 5000)

ca1.withdraw(5500)
sa1.withdraw(5500)

print(ca1.name, ca1.get_balance())
print(sa1.name, sa1.get_balance())

print(ca1.__dict__)
print(ca1.__class__)
