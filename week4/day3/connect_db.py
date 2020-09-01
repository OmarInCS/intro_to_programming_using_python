
from sqlite3 import connect
# from cx_Oracle import connect

from week4.day3.department import Department

db_path = "C:/sqlite/db/hr.db"
# db_path = "hr/hr@localhost/XEPDB1"

with connect(db_path) as conn:
    cur = conn.cursor()
    sql = "select * from departments"
    result = cur.execute(sql).fetchall()
    # result = [Department(*row) for row in result]
    print(result)
