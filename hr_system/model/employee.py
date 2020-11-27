import os
from sqlite3 import connect


class Employee:

    def __init__(self, emp_id, emp_name, email, hire_date, job_id, salary, dept_id):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.email = email
        self.hire_date = hire_date
        self.job_id = job_id
        self.salary = salary
        self.dept_id = dept_id

    def __repr__(self):
        return self.emp_name

    @staticmethod
    def get_all_emps():
        basedir = os.path.abspath(os.path.dirname(__file__))
        with connect(f"{basedir}\\hr.db") as conn:
            cur = conn.cursor()
            sql = "SELECT employee_id, last_name, email, hire_date, job_id, salary, department_id FROM employees"
            result = cur.execute(sql).fetchall()
            result = [Employee(*row) for row in result]

            return result

    def save_to_db(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        with connect(f"{basedir}\\hr.db") as conn:
            cur = conn.cursor()
            sql = "INSERT INTO employees (employee_id, last_name, email, hire_date, job_id, salary, department_id) VALUES (:emp_id, :emp_name, :email, :hire_date, :job_id, :salary, :dept_id)"
            cur.execute(sql, self.__dict__)
            conn.commit()

    def delete_from_db(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        with connect(f"{basedir}\\hr.db") as conn:
            cur = conn.cursor()
            sql = "DELETE FROM employees WHERE employee_id = :emp_id"
            cur.execute(sql, self.__dict__)
            conn.commit()
