#!/usr/bin/env python
# -*- coding: utf-8 -*-
#By mad_dev(A'mmer Almadani)
# Form implementation generated from reading ui file 'simpleXOR_encrypter_v2.ui'
#
# Created: Fri Sep 14 19:59:56 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import SimpleXOR
import datetime
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

now = datetime.datetime.now()
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(336, 297)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Select_BTN = QtGui.QPushButton(Form)
        self.Select_BTN.setObjectName(_fromUtf8("Select_BTN"))
        self.horizontalLayout.addWidget(self.Select_BTN)
        self.label = QtGui.QLabel(Form)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.plainTextEdit = QtGui.QPlainTextEdit(Form)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText(_fromUtf8(""))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.Clear = QtGui.QPushButton(Form)
        self.Clear.setObjectName(_fromUtf8("Clear"))
        self.gridLayout.addWidget(self.Clear, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.Select_BTN, QtCore.SIGNAL(_fromUtf8("clicked()")), self.selectFile) #File Dialog
        QtCore.QObject.connect(self.Clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.plainTextEdit.clear) #Clear All
        QtCore.QObject.connect(self.Clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label.clear) #Clear All
       
        QtCore.QMetaObject.connectSlotsByName(Form)

    def selectFile(self):
        dialog = QtGui.QFileDialog
        fileDialog = dialog.getOpenFileName(Form)
        filePath = self.label.setText(fileDialog)
        
        f = open(fileDialog, 'r') 
        with f:        
            data = f.read()
            l = len(data) 
            f.close() #not sure this is the right place
            key= SimpleXOR.rand(l)
            xor = SimpleXOR.xor_en(data, ke=key)

            log = """Date: """ + str(now) + '\n'+ """
Original Message: """ + str(data) + """
Number of Characters: """ + str(l) + '\n'+ """
Key: [""" + str(key) + """]""" + '\n'+ """ 
Encrypted Message: ["""+ str(xor) + """]"""

            self.plainTextEdit.setPlainText(log)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("SimpleXOR-EncrypterGui", "SimpleXOR-EncrypterGui", None, QtGui.QApplication.UnicodeUTF8))
        self.Select_BTN.setText(QtGui.QApplication.translate("Form", "Select File and Encrypt", None, QtGui.QApplication.UnicodeUTF8))
       
        self.label_2.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p align=\"center\">Log</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.Clear.setText(QtGui.QApplication.translate("Form", "Clear All", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

