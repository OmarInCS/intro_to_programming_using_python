
from sqlite3 import connect

from week4.day3.department import Department

with connect("C:\\sqlite\\db\\hr.db") as conn:
    cur = conn.cursor()
    stat = "select * from departments"
    data = cur.execute(stat).fetchall()
    data = [Department(*row) for row in data]
    print(data[3].dept_name)
