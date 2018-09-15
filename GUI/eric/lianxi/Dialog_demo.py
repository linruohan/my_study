#coding=utf-8
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class NumberFormatDlg(QDialog):
    def __init__(self,format,parent=None):
        super(NumberFormatDlg, self).__init__(parent)
        self.format=format.copy()

        thousandsLabel=QLabel("&Thousands separator【千分位】")
        self.thousandsEdit=QLineEdit(format["thousandsseparator"])
        thousandsLabel.setBuddy(self.thousandsEdit)
        decimalMarkerLabel=QLabel("Decimal &marker【小数点】")
        self.decimalMarkerEdit=QLineEdit(format["decimalmarker"])
        decimalMarkerLabel.setBuddy(self.decimalMarkerEdit)
        decimalPlacesLabel=QLabel("&Decimal places【小数空格】")
        self.decimalPlacesSpinBox=QSpinBox()
        decimalPlacesLabel.setBuddy(self.decimalPlacesSpinBox)
        self.decimalPlacesSpinBox.setRange(0,6)
        self.decimalPlacesSpinBox.setValue(format["decimalplaces"])
        self.redNegativesCheckBox=QCheckBox("&Red negative numbers【红负数】")
        self.redNegativesCheckBox.setChecked(format["rednegatives"])
        buttonBox=QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        buttonBox.button(QDialogButtonBox.Ok).setDefault(True)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        grid=QGridLayout(self)
        grid.addWidget(thousandsLabel,0,0)
        grid.addWidget(self.thousandsEdit,0,1)
        grid.addWidget(decimalMarkerLabel,1,0)
        grid.addWidget(self.decimalMarkerEdit,1,1)
        grid.addWidget(decimalPlacesLabel,2,0)
        grid.addWidget(self.decimalPlacesSpinBox,2,1)
        grid.addWidget(self.redNegativesCheckBox,3,0,1,2)
        grid.addWidget(buttonBox,4,0,1,2)

    def numberFormat(self):
        return self.format
    def accept(self):
        '''校验字符串'''
        class ThousandsError(Exception):pass
        class DecimalError(Exception):pass
        Punctuation=frozenset(" ,;:.")
        thousands=str(self.thousandsEdit.text())
        decimal=str(self.decimalMarkerEdit.text())
        try:
            if len(decimal)==0 :
                raise DecimalError("The decimal may not be empty.")
            if len(thousands)>1:
                raise ThousandsError("The thousand separator may only be empty or one character.")
            if len(decimal)>1:
                raise DecimalError("The decimal marker must be one character")
            if thousands==decimal:
                raise DecimalError("【thousands separator】 and  【dicimal marker】 must be different")
            if thousands and thousands not in Punctuation:
                raise ThousandsError("The thousands separator must be a punctuation symbol")
            if decimal and decimal not in Punctuation:
                raise DecimalError("The decimal marker must be a punctuation symbol")
        except ThousandsError as e:
            QMessageBox.warning(self,"Thousands Separator Error",str(e))
            self.thousandsEdit.selectAll()
            self.thousandsEdit.setFocus()
            return
        except DecimalError as e:
            QMessageBox.warning(self, "Decimal Marker Error", str(e))
            self.decimalMarkerEdit.selectAll()
            self.decimalMarkerEdit.setFocus()
            return
        self.format["thousandsseparator"]=thousands
        self.format["decimalmarker"]=decimal
        self.format["decimalplaces"]=self.decimalPlacesSpinBox.value()
        self.format["rednegatives"]=self.redNegativesCheckBox.isChecked()
        QDialog.accept(self)
class Example(QWidget):
    '''standard Dialog'''
    def __init__(self):
        super(Example, self).__init__()
        self.format=dict(thousandsseparator=",",decimalmarker=".",decimalplaces=2,rednegatives=False)
        self.initUI()
        self.show()
    def initUI(self):
        self.setWindowTitle(u"复利计算")
        self.resize(400, 100)
        self.setNumberFormat()

        self.show()
    def setNumberFormat(self):
        dialog=NumberFormatDlg(self.format,self)
        if dialog.exec_():
            self.format=dialog.numberFormat()
            self.refreshTable()
    def refreshTable(self):
        print('OK')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = Example()
    sys.exit(app.exec_())
