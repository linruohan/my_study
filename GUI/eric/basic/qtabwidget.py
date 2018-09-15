# QMainWindow + QtabWidget
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWidgets import QApplication
class Example(QWidget):
    '''QtabWidget 实现 菜单栏 和 标签'''
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        self.show()
    def initUI(self):
        self.setWindowTitle("QTabWidget")
        self.resize(400, 100)
        tab = QTabWidget()
        tab.addTab(QLabel("Tab Content 1"), "Tab & 1")
        tab.addTab(QLabel("Tab Content 2"), "Tab & 2")
        tab.addTab(QLabel("Tab Content 3"), "Tab & 3")
        tab.setCurrentIndex(0)
        vbox = QVBoxLayout()
        vbox.addWidget(tab)
        self.setLayout(vbox)
        self.show()
if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = Example()
    sys.exit(app.exec_())
