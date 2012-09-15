#!/usr/bin/env python
# -*- coding: utf-8 -*-
#By mad_dev(A'mmer Almadani)
# Form implementation generated from reading ui file 'simpleXOR_encrypter.ui'
#
# Created: Sat Sep 15 04:17:58 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import SimpleXOR
import time
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(872, 291)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Guardian Laser"))
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.encrypted_label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Radio Space"))
        font.setPointSize(14)
        self.encrypted_label.setFont(font)
        self.encrypted_label.setObjectName(_fromUtf8("encrypted_label"))
        self.verticalLayout_3.addWidget(self.encrypted_label)
        self.encrypted_text = QtGui.QTextEdit(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setBold(True)
        font.setWeight(75)
        self.encrypted_text.setFont(font)
        self.encrypted_text.setReadOnly(True)
        self.encrypted_text.setAcceptRichText(False)
        self.encrypted_text.setObjectName(_fromUtf8("encrypted_text"))
        self.verticalLayout_3.addWidget(self.encrypted_text)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 2, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.original_label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Radio Space"))
        font.setPointSize(14)
        self.original_label.setFont(font)
        self.original_label.setObjectName(_fromUtf8("original_label"))
        self.verticalLayout.addWidget(self.original_label)
        self.Original_text = QtGui.QTextEdit(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setBold(True)
        font.setWeight(75)
        self.Original_text.setFont(font)
        self.Original_text.setReadOnly(True)
        self.Original_text.setObjectName(_fromUtf8("Original_text"))
        self.verticalLayout.addWidget(self.Original_text)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.generated_label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Radio Space"))
        font.setPointSize(14)
        self.generated_label.setFont(font)
        self.generated_label.setObjectName(_fromUtf8("generated_label"))
        self.verticalLayout_2.addWidget(self.generated_label)
        self.Key_text = QtGui.QTextEdit(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setBold(True)
        font.setWeight(75)
        self.Key_text.setFont(font)
        self.Key_text.setReadOnly(True)
        self.Key_text.setObjectName(_fromUtf8("Key_text"))
        self.verticalLayout_2.addWidget(self.Key_text)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.selectBtnAndEncrypt = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Radio Space"))
        font.setPointSize(12)
        self.selectBtnAndEncrypt.setFont(font)
        self.selectBtnAndEncrypt.setObjectName(_fromUtf8("selectBtnAndEncrypt"))
        self.gridLayout.addWidget(self.selectBtnAndEncrypt, 1, 0, 1, 1)
        self.clearBtn = QtGui.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Radio Space"))
        font.setPointSize(12)
        self.clearBtn.setFont(font)
        self.clearBtn.setObjectName(_fromUtf8("clearBtn"))
        self.gridLayout.addWidget(self.clearBtn, 2, 0, 1, 1)
        self.filePath = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        self.filePath.setFont(font)
        self.filePath.setText(_fromUtf8(""))
        self.filePath.setObjectName(_fromUtf8("filePath"))
        self.gridLayout.addWidget(self.filePath, 1, 1, 1, 1)
        self.time = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        self.time.setFont(font)
        self.time.setText(_fromUtf8(""))
        self.time.setObjectName(_fromUtf8("time"))
        self.gridLayout.addWidget(self.time, 1, 2, 1, 1)
        self.originalCharCount = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        self.originalCharCount.setFont(font)
        self.originalCharCount.setText(_fromUtf8(""))
        self.originalCharCount.setObjectName(_fromUtf8("originalCharCount"))
        self.gridLayout.addWidget(self.originalCharCount, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.clearBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Original_text.clear)
        QtCore.QObject.connect(self.clearBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Key_text.clear)
        QtCore.QObject.connect(self.clearBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.encrypted_text.clear)
        QtCore.QObject.connect(self.clearBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.originalCharCount.clear)
        QtCore.QObject.connect(self.clearBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.filePath.clear)
        QtCore.QObject.connect(self.clearBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.time.clear)

        QtCore.QObject.connect(self.selectBtnAndEncrypt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.selectFile)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def selectFile(self):
        dialog = QtGui.QFileDialog
        fileDialog = dialog.getOpenFileName(Form)
        filePathP = self.filePath.setText(fileDialog)
        
        f = open(fileDialog, 'r')
        now = time.time() 
        with f:        
            data = f.read()
            l = len(data)
            for i in data:  
                key= SimpleXOR.rand(l)
            xor = SimpleXOR.xor_en(data, ke=key)

            self.Original_text.setText(data)
            self.Key_text.setText(key)
            self.encrypted_text.setText(xor)

            nowTime = 'Process took %s s' %str(time.time() - now)
            self.time.setText(nowTime)

            charCount = "There are %s characters in the original file" %l
            self.originalCharCount.setText(charCount)

        f.close()
    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "SimpleXOR-EncrypterGui", None, QtGui.QApplication.UnicodeUTF8))
        self.encrypted_label.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p align=\"center\">Encrypted Data</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.original_label.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p align=\"center\">Original</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.generated_label.setText(QtGui.QApplication.translate("Form", "<html><head/><body><p align=\"center\">Generated Key</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.selectBtnAndEncrypt.setText(QtGui.QApplication.translate("Form", "Encrypt", None, QtGui.QApplication.UnicodeUTF8))
        self.clearBtn.setText(QtGui.QApplication.translate("Form", "Clear All", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

