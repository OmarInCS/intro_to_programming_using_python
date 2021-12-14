from datetime import date


class Employee:

    def __init__(self, name, salary, hire_year):
        self.name = name
        self.salary = salary
        self.hire_year = hire_year

    def get_annual_salary(self):
        return self.salary * 12

    def get_service_period(self):
        return date.today().year - self.hire_year
