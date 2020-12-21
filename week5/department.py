
class Department:

    def __init__(self, dept_id, dept_name, mgr_id, loc_id):
        self.dept_id = dept_id
        self.dept_name = dept_name
        self.mgr_id = mgr_id
        self.loc_id = loc_id

    def __repr__(self):
        return self.dept_name

