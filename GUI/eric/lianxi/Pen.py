#coding=utf-8
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class PenPropertiesDlg(QDialog):
    '''画笔属性设置对话框'''
    def __init__(self,parrent=None):
        super(PenPropertiesDlg, self).__init__()

        widthlabel=QLabel('&Width:')
        self.widthSpinBox=QSpinBox()
        widthlabel.setBuddy(self.widthSpinBox)
        self.widthSpinBox.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
        self.widthSpinBox.setRange(0,24)

        self.beveledCheckBox=QCheckBox("&Beveled edges")
        stylelabel=QLabel("&Style:")
        self.styleComboBox=QComboBox()
        stylelabel.setBuddy(self.styleComboBox)
        self.styleComboBox.addItems(['Solid','Dashed','Dotted'])
        ''' 确定和取消box'''
        # Okbtn=QPushButton("&OK")
        # canclebtn=QPushButton("&Cancel")
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.button(QDialogButtonBox.Ok).setDefault(True)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        layout=QGridLayout(self)
        layout.addWidget(widthlabel,0,0)
        layout.addWidget(self.widthSpinBox,0,1)
        layout.addWidget(self.beveledCheckBox,0,2)
        layout.addWidget(stylelabel,1,0)
        layout.addWidget(self.styleComboBox,1,1,1,2)
        layout.addWidget(buttonBox,2,0,1,3)

class Example(QWidget):
    '''复利计算'''
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        self.show()
    def initUI(self):
        self.setWindowTitle(u"复利计算")
        self.resize(400, 100)
        self.width=2
        self.beveled=True
        self.style='Solid'
        self.setPenProperties()
        self.show()

    def setPenProperties(self):
        dialog=PenPropertiesDlg(self)
        dialog.widthSpinBox.setValue(self.width)
        dialog.beveledCheckBox.setChecked(self.beveled)
        dialog.styleComboBox.setCurrentIndex(dialog.styleComboBox.findText(self.style))
        if dialog.exec_():
            self.width=dialog.widthSpinBox.value()
            self.beveled=dialog.beveledCheckBox.isChecked()
            self.style=str(dialog.styleComboBox.currentText())
            self.updateData()
    def updateData(self):
        print(self.width,self.beveled,self.style)
if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = Example()
    sys.exit(app.exec_())
