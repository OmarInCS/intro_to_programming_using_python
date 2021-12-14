
from week3.day3.employee import Employee

e1 = Employee("Ahmed", 10000, 2018)
e2 = Employee("Wael", 7000, 2020)

print(e1.name, e1.get_annual_salary(), e1.get_service_period())
print(e2.name, e2.get_annual_salary(), e2.get_service_period())
