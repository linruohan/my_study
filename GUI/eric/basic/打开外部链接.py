# -*- coding: utf-8 -*-

import sys, random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import webbrowser

class Ui_MainWindow(QWidget):
    item_name='PyQt打开外部链接'
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.tips_1=QLabel("网站：<a href='http://code.py40.com'>http://code.py40.com</a>")
        self.tips_1.setOpenExternalLinks(True)

        self.btn_webbrowser=QPushButton('webbrowser',self)
        self.btn_webbrowser.clicked.connect(self.btn_webbrowser_Clicked)

        grid=QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.btn_webbrowser,1,0)
        grid.addWidget(self.tips_1,2,0)
        self.setLayout(grid)

        self.resize(350,150)
        self.setMinimumSize(266,304)
        self.setMaximumSize(266,304)
        self.center()
        self.setWindowTitle(self.item_name)
        self.show()
    def btn_webbrowser_Clicked(self):
        webbrowser.open('http://www/paoquba.com')
    def center(self):
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app=QApplication(sys.argv)
    a=Ui_MainWindow()
    sys.exit(app.exec_())