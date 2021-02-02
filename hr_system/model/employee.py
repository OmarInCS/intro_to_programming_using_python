from cx_Oracle import connect


class Employee:

    def __init__(self, emp_id, emp_name, email, hire_date, job_id, salary, dept_id):
        self.emp_id = emp_id
        self.emp_name: str = emp_name
        self.email = email
        self.hire_date = hire_date
        self.job_id = job_id
        self.salary = salary
        self.dept_id = dept_id

    def __repr__(self):
        return self.emp_name

    @staticmethod
    def get_all_emps():
        with connect("hr/hr@localhost/XEPDB1") as conn:
            cur = conn.cursor()
            sql = "select employee_id, last_name, email, hire_date, job_id, salary, department_id from employees"
            result = cur.execute(sql).fetchall()
            result = [Employee(*row) for row in result]

        return result

    def save_to_db(self):
        with connect("hr/hr@localhost/XEPDB1") as conn:
            cur = conn.cursor()
            sql = """INSERT INTO employees 
            (employee_id, last_name, email, hire_date, job_id, salary, department_id) 
            VALUES (:emp_id, :emp_name, :email, :hire_date, :job_id, :salary, :dept_id)"""
            cur.execute(sql, self.__dict__)
            conn.commit()

    def delete_from_db(self):
        with connect("hr/hr@localhost/XEPDB1") as conn:
            cur = conn.cursor()
            sql = f"DELETE FROM employees WHERE employee_id = {self.emp_id}"
            cur.execute(sql)
            conn.commit()