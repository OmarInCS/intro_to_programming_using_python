
from cx_Oracle import connect

from week4.day2.department import Department

with connect("hr/hr@localhost/XEPDB1") as conn:
    cur = conn.cursor()
    sql = "select * from departments"
    result = cur.execute(sql).fetchall()
    result = [Department(*row) for row in result]
    print(result)
