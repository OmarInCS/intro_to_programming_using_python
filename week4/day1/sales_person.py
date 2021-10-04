from week4.day1.employee import Employee


class SalesPerson(Employee):

    def __init__(self, name, salary, comm):
        Employee.__init__(self, name, salary)
        self.comm = comm

    def get_total_salary(self):
        return self.salary + self.salary * self.comm
