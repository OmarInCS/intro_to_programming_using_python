
from PyQt5.QtWidgets import *

from hr_system.model.department import Department
from hr_system.model.employee import Employee
from hr_system.view.hr_system import Ui_Form


class MainWindow(QWidget, Ui_Form):

    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

        self.depts = Department.get_all_depts()
        self.load_depts()
        self.emps = Employee.get_all_emps()
        self.load_emps()

        self.cb_depts.currentIndexChanged.connect(self.filter_emps_by_dept)
        self.le_search.textChanged.connect(self.filter_emps_by_name)

    def load_depts(self):
        dept_names = [d.dept_name for d in self.depts]
        self.cb_depts.addItems(dept_names)

    def load_emps(self):
        self.tb_emps.setRowCount(0)
        for i, emp in enumerate(self.emps):
            self.tb_emps.insertRow(i)
            for j, value in enumerate(emp.__dict__.values()):
                self.tb_emps.setItem(i, j, QTableWidgetItem(str(value)))

    def filter_emps_by_dept(self, idx):
        self.load_emps()
        if idx != 0:
            dept = self.depts[idx - 1]
            for i, emp in enumerate(self.emps):
                if emp.dept_id != dept.dept_id:
                    self.tb_emps.hideRow(i)

    def filter_emps_by_name(self):
        self.load_emps()
        text = self.le_search.text().lower()
        if text != "":
            for i, emp in enumerate(self.emps):
                if not emp.emp_name.lower().startswith(text):
                    self.tb_emps.hideRow(i)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()