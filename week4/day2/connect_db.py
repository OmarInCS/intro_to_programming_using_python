
from sqlite3 import connect

from week4.day2.department import Department

url = "C:\\Users\\OmarKarem\\SemicolonGD\\Python\\resources\\hr.db"
with connect(url) as conn:
    cur = conn.cursor()
    query = "select * from departments"
    result = cur.execute(query).fetchall()
    result = [Department(*row) for row in result]
    print(result)
