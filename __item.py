# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_item.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(150, 220)
        Form.setMinimumSize(QtCore.QSize(150, 220))
        Form.setMaximumSize(QtCore.QSize(150, 220))
        self.picture = QtWidgets.QLabel(Form)
        self.picture.setGeometry(QtCore.QRect(0, 0, 150, 150))
        self.picture.setText("")
        self.picture.setObjectName("picture")
        self.name = QtWidgets.QLabel(Form)
        self.name.setGeometry(QtCore.QRect(0, 150, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name.setFont(font)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.price = QtWidgets.QLabel(Form)
        self.price.setGeometry(QtCore.QRect(0, 180, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.price.setFont(font)
        self.price.setAlignment(QtCore.Qt.AlignCenter)
        self.price.setObjectName("price")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name.setText(_translate("Form", "name"))
        self.price.setText(_translate("Form", "price"))