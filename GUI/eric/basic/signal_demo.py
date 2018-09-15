#coding=utf-8
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWidgets import QApplication
class Example(QWidget):
    '''信号切换'''
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        self.show()
    def initUI(self):
        self.setWindowTitle("QTabWidget")
        self.resize(400, 100)
        vbox = QVBoxLayout(self)
        self.label=QLabel()
        btn1=QPushButton('one')
        btn2=QPushButton('two')
        btn3=QPushButton('three')
        btn4=QPushButton('four')
        btn5=QPushButton('five')
        btn6=QPushButton('six')
        for btn in (btn1,btn2,btn3,btn4,btn5,btn6):
            btn.clicked.connect(self.anybtn)
            vbox.addWidget(btn)
        vbox.addWidget(self.label)


        self.show()
    def anybtn(self):
        btn=self.sender()
        if btn is None or not isinstance(btn,QPushButton):
            return
        self.label.setText(btn.text())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = Example()
    sys.exit(app.exec_())
