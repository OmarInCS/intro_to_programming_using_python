
class Department:

    def __init__(self, dept_id, dept_name, loc_id):
        self.dept_id = dept_id
        self.dept_name = dept_name
        self.loc_id = loc_id

    def __repr__(self):
        return self.dept_name

