
from PyQt5.QtWidgets import *

from hr_system.model.employee import Employee
from hr_system.view.main_window import Ui_Form
from hr_system.model.department import Department


class MyWidget(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.depts = Department.get_all_depts()
        self.load_depts()

        self.emps = Employee.get_all_emps()
        self.load_emps()

        print()

    def load_depts(self):
        names = [d.dept_name for d in self.depts]
        self.cb_depts.addItems(names)

    def load_emps(self):

        for i, e in enumerate(self.emps):
            self.tb_emps.insertRow(i)
            for j, value in enumerate(e.__dict__.values()):
                self.tb_emps.setItem(i, j, QTableWidgetItem(str(value)))


app = QApplication([])
window = MyWidget()
window.show()
app.exec()
