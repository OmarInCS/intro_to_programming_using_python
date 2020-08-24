from datetime import date


class Employee:

    def __init__(self, name, salary, birth_year):
        self.name = name
        self.salary = salary
        self.birth_year = birth_year

    def get_annual_salary(self):
        return self.salary * 12

    def get_age(self):
        return date.today().year - self.birth_year

