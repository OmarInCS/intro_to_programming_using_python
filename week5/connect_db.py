from cx_Oracle import connect

from week5.department import Department

url = "hr/hr@localhost/XEPDB1"

with connect(url) as conn:
    cur = conn.cursor()
    query = "select * from departments"
    result = cur.execute(query).fetchall()
    result = [Department(*row) for row in result]
    print(result)

