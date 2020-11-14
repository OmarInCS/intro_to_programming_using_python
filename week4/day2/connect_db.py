from sqlite3 import connect

from week4.day2.department import Department

with connect("C:\\sqlite\\db\\hr.db") as conn:
    cur = conn.cursor()
    sql = "SELECT * FROM departments"
    result = cur.execute(sql).fetchall()
    result = [Department(*row) for row in result]
    print(result)
