
from PyQt5.QtWidgets import *

from hr_system.model.department import Department
from hr_system.view.main_window import Ui_Form


class MyWidget(QWidget, Ui_Form):

    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

        self.depts = Department.get_all_depts()
        self.load_depts()

    def load_depts(self):
        names = [d.dept_name for d in self.depts]
        self.cb_depts.addItems(names)


app = QApplication([])
window = MyWidget()
window.show()
app.exec()