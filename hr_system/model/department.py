from cx_Oracle import connect


class Department:

    def __init__(self, dept_id, dept_name, mgr_id, loc_id):
        self.dept_id = dept_id
        self.dept_name = dept_name
        self.mgr_id = mgr_id
        self.loc_id = loc_id

    def __repr__(self):
        return self.dept_name

    @staticmethod
    def get_all_depts():
        url = "hr/hr@localhost/XEPDB1"

        with connect(url) as conn:
            cur = conn.cursor()
            query = "select * from departments"
            result = cur.execute(query).fetchall()
            result = [Department(*row) for row in result]

            return result

    def save_to_db(self):
        url = "hr/hr@localhost/XEPDB1"

        with connect(url) as conn:
            cur = conn.cursor()
            sql = "INSERT INTO departments VALUES (:dept_id, :dept_name, :mgr_id, :loc_id)"
            cur.execute(sql, self.__dict__)
            conn.commit()

    def delete_from_db(self):
        url = "hr/hr@localhost/XEPDB1"

        with connect(url) as conn:
            cur = conn.cursor()
            sql = f"DELETE FROM departments WHERE department_id = {self.dept_id}"
            cur.execute(sql)
            conn.commit()