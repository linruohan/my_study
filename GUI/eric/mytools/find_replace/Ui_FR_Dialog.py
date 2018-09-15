# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(417, 192)
        Dialog.setSizeGripEnabled(True)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(300, 10, 20, 171))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 281, 171))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.findLineLabel = QtWidgets.QLabel(self.widget)
        self.findLineLabel.setObjectName("findLineLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.findLineLabel)
        self.findLineEdit = QtWidgets.QLineEdit(self.widget)
        self.findLineEdit.setObjectName("findLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.findLineEdit)
        self.replaceLineLabel = QtWidgets.QLabel(self.widget)
        self.replaceLineLabel.setObjectName("replaceLineLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.replaceLineLabel)
        self.replaceLineEdit = QtWidgets.QLineEdit(self.widget)
        self.replaceLineEdit.setObjectName("replaceLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.replaceLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.caseCheckBox = QtWidgets.QCheckBox(self.widget)
        self.caseCheckBox.setObjectName("caseCheckBox")
        self.horizontalLayout_2.addWidget(self.caseCheckBox)
        self.wholeCheckBox = QtWidgets.QCheckBox(self.widget)
        self.wholeCheckBox.setEnabled(True)
        self.wholeCheckBox.setChecked(True)
        self.wholeCheckBox.setObjectName("wholeCheckBox")
        self.horizontalLayout_2.addWidget(self.wholeCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.SyntaxLabel = QtWidgets.QLabel(self.widget)
        self.SyntaxLabel.setObjectName("SyntaxLabel")
        self.horizontalLayout_3.addWidget(self.SyntaxLabel)
        self.syntaxComboBox = QtWidgets.QComboBox(self.widget)
        self.syntaxComboBox.setObjectName("syntaxComboBox")
        self.syntaxComboBox.addItem("")
        self.syntaxComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.syntaxComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(330, 10, 71, 171))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.findButton = QtWidgets.QPushButton(self.widget1)
        self.findButton.setObjectName("findButton")
        self.verticalLayout_2.addWidget(self.findButton)
        self.replaceButton = QtWidgets.QPushButton(self.widget1)
        self.replaceButton.setObjectName("replaceButton")
        self.verticalLayout_2.addWidget(self.replaceButton)
        self.replaceAllButton = QtWidgets.QPushButton(self.widget1)
        self.replaceAllButton.setObjectName("replaceAllButton")
        self.verticalLayout_2.addWidget(self.replaceAllButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.closeButton = QtWidgets.QPushButton(self.widget1)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout_2.addWidget(self.closeButton)
        self.findLineLabel.setBuddy(self.findLineEdit)
        self.replaceLineLabel.setBuddy(self.replaceLineEdit)
        self.SyntaxLabel.setBuddy(self.syntaxComboBox)

        self.retranslateUi(Dialog)
        self.closeButton.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.findLineEdit, self.replaceLineEdit)
        Dialog.setTabOrder(self.replaceLineEdit, self.caseCheckBox)
        Dialog.setTabOrder(self.caseCheckBox, self.wholeCheckBox)
        Dialog.setTabOrder(self.wholeCheckBox, self.syntaxComboBox)
        Dialog.setTabOrder(self.syntaxComboBox, self.findButton)
        Dialog.setTabOrder(self.findButton, self.replaceButton)
        Dialog.setTabOrder(self.replaceButton, self.replaceAllButton)
        Dialog.setTabOrder(self.replaceAllButton, self.closeButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.findLineLabel.setText(_translate("Dialog", "Find &what:"))
        self.replaceLineLabel.setText(_translate("Dialog", "Replace w&ith"))
        self.caseCheckBox.setText(_translate("Dialog", "&Case sensitive"))
        self.wholeCheckBox.setText(_translate("Dialog", "Wh&ole words"))
        self.SyntaxLabel.setText(_translate("Dialog", "&Syntax:"))
        self.syntaxComboBox.setItemText(0, _translate("Dialog", "Literal text"))
        self.syntaxComboBox.setItemText(1, _translate("Dialog", "Regular expression"))
        self.findButton.setText(_translate("Dialog", "&Find"))
        self.replaceButton.setText(_translate("Dialog", "&Replace"))
        self.replaceAllButton.setText(_translate("Dialog", "Replace &All"))
        self.closeButton.setText(_translate("Dialog", "Close"))