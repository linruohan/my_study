# coding=utf-8
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class NumberFormatDlg(QDialog):
    changed=pyqtSignal()
    def __init__(self, format, parent=None):
        super(NumberFormatDlg, self).__init__(parent)
        self.setWindowTitle("Set Number Format (Modeless)")
        self.setAttribute(Qt.WA_DeleteOnClose)  # 关闭后直接删除而不是隐藏
        self.format = format
        punctuationRe = QRegExp(r"[ ,;:.]")
        '''预防式验证--preventative validation'''
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

        buttonBox = QDialogButtonBox(QDialogButtonBox.Apply | QDialogButtonBox.Close)
        buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.apply)
        buttonBox.rejected.connect(self.reject)

        grid = QGridLayout(self)
        grid.addWidget(thousandsLabel, 0, 0)
        grid.addWidget(self.thousandsEdit, 0, 1)
        grid.addWidget(decimalMarkerLabel, 1, 0)
        grid.addWidget(self.decimalMarkerEdit, 1, 1)
        grid.addWidget(decimalPlacesLabel, 2, 0)
        grid.addWidget(self.decimalPlacesSpinBox, 2, 1)
        grid.addWidget(self.redNegativesCheckBox, 3, 0, 1, 2)
        grid.addWidget(buttonBox, 4, 0, 1, 2)

    def numberFormat(self):
        return self.format

    def apply(self):
        '''窗体级验证'''
        thousands = str(self.thousandsEdit.text())
        decimal = str(self.decimalMarkerEdit.text())
        if thousands == decimal:
            QMessageBox.warning(self, "format Error", "【thousands separator】 and  【dicimal marker】 must be different")
            self.thousandsEdit.selectAll()
            self.thousandsEdit.setFocus()
            return

        if len(decimal)==0:
            QMessageBox.warning(self, "format Error", "The decimal may not be empty.")
            self.decimalMarkerEdit.selectAll()
            self.decimalMarkerEdit.setFocus()
            return

        self.format["thousandsseparator"] = thousands
        self.format["decimalmarker"] = decimal
        self.format["decimalplaces"] = self.decimalPlacesSpinBox.value()
        self.format["rednegatives"] = self.redNegativesCheckBox.isChecked()
        self.changed.emit()#发送changed信号


class Example(QWidget):
    '''standard Dialog'''

    def __init__(self):
        super(Example, self).__init__()
        self.format = dict(thousandsseparator=",", decimalmarker=".", decimalplaces=2, rednegatives=False)
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle(u"复利计算")
        self.resize(400, 100)
        self.setNumberFormat()

        self.show()

    def setNumberFormat(self):
        dialog = NumberFormatDlg(self.format, self)
        dialog.changed.connect(self.refreshTable)
        dialog.show()

    def refreshTable(self):
        print('OK')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Example()
    sys.exit(app.exec_())
