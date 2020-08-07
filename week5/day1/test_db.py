
from sqlite3 import connect

from week5.day1.department import Department

url = "C:\\sqlite\\db\\hr.db"

with connect(url) as conn:
    cur = conn.cursor()
    stat = "select * from departments"
    result = cur.execute(stat).fetchall()
    result = [Department(*row) for row in result]
    print(result)
    for dept in result:
        print(dept.dept_id)
