from PySide.QtCore import *
from PySide.QtGui import *
import sys

import main_window_form


class MainDialog(QDialog, main_window_form.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.buttonOpenFile.clicked.connect(self.browser_open_file)
        self.buttonSaveFile.clicked.connect(self.browser_save_file)

        self.path_to_file = None

    def read_file(self, path_to_file):
        with open(path_to_file, 'r') as file:
            full_file = file.readlines()
        return full_file

    def transfer_text_to_editor(self, text):
        for line in text:
            self.plainTextEdit.appendPlainText(line[:-1])

    def browser_open_file(self):
        self.path_to_file = QFileDialog.getOpenFileName()[0]
        content_file = self.read_file(self.path_to_file)
        self.transfer_text_to_editor(content_file)

    def save_file(self, path_to_file):
        text = self.plainTextEdit.toPlainText()
        with open(path_to_file, 'w') as file:
            for line in text:
                file.write(line)

    def browser_save_file(self):
        self.path_to_file = QFileDialog.getSaveFileName()[0]
        self.save_file(self.path_to_file)


app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()
