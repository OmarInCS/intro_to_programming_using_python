
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from datetime import date

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

        self.cb_depts.currentIndexChanged.connect(self.filter_emps_by_dept)
        self.le_search.textChanged.connect(self.filter_emps_by_name)
        self.bt_add_dept.clicked.connect(self.show_add_dept_dialog)
        self.bt_exit.clicked.connect(app.exit)
        self.bt_del_dept.clicked.connect(self.delete_dept)
        self.bt_add_emp.clicked.connect(self.show_add_emp_dialog)
        self.bt_del_emp.clicked.connect(self.delete_emp)
        self.bt_export.clicked.connect(self.export_data)
        print()

    def load_depts(self):
        names = [d.dept_name for d in self.depts]
        self.cb_depts.addItems(names)

    def load_emps(self):
        self.tb_emps.setRowCount(0)
        for i, e in enumerate(self.emps):
            self.tb_emps.insertRow(i)
            for j, value in enumerate(e.__dict__.values()):
                self.tb_emps.setItem(i, j, QTableWidgetItem(str(value)))

    def filter_emps_by_dept(self, idx):
        self.load_emps()
        if idx != 0:
            dept = self.depts[idx - 1]
            for i, e in enumerate(self.emps):
                if e.dept_id != dept.dept_id:
                    self.tb_emps.hideRow(i)

    def filter_emps_by_name(self):
        self.load_emps()
        query = self.le_search.text().upper()
        if query != "":
            for i, e in enumerate(self.emps):
                if not e.emp_name.upper().startswith(query):
                    self.tb_emps.hideRow(i)

    def show_add_dept_dialog(self):
        dialog = loadUi("../view/add_dept.ui")
        locs = {str(d.loc_id) for d in self.depts}
        dialog.cb_locs.addItems(locs)
        choice = dialog.exec()

        if choice == 1:
            d = Department(dialog.le_dept_id.text(),
                           dialog.le_dept_name.text(),
                           dialog.cb_locs.currentText())
            self.cb_depts.addItem(d.dept_name)
            self.depts.append(d)
            d.save_to_db()

    def delete_dept(self):
        idx = self.cb_depts.currentIndex()
        if idx != 0:
            self.cb_depts.removeItem(idx)
            d = self.depts.pop(idx - 1)
            d.delete_from_db()

    def show_add_emp_dialog(self):
        dialog = loadUi("../view/add_emp.ui")
        dialog.de_hire_date.setDate(date.today())
        jobs = {str(e.job_id) for e in self.emps}
        dialog.cb_jobs.addItems(jobs)
        depts = [d.dept_name for d in self.depts]
        dialog.cb_depts.addItems(depts)
        choice = dialog.exec()

        if choice == 1:
            idx = dialog.cb_depts.currentIndex()
            e = Employee(dialog.le_emp_id.text(),
                         dialog.le_emp_name.text(),
                         dialog.le_email.text(),
                         dialog.de_hire_date.date().toString("yyyy-MM-dd"),
                         dialog.cb_jobs.currentText(),
                         dialog.le_salary.text(),
                         self.depts[idx - 1].dept_id)
            self.emps.append(e)
            self.load_emps()
            e.save_to_db()

    def delete_emp(self):
        idx = self.tb_emps.currentRow()
        if idx != -1:
            self.tb_emps.removeRow(idx)
            e = self.emps.pop(idx)
            e.delete_from_db()

    def export_data(self):
        info = QFileDialog().getSaveFileName(filter="CSV File(*.csv)")

        if info[0] != "":
            with open(info[0], "w") as file:
                row_count = self.tb_emps.rowCount()
                col_count = self.tb_emps.columnCount()

                for i in range(col_count):
                    header = self.tb_emps.horizontalHeaderItem(i).text()
                    file.write(header + ",")
                file.write("\n")

                for i in range(row_count):
                    if not self.tb_emps.isRowHidden(i):
                        for j in range(col_count):
                            data = self.tb_emps.item(i, j).text()
                            file.write(data + ",")
                        file.write("\n")


app = QApplication([])
window = MyWidget()
window.show()
app.exec()
