
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from hr_system.model.department import Department
from hr_system.model.employee import Employee
from hr_system.view.main_window import Ui_Form


class HomeWidget(QWidget, Ui_Form):

    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

        self.depts = Department.get_all_depts()
        self.load_depts()

        self.emps = Employee.get_all_emps()
        self.load_emps()

        self.tb_emps.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.cb_depts.currentIndexChanged.connect(self.filter_emps_by_dept)
        self.le_search.textChanged.connect(self.filter_emps_by_name)
        self.bt_add_dept.clicked.connect(self.show_add_dept_dialog)
        self.bt_del_dept.clicked.connect(self.delete_dept)
        self.bt_exit.clicked.connect(app.exit)

    def load_depts(self):
        names = [d.dept_name for d in self.depts]
        self.cb_depts.addItems(names)

    def load_emps(self):
        self.tb_emps.setRowCount(0)
        for i, e in enumerate(self.emps):
            self.tb_emps.insertRow(i)
            for j, info in enumerate(e.__dict__.values()):
                self.tb_emps.setItem(i, j, QTableWidgetItem(str(info)))

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
        dialog = loadUi("view/add_dept.ui")
        locs = sorted({str(d.loc_id) for d in self.depts})
        dialog.cb_locs.addItems(locs)
        choice = dialog.exec()

        if choice == 1:
            new_dept = Department(dialog.le_dept_id.text(),
                                  dialog.le_dept_name.text(),
                                  dialog.cb_locs.currentText())
            self.depts.append(new_dept)
            self.cb_depts.addItem(new_dept.dept_name)
            new_dept.save_to_db()

    def delete_dept(self):
        idx = self.cb_depts.currentIndex()
        if idx != 0:
            self.cb_depts.removeItem(idx)
            dept = self.depts.pop(idx - 1)
            dept.delete_from_db()


app = QApplication([])
window = HomeWidget()
window.show()
app.exec()
