#coding=utf-8
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Example(QWidget):
    '''复利计算'''
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        self.show()
    def initUI(self):
        self.setWindowTitle(u"复利计算")
        self.resize(400, 100)
        self.box()
        self.setLayout(self.gridlay)
        self.show()
    def box(self):
        self.gridlay=QGridLayout()

        P_label=QLabel('本金（principle）：')
        self.Pv_label=QDoubleSpinBox()
        P_label.setBuddy(self.Pv_label)
        self.Pv_label.setPrefix('$')
        self.Pv_label.setRange(0,9999999999)
        self.Pv_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        R_label=QLabel('利率（rate）：')
        self.Rv_label=QDoubleSpinBox()
        R_label.setBuddy(self.Rv_label)
        self.Rv_label.setRange(0, 100)
        self.Rv_label.setSuffix('%')
        self.Rv_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        Y_label=QLabel('年限（years）：')
        self.Yv_label=QSpinBox()
        Y_label.setBuddy(self.Yv_label)
        self.Yv_label.setRange(0, 99)
        self.Yv_label.setSuffix(' years')
        self.Yv_label.setValue(self.Yv_label.value()+1)
        self.Yv_label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        A_label=QLabel('总计（Amount）：')
        self.result_label=QLabel()

        self.gridlay.addWidget(P_label,0,0)
        self.gridlay.addWidget(self.Pv_label,0,1)
        self.gridlay.addWidget(R_label,1,0)
        self.gridlay.addWidget(self.Rv_label,1,1)
        self.gridlay.addWidget(Y_label,2,0)
        self.gridlay.addWidget(self.Yv_label,2,1)
        self.gridlay.addWidget(A_label,3,0)
        self.gridlay.addWidget(self.result_label,3,1)


        self.Pv_label.valueChanged.connect(self.updateUI)
        self.Rv_label.valueChanged.connect(self.updateUI)
        self.Yv_label.valueChanged.connect(self.updateUI)


    def updateUI(self):
        result=float(self.Pv_label.value())*((1+float(self.Rv_label.value())/100.0))**float(self.Yv_label.value())
        self.result_label.setText('$ %.2f 元'%result)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = Example()
    sys.exit(app.exec_())
