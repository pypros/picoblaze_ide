# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowForm.ui'
#
# Created: Mon Feb 06 19:11:41 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.plainTextEdit = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 60, 381, 231))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.buttonOpenFile = QtGui.QPushButton(Dialog)
        self.buttonOpenFile.setGeometry(QtCore.QRect(10, 30, 75, 23))
        self.buttonOpenFile.setObjectName("buttonOpenFile")
        self.buttonSaveFile = QtGui.QPushButton(Dialog)
        self.buttonSaveFile.setGeometry(QtCore.QRect(100, 30, 75, 23))
        self.buttonSaveFile.setObjectName("buttonSaveFile")
        self.translate = QtGui.QPushButton(Dialog)
        self.translate.setGeometry(QtCore.QRect(190, 30, 75, 23))
        self.translate.setObjectName("translate")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "PicoBlaze IDE", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonOpenFile.setText(QtGui.QApplication.translate("Dialog", "Open file", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSaveFile.setText(QtGui.QApplication.translate("Dialog", "Save file", None, QtGui.QApplication.UnicodeUTF8))
        self.translate.setText(QtGui.QApplication.translate("Dialog", "Translate", None, QtGui.QApplication.UnicodeUTF8))

