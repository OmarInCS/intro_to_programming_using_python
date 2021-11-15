from week4.day2.sales_person import SalesPerson
from week4.day2.trainer import Trainer

t1 = Trainer(101, "Ahmed", 8000)
s1 = SalesPerson(102, "Wael", 10000, 0.05)

t1.overtime = 1000

print(t1.get_annual_salary(), t1.get_total_salary())
print(s1.get_annual_salary(), s1.get_total_salary())
