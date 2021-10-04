from week4.day1.sales_person import SalesPerson
from week4.day1.trainer import Trainer

t1 = Trainer("Ahmed", 7777)
s1 = SalesPerson("Wael", 5000, 0.1)

print(t1.get_annual_salary())
print(t1.get_total_salary())
print(s1.get_annual_salary())
print(s1.get_total_salary())

print(t1.__dict__)
print(t1.__class__)
print(t1)
