from week4.day4.employee import Employee
from week4.day4.sales_person import SalesPerson
from week4.day4.trainer import Trainer

t1 = Trainer(101, "Ahmed", 10000, 1000)
s1 = SalesPerson(102, "Belal", 10000, 0.02)
e1 = Employee(103, "Wael", 10000)

print(t1.emp_name, t1.get_total_salary(), t1.get_annual_salary())
print(s1.emp_name, s1.get_total_salary(), s1.get_annual_salary())
print(e1.emp_name, e1.get_annual_salary())