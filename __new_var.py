# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_new_var.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 80)
        MainWindow.setMinimumSize(QtCore.QSize(340, 80))
        MainWindow.setMaximumSize(QtCore.QSize(340, 80))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.m_label1 = QtWidgets.QLabel(self.centralwidget)
        self.m_label1.setGeometry(QtCore.QRect(9, 9, 70, 20))
        self.m_label1.setObjectName("m_label1")
        self.m_label2 = QtWidgets.QLabel(self.centralwidget)
        self.m_label2.setGeometry(QtCore.QRect(100, 9, 50, 20))
        self.m_label2.setObjectName("m_label2")
        self.m_label3 = QtWidgets.QLabel(self.centralwidget)
        self.m_label3.setGeometry(QtCore.QRect(170, 9, 50, 20))
        self.m_label3.setObjectName("m_label3")
        self.m_ok = QtWidgets.QPushButton(self.centralwidget)
        self.m_ok.setGeometry(QtCore.QRect(240, 30, 70, 21))
        self.m_ok.setObjectName("m_ok")
        self.m_color = QtWidgets.QComboBox(self.centralwidget)
        self.m_color.setGeometry(QtCore.QRect(9, 30, 69, 20))
        self.m_color.setObjectName("m_color")
        self.m_size = QtWidgets.QSpinBox(self.centralwidget)
        self.m_size.setGeometry(QtCore.QRect(100, 30, 50, 20))
        self.m_size.setSuffix("")
        self.m_size.setPrefix("")
        self.m_size.setMinimum(24)
        self.m_size.setMaximum(45)
        self.m_size.setObjectName("m_size")
        self.m_price = QtWidgets.QSpinBox(self.centralwidget)
        self.m_price.setGeometry(QtCore.QRect(170, 30, 51, 20))
        self.m_price.setMinimum(500)
        self.m_price.setMaximum(100000)
        self.m_price.setObjectName("m_price")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.m_label1.setText(_translate("MainWindow", "color"))
        self.m_label2.setText(_translate("MainWindow", "size"))
        self.m_label3.setText(_translate("MainWindow", "price"))
        self.m_ok.setText(_translate("MainWindow", "ok"))