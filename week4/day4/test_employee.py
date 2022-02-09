from week4.day4.sales_person import SalesPerson
from week4.day4.trainer import Trainer

t1 = Trainer(101, "Ahmed", 10000)
s1 = SalesPerson(102, "Ali", 10000, 0.2)

t1.overtime = 1000

print(t1.emp_name, t1.get_annual_salary(), t1.get_total_salary())
print(s1.emp_name, s1.get_annual_salary(), s1.get_total_salary())
