
from PyQt5.QtWidgets import *

from hr_system.view.main_window import Ui_Form


class MyWidget(QWidget, Ui_Form):

    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)


app = QApplication([])
window = MyWidget()
window.show()
app.exec()