
from sqlite3 import connect

# conn = connect("C:\\sqlite\\hr.db")
#
# conn.close()
from week4.day3.department import Department

with connect("C:\\sqlite\\hr.db") as conn:
    cur = conn.cursor()
    sql = "SELECT * FROM departments"
    result = cur.execute(sql).fetchall()
    result = [Department(*row) for row in result]
    print(result)
