from week4.day2.employee import Employee


class SalesPerson(Employee):

    def __init__(self, emp_id, emp_name, salary, comm):
        Employee.__init__(self, emp_id, emp_name, salary)
        self.comm = comm

    def get_total_salary(self):
        return self.salary + self.salary * self.comm

