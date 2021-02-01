from sqlite3 import connect

from week4.day2.department import Department

path = "C:\\Users\\OmarKarem\\SemicolonGD\\Python\\intro_to_python_programming\\week4\\day2\\hr.db"

with connect(path) as conn:
    cur = conn.cursor()
    sql = "SELECT * FROM departments"
    result = cur.execute(sql).fetchall()
    result = [Department(*row) for row in result]
    print(result)