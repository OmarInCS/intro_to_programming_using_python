
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

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
        self.le_search.textChanged.connect(self.filter_emps_by_name)
        self.bt_add_dept.clicked.connect(self.show_add_dept_dialog)

    def load_depts(self):
        names = [d.dept_name for d in self.depts]
        self.cb_depts.addItems(names)

    def load_emps(self):
        self.tb_emps.setRowCount(0)
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
        self.load_emps()
        if idx != 0:
            dept = self.depts[idx - 1]
            for i, e in enumerate(self.emps):
                if e.dept_id != dept.dept_id:
                    self.tb_emps.hideRow(i)

    def filter_emps_by_name(self):
        self.load_emps()
        query = self.le_search.text().lower()
        if query != "":
            for i, e in enumerate(self.emps):
                if not e.emp_name.lower().startswith(query):
                    self.tb_emps.hideRow(i)

    def show_add_dept_dialog(self):
        dialog = loadUi("../view/add_dept.ui")
        locs = {str(d.loc_id) for d in self.depts}
        dialog.cb_locs.addItems(locs)
        choice = dialog.exec()

        if choice == 1:
            dept = Department(dialog.le_dept_id.text(),
                              dialog.le_dept_name.text(),
                              dialog.cb_locs.currentText())
            self.depts.append(dept)
            self.cb_depts.addItem(dept.dept_name)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()