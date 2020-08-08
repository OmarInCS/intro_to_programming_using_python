
from PyQt5.QtWidgets import *

from hr_system.model.department import Department
from hr_system.model.employee import Employee
from hr_system.view.main_window import Ui_Form


class MainWindw(QWidget, Ui_Form):

    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

        self.depts = Department.get_all_depts()
        self.load_depts()


        self.emps = Employee

        print()

    def load_depts(self):
        dept_names = [d.dept_name for d in self.depts]
        self.cb_depts.addItems(dept_names)





app = QApplication([])
window = MainWindw()
window.show()
app.exec()