
from PyQt5.QtWidgets import *

from hr_system.model.department import Department
from hr_system.model.employee import Employee
from hr_system.view.main_window import Ui_Form


class MainWindow(QWidget, Ui_Form):

    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

        self.depts = Department.get_all_depts()
        self.load_depts()

        self.emps = Employee.get_all_emps()
        self.load_emps()

        self.cb_depts.currentIndexChanged.connect(self.filter_emps_by_dept)


    def load_depts(self):
        names = [d.dept_name for d in self.depts]
        self.cb_depts.addItems(names)

    def load_emps(self):

        for i, e in enumerate(self.emps):
            self.tb_emps.insertRow(i)
            self.tb_emps.setItem(i, 0, QTableWidgetItem(str(e.emp_id)))
            self.tb_emps.setItem(i, 1, QTableWidgetItem(str(e.emp_name)))
            self.tb_emps.setItem(i, 2, QTableWidgetItem(str(e.email)))
            self.tb_emps.setItem(i, 3, QTableWidgetItem(str(e.hire_date)))
            self.tb_emps.setItem(i, 4, QTableWidgetItem(str(e.job_id)))
            self.tb_emps.setItem(i, 5, QTableWidgetItem(str(e.salary)))
            self.tb_emps.setItem(i, 6, QTableWidgetItem(str(e.dept_id)))

    def filter_emps_by_dept(self, idx):

        if idx != 0:
            dept = self.depts[idx - 1]
            for i, e in enumerate(self.emps):
                if e.dept_id != dept.dept_id:
                    self.tb_emps.hideRow(i)





app = QApplication([])
window = MainWindow()
window.show()
app.exec()