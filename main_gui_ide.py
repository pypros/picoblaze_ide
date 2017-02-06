from PySide.QtCore import *
from PySide.QtGui import *
import sys

import main_window_form


class MainDialog(QDialog, main_window_form.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()
