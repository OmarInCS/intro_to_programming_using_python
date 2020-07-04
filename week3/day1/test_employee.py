
from week3.day1.employee import Employee

e1 = Employee("Omar", 10000, 2017)
e2 = Employee("Ahmed", 7000, 2013)

print(e1.name, e1.get_annual_salary(), e1.get_emp_level())
print(e2.name, e2.get_annual_salary(), e2.get_emp_level())