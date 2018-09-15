# coding=utf-8
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class NumberFormatDlg(QDialog):
    def __init__(self, format,func, parent=None):
        super(NumberFormatDlg, self).__init__(parent)
        self.setWindowTitle("Set Number Format (Modeless)")
        self.format =format
        self.callback=func
        punctuationRe = QRegExp(r"[ ,;:.]")
        '''动态验证--preventative validation'''
        thousandsLabel = QLabel("&Thousands separator【千分位】")
        self.thousandsEdit = QLineEdit(format["thousandsseparator"])
        thousandsLabel.setBuddy(self.thousandsEdit)
        self.thousandsEdit.setMaxLength(1)
        self.thousandsEdit.setValidator(QRegExpValidator(punctuationRe, self))

        decimalMarkerLabel = QLabel("Decimal &marker【小数点】")
        self.decimalMarkerEdit = QLineEdit(format["decimalmarker"])
        decimalMarkerLabel.setBuddy(self.decimalMarkerEdit)
        self.decimalMarkerEdit.setMaxLength(1)
        self.decimalMarkerEdit.setValidator(QRegExpValidator(punctuationRe, self))
        self.decimalMarkerEdit.setInputMask("X")  # 输入掩码 必须有一位

        decimalPlacesLabel = QLabel("&Decimal places【小数空格】")
        self.decimalPlacesSpinBox = QSpinBox()
        decimalPlacesLabel.setBuddy(self.decimalPlacesSpinBox)
        self.decimalPlacesSpinBox.setRange(0, 6)
        self.decimalPlacesSpinBox.setValue(format["decimalplaces"])

        self.redNegativesCheckBox = QCheckBox("&Red negative numbers【红负数】")
        self.redNegativesCheckBox.setChecked(format["rednegatives"])

        self.thousandsEdit.textChanged.connect(self.checkAndFix)
        self.decimalMarkerEdit.textChanged.connect(self.checkAndFix)
        self.decimalPlacesSpinBox.valueChanged.connect(self.apply)
        self.redNegativesCheckBox.toggled[bool].connect(self.apply)

        grid = QGridLayout(self)
        grid.addWidget(thousandsLabel, 0, 0)
        grid.addWidget(self.thousandsEdit, 0, 1)
        grid.addWidget(decimalMarkerLabel, 1, 0)
        grid.addWidget(self.decimalMarkerEdit, 1, 1)
        grid.addWidget(decimalPlacesLabel, 2, 0)
        grid.addWidget(self.decimalPlacesSpinBox, 2, 1)
        grid.addWidget(self.redNegativesCheckBox, 3, 0, 1, 2)

    def checkAndFix(self):
        thousands = str(self.thousandsEdit.text())
        decimal = str(self.decimalMarkerEdit.text())
        if thousands == decimal:
            self.thousandsEdit.clear()
            self.thousandsEdit.setFocus()
        if len(decimal) == 0:
            self.decimalMarkerEdit.setText('.')
            self.decimalMarkerEdit.selectAll()
            self.decimalMarkerEdit.setFocus()
        self.apply()

    def apply(self):
        '''窗体级验证'''
        self.format["thousandsseparator"] = str(self.thousandsEdit.text())
        self.format["decimalmarker"] = str(self.decimalMarkerEdit.text())
        self.format["decimalplaces"] = self.decimalPlacesSpinBox.value()
        self.format["rednegatives"] = self.redNegativesCheckBox.isChecked()
        self.callback()



class Example(QWidget):
    '''standard Dialog'''

    def __init__(self):
        super(Example, self).__init__()
        self.numberFormatDlg=None
        self.format = dict(thousandsseparator=",", decimalmarker=".", decimalplaces=2, rednegatives=False)
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle(u"复利计算")
        self.resize(400, 100)
        self.setNumberFormat()

        self.show()

    def setNumberFormat(self):
        if self.numberFormatDlg is None:
            self.numberFormatDlg = NumberFormatDlg(self.format, self.refreshTable,self)
        self.numberFormatDlg.show()
        self.numberFormatDlg.raise_()#激活对话框并使其获得光标
        self.numberFormatDlg.activateWindow()
    def refreshTable(self):
        print('123')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Example()
    sys.exit(app.exec_())
