import sys, random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn=QPushButton('btn',self)
        btn.move(20,20)
        btn.clicked.connect(self.btn_apk_Clicked)
        self.setGeometry(300, 300, 300, 220)  # x,y,w,h
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def btn_apk_Clicked(self):
        apk_file = self.cacheUtils.getCacheString('apk_file', self.current_file_dictory)

        filename, _ = QFileDialog.getOpenFileName(self, apk_file);
        # text=open(filename,'r').read()
        self.btn_apk.setText(filename)
        self.cacheUtils.setCacheString('apk_file', filename)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())