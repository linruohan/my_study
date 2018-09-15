# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\eric6\mytool\main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from union import Union


class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(524, 400)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 341, 171))
        self.groupBox.setMinimumSize(QtCore.QSize(0, 171))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(80, 60, 31, 16))
        self.label.setMinimumSize(QtCore.QSize(0, 16))
        self.label.setObjectName("label")
        self.province = QtWidgets.QComboBox(self.groupBox)
        self.province.setGeometry(QtCore.QRect(10, 60, 69, 22))
        self.province.setMinimumSize(QtCore.QSize(0, 22))
        self.province.setObjectName("province")

        self.city = QtWidgets.QComboBox(self.groupBox)
        self.city.setGeometry(QtCore.QRect(100, 60, 69, 22))
        self.city.setMinimumSize(QtCore.QSize(0, 22))
        self.city.setObjectName("city")

        self.town = QtWidgets.QComboBox(self.groupBox)
        self.town.setGeometry(QtCore.QRect(210, 60, 69, 22))
        self.town.setMinimumSize(QtCore.QSize(0, 22))
        self.town.setObjectName("town")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(170, 60, 31, 16))
        self.label_2.setMinimumSize(QtCore.QSize(0, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(290, 60, 31, 16))
        self.label_3.setMinimumSize(QtCore.QSize(0, 16))
        self.label_3.setObjectName("label_3")
        self.exitButton = QtWidgets.QPushButton(self.groupBox)
        self.exitButton.setGeometry(QtCore.QRect(240, 140, 75, 23))
        self.exitButton.setObjectName("exitButton")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 54, 12))
        self.label_4.setObjectName("label_4")
        self.sureBtn = QtWidgets.QPushButton(self.groupBox)
        self.sureBtn.setGeometry(QtCore.QRect(240, 100, 75, 23))
        self.sureBtn.setObjectName("sureBtn")
        self.resultedit = QtWidgets.QLabel(self.groupBox)
        self.resultedit.setGeometry(QtCore.QRect(110, 110, 81, 31))
        self.resultedit.setText("")
        self.resultedit.setObjectName("resultedit")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.province.activated['int'].connect(Union.on_province_activated)
        self.city.activated['int'].connect(Union.on_city_activated)
        self.town.activated['int'].connect(Union.on_town_activated)
        self.exitButton.clicked.connect(Union.on_exitButton_clicked)
        self.sureBtn.clicked.connect(Union.on_sureBtn_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label.setText(_translate("MainWindow", "省"))
        self.province.setItemText(0, _translate("MainWindow", "请选择"))
        self.city.setItemText(0, _translate("MainWindow", "请选择"))
        self.town.setItemText(0, _translate("MainWindow", "请选择"))
        self.label_2.setText(_translate("MainWindow", "县/市"))
        self.label_3.setText(_translate("MainWindow", "区"))
        self.exitButton.setText(_translate("MainWindow", "退出"))
        self.label_4.setText(_translate("MainWindow", "选择结果："))
        self.sureBtn.setText(_translate("MainWindow", "确定"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

