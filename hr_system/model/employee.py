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

    def __str__(self):
        return self.emp_name

    def __repr__(self):
        return self.emp_name

    @staticmethod
    def get_all_emps():
        url = "C:\\sqlite\\db\\hr.db"

        with connect(url) as conn:
            cur = conn.cursor()
            stat = "select employee_id, last_name, email, hire_date, job_id, salary, department_id from employees"
            result = cur.execute(stat).fetchall()
            result = [Employee(*row) for row in result]
            return result

    def save_to_db(self):
        url = "C:\\sqlite\\db\\hr.db"

        with connect(url) as conn:
            cur = conn.cursor()
            stat = '''insert into employees (employee_id, last_name, email, hire_date, job_id, salary, department_id) 
                    values (:emp_id, :emp_name, :email, :hire_date, :job_id, :salary, :dept_id)'''
            cur.execute(stat, self.__dict__)
            conn.commit()

    def delete_from_db(self):
        url = "C:\\sqlite\\db\\hr.db"

        with connect(url) as conn:
            cur = conn.cursor()
            stat = "delete from employees where employee_id = :emp_id"
            cur.execute(stat, self.__dict__)
            conn.commit()