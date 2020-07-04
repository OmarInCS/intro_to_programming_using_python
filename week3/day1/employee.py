

class Employee:

    def __init__(self, name, salary, year):
        self.name = name
        self.salary = salary
        self.year = year

    def get_annual_salary(self):
        return self.salary * 12

    def get_service_period(self):
        return 2020 - self.year

    def get_emp_level(self):
        sp = self.get_service_period()
        if sp > 10:
            return "Level A"
        elif sp > 5:
            return "Level B"
        else:
            return "Level C"
